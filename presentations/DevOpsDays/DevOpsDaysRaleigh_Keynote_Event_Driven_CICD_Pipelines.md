# Event Driven Ci/CD Pipelines Keynote

## Overview

We are an ISV (Independent software vendor). We still deliver software to customers. We deliver RPMs, Debs, OCI Containers, on several architectures. We have a pipeline that builds, tests, stores, and eventually allows customers to download the software from us.

## Pipeline before Events

We go back to 2015. Our team was tasked with building a pipeline to produce RPMs for bare metal installs for our new product. At the time we had a regular software supply chain built around Jenkins (CI) and Gerrit (SCM). Over the course of a few years we built out a templated packaging system and an asynchronous task engine for building and packaging the software.

I know what you are thinking "Why a templating system?".

We didn't think asking developers to write hundreds of RPM spec files was going to go well.

Why did we write our own asynchronous task engine?

Kubernetes was not ready.

We leveraged Pulp (The Red Hat tech they use to deliver RPM content) as our repository technology. We have an instance of Artifactory and leverage it for storing dependency artifacts. We built out a metadata service to track all our units relationships. Over time we expanded the packaging system to include new package types.

The packaging system is pretty complex. It is driven by data that is transformed into native package types using templates. But we are not here to talk about packaging systems.

## Why Event Driven CI/CD?

In early 2019 the CTO comes to us and says "I want full CI/CD". Awesome. Now we could have chained together thousands of Jenkins jobs and got where we needed to be. But I am not a fan of Jenkins and I wanted to do something that was not tied to a specific CI.

Why? Because eventually you need to migrate to a newer CI technology. If your event system is tied to your CI technology it is considerably harder to migrate. You end up supporting both CI and Event Systems for a while. Because if you have a new pipeline you now have two pipelines.

I decided to build out an event driven framework that would allow us to expand over time. The Tools and Services would be written in Go/Python and Kafka would serve as our event message bus. We already had Kafka running in house so it was an easy choice.

## Decisions on tooling

Problem number one. We had to keep shipping software. Problem number two. We had invested several years in our current pipeline and it just works. So the question became how to add events to the current pipeline without starting over?

We have a multitude of CI tooling and services we wanted to tie into the system. Special clients are painful to distribute. We needed to be able to bolt events onto the current pipeline. There was aa need to be able to create events with tools that were readily available like curl, python, go, groovy, java, etc. We let the services handle talking to Kafka so the legacy pipeline just needs to be able to POST to the service. The decisions was made to use JSON for the messages since it is an industry standard and well supported in many languages. Using Avro was out based on the tooling requirements. Really because I never want to see another XML-RPC service in my lifetime.

## Receipts Gates and Stages

Let's talk about the core concepts of the system.

Actions are the tasks run to accomplish a result. Examples of Actions would be "ran unit tests", "built binary", "ran functional tests", and "ran integration tests". Actions produce receipts.

Receipts are the audit trail. They record all the information from the action. Receipts are JSON [Cloud Event Spec](https://github.com/cloudevents/spec) envelope around a [CNAB bundle](https://github.com/cnabio/cnab-spec) payload. The receipts have an identifier built into them that tells us whether the action passed or failed. We struggled to name the field because we wanted it to be a boolean so we weren't trying to string match. So we decided on multipass. Multipass.

NVRPP is used as the identifier of a unit for purposes of receipts.
Stands for Name, Version, Release, Platform ID, Package.
For example:

```text
  Name: foo
  Version: 1.0.0
  Release: 2023
  Platform ID: aarch64-oci-linux-2
  Package: docker
```

The structure is modeled after the RPM NEVRA.

We use NVRPP data to track receipts for units through the system.

Gates represent the action. Example would be if I have an action to "build the binary" I have a corresponding build gate to represent that set of tasks. We make receipts for build actions and post them to the build gate. 

Gates are satisfied by receipts, which track the completion of each gate's requirements. Posting a receipt to a gate results in a message on the Kafka bus. The makings of event driven.

Stages are a list of gates. When all gates in a stage have successful receipts (with
"multipass": true status), then the stage triggers it emits a message to the Kafka topic. Example would be [ "unit tests gate", "build gate", "functional tests gate", "integration tests gate" ].


Receipts, Gates, and Stages all have unique ids. For the unique identifier we decided to use a ULID. Basically a UUID with a built in timestamp that sort lexicographically. They are awesome.

## Where do we store the Receipts, Gates, and Stages?

The Gatekeeper was the first service we built. It is the central communication point for the system. It is a go service with a PostgreSQL DB. Always use Postgres. It has REST endpoints for CRUD operations for Receipts, Gates, and Stages. It has a GraphQL API endpoint for searching for Receipts, Gates, and Stages by various attributes. Receipt, Gates, and Stages can never be deleted, they are our audit trail. You can revoke a receipt regardless of its multipass. You can disable a stage so it stops emitting messages. The Gatekeeper is the source of the truth. It is the only service allowed to talk to the main Kafka Topics.

## We built a Gatekeeper, what was next?

Watchers listen to the Kafka topic for messages filtering on data they care about. When they find a message they care about they do something and create a receipt for the task when it is done. Most of our watchers are written in Go and run in kubernetes. They allow us to trigger actions based on events.

The first watcher we built registered test containers with our test container registration service. The second watcher we built was a webhook service. It uses the Go template language to form URL using data from the event message and attaches any receipts referenced in the event as a payload. This allowed us to trigger Jenkins jobs based on events and pass in data to the job. We use it to trigger non-event aware systems wherever we can. The third watcher we built was a Jira issue watcher. It can trigger Jira ticket creation from an event and it posts a receipt when the Jira issue is closed. We use this watcher for human interaction.

## The pipeline after we bolted events on

The chain of events all starts with a build. Developer pushes code, unit builds, build receipt is POSTd to Gatekeeper, Gatekeeper puts event on the bus, Watchers catch the event and do things, make receipts that create events that drive other watchers.

## We should wire up our automated test framework.

While we were working on building out our army of watchers our test team was adapting the test automation to be event driven. It took us a couple of months but eventually we had a workflow that was completely event driven. We built all the tests into test containers. 
Test containers are a containerized set of tests that test a specific software we ship to customers.
When we build a test container the build receipt event triggered the test container watcher to make gates for the new test container and register the container and its gates and the units it tested with the test registration service. The test automation service does a deployment of all the units. It then talks to the test container registration service to get a list of all the test containers and their gates and the units they test. It then runs the test containers (with injected configuration) in batches as kubernetes jobs. As each test container runs its tests they record the output of the tests as xunit. Each test container contains a tool that converts the xunit to a receipt with test count and sets the multipass for the receipt true or false based on results from the xunit. The tool posts the receipt to the test containers corresponding gate.

Once all the tests have run and passed for a particular unit the stage around its test gates will emit a message to the kafka topic. We then have a watcher that catches that message and promotes the unit in Pulp to the next level. No humans just robots. This was great for non-destructive testing and not so great for destructive testing.

## How did we incorporate destructive testing into the event-driven system?

So we have this amazing event driven system driving our automated testing that promotes our units towards production. We have teams outside of this framework doing destructive testing. How do we incorporate testing outside the automated framework? 

I mean, we obviously couldn't put it in with the rest of the automation. You can't rip the database out from under the software while test containers are running.

We set up the teams doing destructive testing outside of the automated framework with their own automation, usually kicked off by some event from the system. And then those teams create their own set gates that represent their destructive testing. As they run their destructive testing for an NVRPP (Name, Version, Release, Platform ID, Package), they post receipts to those gates with the results from the destructive tests.

So what we ended up with is a test container that gets registered with the unit that we want to test and what it does during the automated testing cycle is it goes out and finds the gates that are outside of the testing framework, asks those gates for the receipts, and checks the results of all of them. And if all the multipass are true it creates a passing test and if they're not true, it creates a failing test, Then the other utility reads the xunit and posts the receipt just like all the other test containers.

And now we have destructive testing outside of the framework incorporated without destroying the framework.

## How did we take this one step farther?

So now we get into the DevSecOps workflows. Now that we know how to get stuff outside of the pipeline into the pipeline, we decided that we were going to automate all of our security scans and create receipts for them as we go.

We went one step further after we run the security scan, we audit the scan and if the results do not meet the criteria for a clean scan we fail the receipt.

We have a Jira watcher that is watching the security tickets and when the issue is remediated and the the JIRA ticket closed, we post a receipt to the gate that says hey, we did our due diligence, it is now fixed. We are doing this for SAST, SCA, and OCI image scans.

We haven't turned this on as a gating feature yet, but it will be a gating feature in the future.

When gating is enabled we will create test containers in the automation framework that go and check the security gates and ask for passing receipts for the units.

So that's kind of how we're working through all that.

## Lessons Learned

### Observability

Event Driven Asynchronous Systems are really awesome.

Event Driven Asynchronous Systems have a huge observability challenge. Think about debugging tools and observability early process. A lot of teams will have no idea how to debug event driven pipeline issues. Write tracing tools early and make them easy to understand.

We found ourselves constantly writing chunks of Python And Go to figure out what's going on, and then those ended up becoming tools.

We built a UI that could leverage the Gatekeeper GraphQL API. It is great if you know what you are looking for. If you didn't know what you're looking for, you couldn't find it to save your life. So we had to augment it with a service that could discover gates and stages and decipher the business logic.

### JSON Schema

If you use JSON for anything write a schema for it and validate it against the schema. I was pretty adamant about this throughout the project and it served us well. One example was when you create a gate you can pass in a JSON schema for the custom section of the payload. Any receipt posted to the gate must pass full schema validation including the Cloud Event envelope, the CNAB payload, and the custom section in the CNAB. It helped eliminate the bad receipts. It did not help with spoofed receipts.

### Xunit Schema

If you use Xunit for anything write a schema for it and validate it against the schema. Sound familiar? Since we have a tool that converts Xunit to a receipt we need the xunit to be valid for a few reasons. One so the conversion works. Second so the data in the receipts is accurate. Sometimes the xunit would skip giving us a final test count and when we were process the data outside the event framework we would end up with negative test counts.

### Authentication (OIDC)

When we originally started we planned to implement authentication.

And we started to write an ACL system for the Gatekeeper.

As we designed it we realized we would never finish this and hit our goal release dates.

So we decided to go with the token base authentication and while it worked well enough.

And we could tell who posted what based on the token.

If you give a developer a token, they check it into a git repo and now everybody's got the token.

Last year we added OIDC authentication to all the endpoints in the system.

It made a big difference. We should have done it from the beginning.

Always do security first, right?

### Guardrails

Guard Rails. They are cool. We should have built some in from the beginning. You don't know what you don't know.

Basically, we had a box of Legos with no instructions. If you give devs a box of Legos, it doesn't mean they're gonna build something cool.

#### Event Message Size

Limit message size. At the time the default message size for Kafka out of the box was 1mb. We had a dev learning the system trigger his watcher on the same action as the watchers gate so it basically fork bombed itself into oblivion. We ended up with a 97mb receipt. We then decided to limit receipt size to 1mb and move large data to some other appropriate storage. Then we add the URI to the data in the receipt.

The fun forkbomb incident prompted us to go into the watchers and put a check so you couldn't watch for the event created by the gate that the watcher was posting its receipts to.

#### Rate Limiting

Kafka Consumer Groups are great. They keep track of the last message read so if a service drops off it can pick up where it left off. So our promotion watcher went down on a Saturday morning during a maintenance window. The automated testing framework did not and it was running along with no issues. While our promotion service was down the promotion events piled up into the thousands. We came in Monday morning saw the issue with the promotion service and decided that we would just start it back up and let it plow through the events it missed. The promotion watcher has no rate limiting. It just screamed through the thousands of events flooding the downstream services with requests. Eventually it started knocking things over and we had to shut it down. Rate Limiting.


#### Sanitize Inputs

In the first month we had a dev try to base64 encode a binary into a receipt... give a dev a database and they try to make it into a blob store. Make sure you sanitize the inputs. The system is very much a "garbage in garbage out" paradigm. Make sure your inputs are as good as your output.

Guardrails.

We should have guardrails.

### Watcher SDK

And that leads to "We should have written a Watcher SDK".

When we started we didn't think we're gonna have that many watchers.

So we ended up with a basically example watcher that you could fire up for demo purposes but didn't do anything.

We added a script to change the names. So if you need to create a new watcher, you downloaded this thing, you ran the script, and boom, you have a new watcher.

While we do have a library that we keep up to date that most watchers use, if we have written the Watcher SDK and made it really easy for the end users to just put the functions they needed in the task section of the Watcher, we could have kept the watchers up-to-date easier.

### CNAB

CNAB I wanted to use specs so I didn't have to write one and at the time CNAB seemed like a good choice at the time. The plan was to use the CNAB tooling to replay the Receipt if we needed to reproduce an action. That didn't go as planned.

There is a bunch of tooling around it and I was excited it. I was excited to use the CNAB and the CNAB tooling to replay my events. And I don't have to write new tooling. Tooling wasn't finished or polished. I was hoping to contribute upstream and some other stuff and we just didn't get around to it.

Not many people understood that part of the system as I intended it to work.

It is hard enough to understand the fact that it was event-driven, asynchronous, it had receipts, gates, and stages, so the intent of the CNAB kind of fell on the floor.

We proved out it would work during the POC, it never really was adopted well.

And so now I'm stuck with it until we do a rewrite.

### Misc

So you would think that a watcher would have a single gate to represent its tasks were finished.

Well we found out found a useful was that we ended up with the start gate and an end gate for the task and we wrapped it in the stage so that if one of the two if one of the two failed.

Of course the stage doesn't fire an event and then so downstream watchers would end up watching for the stage event which is always true.

And then it made it easier to troubleshoot.

So if you had a start receipt and no end receipt, you need to go to the watcher and check out the logs to find out what happened.

And if you didn't have a start receipt you go to the CI and see what happened there.

Just some traceability things that made it nice.

Write READMEs for every tool in the chain along with lots of examples.

Keep your documentation up to date.

Organize your documentation using a system like diataxis system.

When in doubt codify your instructions. A binary or script that asks the user questions and creates the things they need can be very helpful.

Do not turn debugging on in Production. Rework your logging to let info statements tell you all you need to know.

The learning curve on decentralized systems is high and not as easy to roll out as we had hoped. Think about on-boarding when you are designing the system. It needs to be simpler and easier to implement.


## Things I wish I had done

So a couple other things that I wish I had done so.

Cryptographically signed the receipts.

Had we cryptographically signed the receipts, then I would be almost done with my SLSA provenance.

I wish we could build an RBAC role-based access control (RBAC) service for the complete pipeline, not just the event driven system, that we could use to control access to all parts of the pipeline based on roles.

I wish we prioritized observability from the beginning.

## Things that went really well

We increased performance exponentially without having to rebuild the old pipeline.

It would take a week to get a a new version of a product to a customer. Now it takes 8 hours so.

All the testing automation increased our confidence in the quality of our software. The confidence allows us to create, update, patch, and ultimately ship software faster.

All the security automation decreased our time to remediation and increased our security observability.

The framework continues to allow us to quickly create event driven automation for any set of tasks we need.

You know a project was a success when teams outside of the pipeline team make use of it for their automation and the framework is transparent. We had a demo the other day showing off some really trick automation and I had a dev reach out to me and say "I remember your talk about event driven at the DevOps Unconference a few years ago... Has to be really satisfying to see how much progress is going on."

## CD Foundation (part of the Linux Foundation)

Some stuff that I'm involved in that I think you guys would be interested in if you want to come talk about pipelines and events.

I'm working with the CD foundation (part of the Linux Foundation).

We've got the CD events project, which is a common spec for continuous delivery events.

If I had the CD Events spec when I started this project, I would have used it instead of CNAB.

I'm working on this in the SIG events to help define the spec.

I'm also working in the SIG software supply chain and we would love to have you come out and talk to us.

There are public calendars for the SIGs where you can see the meeting times.

## Closing

I'm Smitty, and I'm afraid of robots.

Thank you.

Questions.
