# Event Driven Ci/CD Pipelines Keynote

## Overview

We are an ISV (Independent software vendor). We still deliver software to customers. We deliver RPMs, Debs, OCI Containers, on several architectures. We have a pipeline that builds, stores, and eventually allows customers to download their orders from us.

We go back to 2015. Our team was tasked with building a pipeline to produce RPMs for bare metal installs for our new product. At the time we had a regular software supply chain built around Jenkins (CI) and Gerrit. Over the course of a few years we built out a templated packaging system and an asynchronous task engine for building and packaging the software.

I know what you are thinking "Why a templating system?".

We didn't think it was going to go well asking developers to write hundreds of RPM spec files.

Why did we write our own asynchronous task engine?

Kubernetes was not ready.

We leveraged Pulp (The Red Hat tech they use to deliver RPM content) as our repository technology. We have an instance of Artifactory and leverage it for storing dependency artifacts. We built out a metadata service to track all our units relationships. Over time we expanded the packaging system to include new package types. 

The packaging system is pretty complex. It is driven by data that is transformed into native package types using templates. But we are not here to talk about packaging systems.

## Why Event Driven CI/CD?

In early 2019 the CTO comes to us and says "I want full CI/CD". Awesome. Now we could have chained together thousands of Jenkins jobs and got where we needed to be. But I am not a fan of Jenkins and I wanted to do something that was not tied to a specific CI.

Why? Because eventually you need to migrate to a newer CI technology. If your event system is not tied to your CI technology it is considerably easier to migrate over time, where you are supporting both CI for a while. Because if you have a new pipeline you now have two pipelines.

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

We use this data to track receipts for units through the system.

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

While we were working on building out our army of watchers our test team was adapting the test automation to be event driven. It took us a couple of months but eventually we had a workflow that was completely event driven. We built all the tests into test containers. The build receipt event triggered the test container watcher to make gates for the new test container and register the container and its gates and the units it tested with the test registration service. The test automation service does a deployment of all the units. It then talks to the test container registration service to get a list of all the test containers and their gates and the units they test. It then runs the test containers (with injected configuration) in batches as kubernetes jobs. As each test container runs its tests they record the output of the tests as xunit/junit. Each container contains a tool that converts the xunit to a receipt with test count and sets the multipass for the receipt true or false based on results from the xunit. The tool posts the receipt to the test containers corresponding gate.

Once all the tests have run and passed for a particular unit the stage around its test gates will emit a message to the kafka topic. We then have a watcher that catches that message and promotes the unit in Pulp to the next level. No humans just robots. This was great for non-destructive testing and not so great for destructive testing.

## How did we incorporate destructive testing into the event-driven system?

So we have this amazing event driven system driving our automated testing that promotes our units towards production. We have teams outside of this framework doing destructive testing. How do we incorporate testing outside the automated framework? 

I mean, we obviously couldn't put it in with the rest of the automation. You can't rip the database out from under the software while test containers are running.

We set up the teams doing destructive testing outside of the automated framework with their own automation, usually kicked off by some event from the system. And then those teams create their own set of gates and those gates represent their destructive testing. As they run their destructive testing for an NVRPP, they post receipts to those gates for the results of the destructive tests.

To tie the results back into the automated framework our team wrote a utility that could will go out and check those gates for receipts, create a Xunit output for the results of testing those gates. We create a test container with the utility and tell it what gates to check and it runs in the automated framework.

So what we ended up with is a test container that gets registered with the unit that we want to test and what it does during the automated testing cycle is it goes out and finds the gates that are outside of the testing framework, asks those gates for the receipts, and checks the results of all of them. And if all the multipass are true it creates a passing test and if they're not true, it creates a failing test, Then the other utility reads the xunit and posts the receipt just like all the other test containers.

And now we have destructive testing outside of the framework incorporated without destroying the framework.

## How did we take this one step farther?

So now we get into the DevSecOps workflows. Now that we know how to get stuff outside of the pipeline into the pipeline, we decided that we were gonna automate all of our security scans and create receipts for them as we did it.

But we went one step further and basically we are catching the event and we go, we run the security scan and we audit the security scan and if the security scan fails we create a JIRA issue.

We have juror watcher that is watching these issues obviously and when the issue is remediated and the issue and the the JIRA issues closed, we then go close to receipt in the gate that says hey, we did our due diligence, it is now fixed and we did this for SAST SCA and OCI image scan.

We haven't fully finished implementing this.

We haven't turned this on as a gating feature yet, but it will be a gating feature in the future and it's gonna work the same way.

We're gonna have test containers in the automation framework that go and check the security gates and ask for passing receipts for the DU and.

So that's kind of how we're working through all that.

## Lessons Learned

Event Driven Asynchronous Systems are really awesome.

Event Driven Asynchronous Systems have a huge observability challenge. Think about debugging tools and observability early process. A lot of teams will have no idea how to debug pipeline issues. Write tracing tools early and make them easy to understand. 



CNAB I wanted to use specs so I didn't have to write one and at the time CNAB seemed like a good choice at the time. The plan was to use the CNAB tooling to replay the Receipt if we needed to reproduce an action. That didn't go as planned.

Limit message size. At the time the default message size for Kafka out of the box was 1mb. We had a dev learning the system trigger his watcher on the same action as the watchers gate so it basically fork bombed itself into oblivion. We ended up with a 97mb receipt. We then decided to limit receipt size to 1mb and move large data to some other appropriate storage. Then we add the URI to the data in the receipt.

Make sure you sanitize the inputs. In the first month we had a dev try to base64 encode a binary into a receipt... give a dev a database and they try to make it into a blob store. CI/CD is very much a "garbage in garbage out" paradigm. Make sure your inputs
  are as good as your output.

If you give the devs a box of legos it doesn't mean they are going to build something cool.

You would think that a watcher would have a single gate to post to but what we found was that we needed a start gate and an end gate wrapped in a stage. It let us find where something died.



Write READMEs for every tool in the chain along with all of the examples.

Keep your documentation up to date.

Organize your documentation using a system like diataxis.

When in doubt codify your instructions. A binary or script that asks the user
  questions and creates the things they need can be very helpful.

Do not turn debugging on in Production. Rework your logging to let info
  statements tell you all you need to know.
  


The learning curve on decentralized systems is high and not as easy to roll
  out as we had hoped. Think about on-boarding when you are designing the system. It needs to be simpler and easier to implement.


## Things I wish I had done

So a couple other things
that I wish I had done so.Cryptographically signed the
receipts.We cryptographically signed the
receipts, then I would be almost done with my salsa.Uh, provenance.I wish we could build an RBAC
service for the complete pipeline, not just the event
driven system, and that would allow me to allow certain
accounts to be able to talk to certain services and then also I
would be all the user with my event driven. Wouldn't you know, been driven
system stuff?Umm. Observability. Yeah, I wish
I had thought of that in the beginning and done something to
make that better.So one of the things that just
continued to buy this.We did go from sometimes taking.It would take a week to get a a
new version to a customer to 8hours so.Yeah, there was a lot of
performance increases in the old pipeline without.Without having to rebuild the

## CD Foundation

Some stuff that I'm involved in
that I think you guys would be interested in if you want to
come talk about this stuff, I'mI'm. I'm working with the CDC
foundation.We've got the CD events, which
is a common spec for continuous delivery events. 5 to had this
back when I started this project, I would have used it
instead of cnab. But you know, I'm working on
this in the SIG events and I'm working in the SIG software
supply chain and we would love to have you come out and talk to
us.There's a public calendars and
all kinds of cool stuff.

I'm Smitty, and I'm afraid of robots.

Thank you.

Questions.
