# Event Driven Ci/CD Pipelines Ignite

Continuous Integration, Continuous Testing, Continuous Deployments, Continuous
Delivery... I am going to need an army of robots. And I hope they don't run
amuck

Hope is not a strategy. We cannot hope the robots do the right thing. We can not
hope the robots don't chase my
[electric sheep](https://en.wikipedia.org/wiki/Do_Androids_Dream_of_Electric_Sheep).
We need a strategy.

Why?

Because Continuous Delivery at scale is hard. Continuous anything at large companies is
going to be difficult. What do we do about this new world?

The future is automatic. Automation will not be enough. I need the developers to
check out code. Make their changes. Submit their pull requests.

Just Commit. And the robots do the work.

How can we accomplish this? I have a few ideas.

What if we create receipts for the actions we automate? What if receipts payloads follow a spec? What if the receipts have all the metadata collected from
the actions?

We create receipts for Builds, Unit tests, Component Test, System Integration,
Regression Tests, Staging. Everything gets a receipt. What do we do with all
these receipts?

We collect all the receipts. We tie them to gates. We collect,
validate and store the receipts. What do all these receipts do?

Receipts check the box. The box is the gate.

What if we use the receipts to satisfy gates and trigger the next
step of the pipeline? The receipts satisfy the gates. The gates enable flow through the pipeline.

The watchers are listening for events. We emit a message to the watchers. The
watcher hears the message it queries all the gates for the receipts. It
validates the gate is satisfied.

The robots promote the unit. We ship by readiness. This is my letter to
[Deckard](https://en.wikipedia.org/wiki/Rick_Deckard).

Automatic not just Automated. Because automation is not enough.

What value do we get from all the receipts and gates?

I can trace the lifecycle of source to a binary running in production. So, when
they find a bug I can trace how it got there. Once I trace how it got there...

I can reproduce the actions for the things the automation did with the
receipts...

We gathered all this data what do we do with it?

We use machine learning to Optimize. We make our tests better, we make our
deployments better, we make everything faster.

We do predictive test selection so when a Developer changes the README I don't
run six hours of regression tests. I run the README test.

We do Deployment Risk Prediction. Automation does 40,000 deployments a year.
10,000 of them fail. We use that data to flag source that is risky for
deployments and come up with another plan.

This is the event driven asynchronous pipeline. I like to refer to it is a
series of bad decisions wrapped in go.

I am Smitty. I am afraid of robots.


