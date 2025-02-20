<!-- TOC -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [CFP - Call for Proposals](#cfp---call-for-proposals)
  - [About](#about)
    - [Title](#title)
    - [Bio](#bio)
    - [Previous Speaking Engagement Experience](#previous-speaking-engagement-experience)
    - [LinkedIn](#linkedin)
    - [Headshot](#headshot)
  - [DevOps Days Nashville](#devops-days-nashville)
    - [General Guidelines](#general-guidelines)
    - [Ignite Sessions](#ignite-sessions)
    - [Presentations](#presentations)
  - [DevOps Days Raleigh](#devops-days-raleigh)
  - [Lightning Talks](#lightning-talks)
    - [Event Driven CI/CT/CD Framework with an Audit Trail](#event-driven-cictcd-framework-with-an-audit-trail)
    - [Supply Chain Robots, Electric Sheep, and SLSA](#supply-chain-robots-electric-sheep-and-slsa)
  - [Presentation Proposals](#presentation-proposals)
    - [Event Driven Supply Chain Robots with an Audit Trail](#event-driven-supply-chain-robots-with-an-audit-trail)
    - [Continuous Talent Development](#continuous-talent-development)
    - [Supply Chain Robots, Electric Sheep, and SLSA](#supply-chain-robots-electric-sheep-and-slsa-1)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->
<!-- /TOC -->

# CFP - Call for Proposals

## About

### Title

Principal Software Developer at SAS

### Bio

Software Architect/Engineer/Developer with 20+ years of experience. Specialties:
Automation, Continuous Integration/Delivery/Testing/Deployment Expertise: Linux,
packaging, and tool design.

Currently Engineering and Securing the Supply Chain with Infrastructure as Code
(IaC) event driven CI/CD gitOps Pipeline Architectures that leverage Kafka, Go,
and Python running in Containers on Kubernetes.

### Previous Speaking Engagement Experience

SAS Internal DevOps Unconferences, Town Halls, and Demo Days CDF
sig-software-supply-chain meetings

### LinkedIn

https://www.linkedin.com/in/brett-smith-15b3737

### Headshot

https://github.com/xbcsmith/xbcsmith/blob/main/images/Headshot_Grey.jpg

## DevOps Days Nashville

<https://sessionize.com/nashvilledevopsdays2023>

### General Guidelines

Be concise, but include as much detail as is necessary to convey your idea.

Please provide at least two takeaways that the audience will get from your talk.

Multiple entries are welcome, but please limit to no more than four submissions
per submitter.

Submissions must be made by one of the proposed presenters; we do not accept
proposals submitted on behalf of others.

All presentations must conform to the code of conduct.

Proposals must be submitted via this CFP site.

If you have questions about our CFP process, please email:
[nashville@devopsdays.org]

### Ignite Sessions

An Ignite talks are 5 minutes talks with slides auto-advancing every 15 seconds
(20 slides total).

### Presentations

A 30-minute talk presented to the entire conference audience

## DevOps Days Raleigh

<https://devopsdays.org/events/2023-raleigh>

## Lightning Talks

### Event Driven CI/CT/CD Framework with an Audit Trail

A lightning talk I did at one of our internal unconferences to kick off the new
event driven CI/CT/CD framework I was designing to bolt onto and expand our
current pipeline. As part of the design there is an audit trail of receipts that
are used to track what was done and trigger events. The talk should lead to a
greater discussion around the how and why to go event driven. Listeners should
come away thinking about ways to gate releases by readiness, drive automated
testing, make their pipelines asynchronous, and use machine learning to make the
pipeline leaner and more reliable.

### Supply Chain Robots, Electric Sheep, and SLSA

A lightning talk focusing on securing the supply chain. In the talk I cover
creating automation, shifting left, attack vectors, attestations, verification,
zero-trust, and how the SLSA spec helps implement solutions for each. The main
take away is that security needs to be applied everywhere in the pipeline. The
talk should lead to a greater discussion around the challenges of securing the
supply chain, supporting EO 14028 and ISO27001, and improving the security
posture of your pipelines.

## Presentation Proposals

### Event Driven Supply Chain Robots with an Audit Trail

In this presentation I go over how we created our current event driven pipeline.
It covers why we decided to go event driven, were we started, where we are now,
and where we are headed. I talk about how we are leveraging several technologies
like Kafka, Go, Kubernetes to create a fully automated asynchronous supply chain
for delivering rpms, deb, and oci images to customers. I also cover how not
having time to build a new greenfield pipeline drove our technical decisions. I
cover our audit system, receipts, and gating system that lets the robots ship
the software by readiness. The lessons learned covers the triumphs and pitfalls
of event driven asynchronous CI/CD pipelines. Attendees will learn about ways to
gate releases by readiness, drive automated testing, make their pipelines
asynchronous, and use machine learning to make the pipeline leaner and more
reliable.

Attendee Takeaways

Answers for the following questions:
- Why go event driven?
- How do we gate releases by readiness?
- How do we drive automated testing?
- How do we make our pipelines asynchronous?
- How do we use machine learning to make the pipeline leaner and more reliable?

### Continuous Talent Development

A presentation on building and growing talent – whether it is interns, recent
graduates or new hires – to feel engaged, productive and ultimately make a
difference. A how-to for fighting the “The Great Resignation” and "Quiet
Quitting". I cover how my team made a change in how we handled new additions to
the team and creating an environment that retains talent. The presentation is
based on an article I wrote that is published on linkedin titled "Continuous
talent development: How to create connected, empowered and inspired employees"
<https://www.linkedin.com/pulse/continuous-talent-developmenthow-create-connected-empowered-smith>.
Attendees will learn methods they can employ on there team to help get new hires
up to speed, be more productive, get more satisfaction from their contributions,
and most importantly help retain the talent.

### Supply Chain Robots, Electric Sheep, and SLSA

A talk about creating automation, shifting left, attack vectors, attestations,
verification, zero-trust, and SLSA.

In the talk I cover creating automation, shifting left, attack vectors,
attestations, verification, zero-trust, and how the SLSA spec helps implement
solutions for each. The main take away is that security needs to be applied
everywhere in the pipeline. The talk should lead to a greater discussion around
the challenges of securing the supply chain, supporting EO 14028 and ISO27001,
and improving the security posture of your pipelines.


Attendee Takeaways

Answers for the following questions:

- Why do we need supply chain automation?
- What are common attack vectors in a supply chain?
- What techniques can we use to help secure the supply chain?
- What are the security benefits of supply chain automation and shift left?
- What specifications and tools can we use to help secure the supply chain?

### Reproducible Builds: Robots recreate Electric Sheep

A talk about the security benefits and challenges of reproducible builds. It includes a real world comparison of the Debian and Fedora build systems and a discussion on the value based on the effort. Listeners should come away with knowledge of what reproducible builds are and opinions on if they are worth the effort.

Attendee Takeaways

Answers for the following questions:
- What is a reproducible build?
- Why do we need reproducible builds?
- What are the security benefits of reproducible builds?
- What are the security challenges of reproducible builds?
- What is the value of reproducible builds?

30 minutes plus QA discussion. First presented at the NCSU Secure Software Supply Chain Community Day.
Presented at DevOps Con 2024 San Diego. 

### Secure the AI: Protect the Electric Sheep

In this session I go over how AI presents security risks to the Software Supply Chain, SDLC, developers, and architects. I cover attack vectors in the supply chain and how they relate to the the OWASP Top 10 for LLMs as well as how they tie into scenarios in your CI/CD pipelines. We wrap up the session covering techniques to close the attack vectors and protect your pipelines, software, and customers.

Attendee Takeaways

Answers for the following questions:
- Why do we need to secure the AI?
- How do we secure the AI?
- What is the OWASP Top 10 for LLMs?
- What are the AI attack vectors in the supply chain?
- How do we close the AI attack vectors?

### Wrangling Third Party Dependencies: Are the Electric Sheep Healthy?

A talk about how we are working on curating our Third Party Dependencies using automation and online resources like Ecosyste.ms, deps.dev, OpenSSF Scorecard as well as Snyk, Sonatype, and others. What libraries are we using? What libraries are unsupported, abandoned, outdated, etc...? What open source tools can we leverage to help answer these questions and more?

Attendee Takeaways

Answers for the following questions:
- Why do we need to curate Third Party Dependencies?
- How to find libraries are we using?
- What libraries are unsupported, abandoned, outdated, etc...?
- What open source tools can we leverage to help answer these questions and more?

### Wrangling Third Party Dependencies: Electric Sheep and JFrog

A talk about how we are working on curating our Third Party Dependencies using automation and JFrog products like Artifactory, Curation, Xray, and Advanced Security. What libraries are we using? What libraries are unsupported, abandoned, outdated, etc...? What open source tools can we leverage to help answer these questions and more?

Attendee Takeaways

Answers for the following questions:
- Why do we need to curate Third Party Dependencies?
- How to find libraries are we using?
- What libraries are unsupported, abandoned, outdated, etc...?
- What open source tools can we leverage to help answer these questions and more?
- What JFrog products can we leverage to help answer these questions?


### The workshop is how long? Using AI to create an all day workshop

In this session I tell the story of how AI saved me from a disaster. I agreed to do a workshop I was working on for a conference. I only had about 45 minutes worth of content but planned to have 90 minutes. I then found out after agreeing to do the workshop that the format 4 90 minute sessions (all day). I will talk about how I used AI to fill in content and tech tricks I used to pull it off from writing workshop content and generating slides to writing software to use in the workshop (Go and Python).

### Platform Engineering: Herding the Electric Sheep

A talk about platform engineering, DevOps, DevSecOps, sprawl, chaos, compliance, and security. Why engineer an Internal Developer Platform when I have DevOps? DevOps works fine when you are a 20 person start-up but it often doesn't scale to Enterprise level development efforts. When you have 3000 developers with different needs and you are responsible for EO compliance and security a modular self-service platform is a good choice to build. In this talk I cover the challenges we have faced in a 3000 developers enterprise and how we are working to address them. I also cover how we are working on automating, integration, and scaling the creation of our internal developer platform. We talk about the tools we are using and the good and bad decisions I have made along the way. I also talk about how we are leveraging SBOMs, SLSA, and other tools to help build out a secure and compliant platform.

Attendee Takeaways

Answers for the following questions:
- Do we need a Platform Engineering Team?
- Is an IDP the right solution for my situation?
- What does a large scale IDP look like?
- What does it take to support a large scale IDP?
- What does security and compliance look like in an IDP?

Attendees will learn the benefits and challenges of Platform Engineering

### Platform Engineering: Herding the Electric Sheep  and some Frogs

A talk about platform engineering, DevOps, DevSecOps, sprawl, chaos, bad decisions, compliance, and security. Why engineer an Internal Developer Platform when I have DevOps? DevOps works fine when you are a 20 person start-up but it often doesn't scale to Enterprise level development efforts. When you have 3000 developers with different needs and you are responsible for EO compliance and security a modular self-service platform is a good choice to build. In this talk I cover the challenges we have faced in a 3000 developers enterprise and how we are working to address them. I also cover how we are working on automating, integration, and scaling the creation of our internal developer platform. We talk about the tools we are using including JFrog products like Artifactory, Curation, Xray, and Advanced Security. I also talk about how we are leveraging SBOMs, SLSA, and other tools to help build out a secure and compliant platform.

Attendee Takeaways

Answers for the following questions:
- Do we need a Platform Engineering Team?
- Is an IDP the right solution for my situation?
- What does a large scale IDP look like?
- What does it take to support a large scale IDP?
- What does security and compliance look like in an IDP?
- What JFrog products can we leverage to help answer these questions?

Attendees will learn the benefits and challenges of Platform Engineering and how JFrog can help.


## Workshops

### Workshop: Building an Event-Driven CI/CD Provenance System

In this hands-on workshop participants will journey through the architecture of an Event-Driven CI/CD Provenance System. We will not only cover microservice architectures, but also asynchronous communication, data interoperability, message specifications, and schema validation.

We will learn how to leverage Golang for service and CLI development, Docker for seamless deployment, Redpanda as a Kafka-compatible message bus, and PostgreSQL for efficient backend storage. The workshop uses the open-source project Event Provenance Registry (EPR) as the central service to leverage these technologies.

Over the course of the session we will delve into the EPR codebase, work through coding and building Golang services, discuss the theories of event driven systems, cover some pitfalls, and examine the integration with Redpanda for effective event propagation.

The workshop provides a valuable blend of theoretical understanding and hands-on experience in the dynamic landscape of Event-Driven CI/CD architectures.

4 90 minute sessions for the full workshop. The workshop can be modified to fit a smaller time slot.

First public delivery at DevOpsCon San Diego 2024