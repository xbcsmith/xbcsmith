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

We can shift left and do things earlier in the software lifecycle. We can build
event driven robots to enforce compliance, scan environments, verify binaries,
and remove out-of-band human checks. However, compliance does not equal
security. Closing the attack vectors should be priority #1. And while monitoring
is necessary verification is more important. The verification of environments,
materials, processes, and artifacts before running actions in our pipelines
increase security. In this sense verification is greater than monitoring

