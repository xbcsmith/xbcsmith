# Continuous Talent Development

## Introduction

Everything in devOps is continuous these days. We have the classics like
Continuous Integration, Continuous Testing, Continuous Delivery, and Continuous
Deployments. We have new ones like Continuous Learning. Continuous Learning is
the only way to survive in a modern devOps shop. While continuous learning is
great for the individual it does not help with replacing talent on the team when
a member moves on to another team or leaves the company. It seems Continuous
Turnover will become a thing at some point in the near future. With the rise
Continuous Turnover there will be a need for Continuous Talent Development.
Continuously developing new talent is the only way your team can survive
developer turnover and the great resignation. The two streams for replacing
talent we will focus on is interns and new junior team members. We will cover
the procedures the team has done to successfully on- board and
transition new team members and interns into major contributors in a short
amount of time.

## Documentation

The best answer is document everything. If you are asked a question twice
document the answer. Established teams tend to neglect documenting things
because everyone on the team knows how it works. That is called tribal knowledge
and it is hard to convey to new team members.

Tribal Knowledge must be shared. Take time to write down your teams tribal
knowledge. New team members benefit from not guessing how things work or where
things are. If the team is in a time crunch have the new team member crowd
source the tribal knowledge. One way to do this is to throw a question into the
group chat and ask for responses. It doesn't have to be full sentences just the
facts. Then you have source for the documentation and didn't have to search for
the answers.

### Developer Environment

On-boarding doc to create a development environment takes a lot of the guess
work out of getting setup and contributing. The new team members are handed the
on-boarding doc and a place to set it up (usually a VM or Container). We
specifically give new team members their own development environment to manage.
It allows them to develop without the risk of messing someone else's development
environment up. It teaches them how to install and maintain the development
tools. For example, when we update the tools in the pre-commit hooks or the
version of go it is the responsibility of each team member to update their
development environment. Lastly, having their own development environment gives
them the same standing as existing team members.

### The Project

Share written references explaining what the project is, what it does, and what
its purpose is in the ecosystem. Explaining the project in a meeting is nice,
but having documentation to reference is very helpful for understanding the
project.

Every repository in the project should have a README next to the source
detailing how to build, use, and deploy the software. The README should also
include examples for all the above.

Keep your documentation up to date. And a good way to teach and update doc is to
have the new team members go through it and update anything that is wrong,
outdated, or typos. Use the new team members to improve the documentation.
Sometimes veteran team members in take for granted we all know how it works when
writing the documentation. Use the new team members to fill in and clarify
sections of the doc that are glossed over.

### Reference Material

Share your reference material with new team members. Links to helpful sites,
articles, tutorials, industry specifications, tools, and repositories are always
helpful. Encourage using "google", using
[O'Reilly online](https://www.oreilly.com/) (free to employees), continuous
learning, and other reference material you use to consistently get better.

## Meaningful Work

Assign new team members meaningful work.

When we say assign meaningful work, we mean specifically not worthless work.
Meaningful work gives new team members purpose and a connection to the team.
Interns in particular benefit from having a reason to be diligent in double and
triple checking their work.

### Assign Small

Start out with small tasks that can be completed in small time boxes. Work up to
more complex problems and tasks. Use linear increases in cognitive complexity of
assigned tasks. Don't assign mission critical or large tasks right away.
Gradually increase the size and complexity based on the individual's progress.
We are spoon feeding kittens not tossing steaks to lions. Be patient. Apply
leniency in achieving understanding of new topics. Not everyone is going to get
it right away. Explain the "big picture" and "why" of the assignment as it helps
with understanding.

For example, when we started with our new interns, we broke up some of our "nice
to have" tickets into smaller pieces that could be finished with relative ease.
We assigned these to the interns and mentored them as they worked. As they
completed them and their confidence and knowledge grew we assigned more normal
sized tasks that were slightly less defined. Over time the new team members and
interns were fully acclimated and work on regular issues with the rest of us.

### Breaking Things

If you are not breaking things, you are not doing anything. New team members are
encouraged to jump in and start working right away with no fear as it is ok to
break things. We have continuous integration that will catch most breakage
before it is even committed to the repository. Even if it does get committed to
the repository fixing it is usually easier than reverting the changes. Always
move forward. Continuous Testing and Continuous Deployments ensure that our
development and test environments are working. Most times the fix is a single
git commit away. Once the fix is in the automation corrects the environments.
Don't worry it will be OK.

### Variety

Variety of tasks, builds a varied skill set. Assign new team members a variety
of tasks. They should work on code cleanup, documentation, writing tests,
continuous integration, and continuous deployments along with writing code and
adding features. BY not doing the same thing the whole time, they get used to
swapping and learning topics. The diversity in the skill set will pay off for
the team and the new member before you know it.

### Explaining Decisions

During planning sessions and meetings make sure to explain your decisions. If it
is not time appropriate make sure to circle back and explain the decisions in a
smaller group or individually. Explaining the decision and the thought process
that went into it is invaluable to junior team members. Everyone benefits from
the explanation when the team makes decisions based on experience that go
outside what would be a normal solution. It also gives the new team members a
chance to ask questions about things that might not be obvious about the
decision.

### Digging Ditches

There are no fun tickets. The fun tickets are so few and far between that they
don't get sprinkled across the team. They are coveted. They are handed out like
golden tickets. Most of the time I refer to the grueling tasks as "digging
ditches". It is not fun, but the work must get done. Early tasks assigned to new
team members are "nice to have". Assigning "nice to have" work benefits the team
and the new team members. The team finally gets the feature that no one had time
to work on. The new team member gets to get their feet wet on something that is
probably more fun than mainline tasks. Once the new team members are ramped up
enough to do harder work they can dig ditches with the rest of us.

## Teach

When someone is new to the team every interaction becomes a teaching moment.

### Mentor

New members of the team should be paired with a mentor. Someone that knows how
things work and knows where to get answers if they do not. For interns this
should be a senior member of the team that will not lead them astray. We only do
one mentor and one mentee because of the amount of time it takes to properly
guide young talent.

### Availability

Being available for the new team members is very important. If we are
encouraging them to not get stuck and ask questions sooner we need to be there
to answer those questions.

Availability means accessibility. As interns and new team members go about
day-to-day work, they should feel like it is OK to ask questions at any time. We
use the chat clients a lot as it is easier to balance getting the work done and
answering smaller questions along the way. We will call the individual if the
answer is going to be very long or depend on lots of other factors.

### Best Practices

The team should be doing their due diligence around the process. Following
industry standard practices, adhering to specifications, and basically trying
their best to do things the right way. New team members should follow these
practices. The best way to convince new team members to follow the practices is
to explain why and how they came about.

Teaching best practices for the team to interns and new members is invaluable.
It is hard to unlearn bad habits. Interns have usually not formed opinions on
the best way to handle tasks, projects, or technical decisions. They learn best
practices from the team and their mentors.

### Subject Experts

One way to become an expert on a subject is to teach the subject. You may do
something every day that is complicated and a bit tricky, but you are used to
doing it so it seems easy. Try explaining it to someone who has never seen it
before. As you describe this thing the outside interactions need to be
explained. They can also seem foreign. Explaining everything usually leads to
losing the audience to a sea of head nods with almost no retention. If you can
highlight the important pieces and key take always you will have more success.
This is sometimes called an elevator pitch. Learning to explain them in an
elevator pitch takes practice and a deep understanding of what you are trying to
explain.

Assign new team members a part of the project they can become subject experts on
and have them present the subject to the team. Interns are no exception here. Do
not worry if you already have a subject expert for the thing on the team. There
can never have too many subject experts on a team and it gives new team members
someone to mentor under.

### Timebox

Teach the new team members to timebox features and fixes. Encourage them too not
spend too much time struggling to solve a problem before asking for help. As an
example, we use 15 - 30 minutes for small problems and 4 hours as a max for
larger problems.

### Don't Micromanage

After initial on-boarding and the new team members are up to speed let them
figure out their own way to work. Every developer has their own process, and
that's a good thing at the end of the day. It's important to let the new members
develop their own skills and techniques. Micromanaging annoys the mentee, is
counterproductive, and get in the way of the developers growth.

### Feedback

Check in with the new team members. Ask questions about how things are going? Do
you need help with anything? Are you getting everything you need from me? While
critiquing is a necessary part of the process of mentoring encouragement and
pointing our jobs well done are just as important. Constant negative feedback is
discouraging. A discouraged team member will be unlikely they will want to ask
for help when they need it. Critiquing with a positive spin is helpful. Make it
a point to comment when the new team members do things well.

### Tools

Teach and explain the tool sets. Explain why we have such heavy-handed linters
and autoformat code. Explain why the functional tests are so extensive. Take
time to teach skills like command line foo and how to make use of APIs.

## Integrate

### Get to Know the People

Let the new team members get to know you and other team members. It does not
need to be a life history just some lighter things like hobbies outside of work
and technical backgrounds. Familiarity with the team members will make the new
team members more comfortable asking questions. Encourage asking good questions.
Answer all the questions even the not so good ones, you can always take time to
explain the way to ask the question as part of the answer.

### Touch Base Meeting

I don't believe in daily scrums. Daily scrums are for Agile Zealots and
Managers. We do two scrums a week. Participants talk about what we
did the day before and what they are working on for the next two days. This way
managers are kept up to date and Developers are freed from daily scrums. We use
a large private group chat to communicate needs, work, and progress within the
team. We use the Microsoft Teams channels to communicate outside the team. Using
these methods we do not have to wait a whole day to ask our question or get the
help we need. Feedback is almost immediate, and developers get to work instead
of meet. New team members are encouraged to ask questions in the group chat and
channels rather than one to one. This spreads the knowledge across the team and
keeps your lead developers from answering the same questions multiple times on
multiple streams.

Interns are the only exception. They are in the team chat, but they should have
a conversation always open directly with their mentor. We do this so the mentor
can explain what is being discussed in the group and channels. Every moment
becomes a teaching moment. On the days we do not have scrum we have a 15 minute
"touch base" meeting with the new team members and interns. It gives us a chance
to talk about what they are doing that day in a smaller group. We make sure that
we explain the why in the what they are asked to do. And it gives them a chance
early in the day to get on track and get contributing. It is important the touch
base is informal compared to a scrum. Being comfortable allows the new team
members to be more forthright about what they might be struggling with.

### All the Meetings

Invite new team members, including interns, to all the meetings. They can feel
included and learn through osmosis. They gain a better idea of why we are making
certain technical choices. Understanding the big picture leads to better
decisions and more satisfaction from assignments. No task is too small, knowing
the tiny change they are making has a big impact on the project gives a better
sense of ownership and pride in the work.

### Part of the Team

Integration and interaction with more than just the mentors are important.
Interns especially should be part of the actual team, not sequestered off
somewhere doing meaningless projects. Have new team members participate in code
reviews from the start. Pair new team members with senior mentors. Give new team
members meaningful work. Make them part of the team.
