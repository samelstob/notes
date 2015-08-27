Manage It! - Notes
==================

# Chapter 1: Starting a project

Project manager:

The person whose job it is to articulate and communicate what 'done' means and
to guide the project team to done.  By 'done', I mean a product that meets the
needs of the organization developing the product and the customers who will
use the product.

## 1.2 Manage Your Drivers, Constraints, and Floats

* What's driving the project?
* Are there constraints on the project?
* Can you trade off any of the drivers and constraints or buy yourself some
  more degrees of freedom?

The iron triangle is too simplistic.  Successful project managers trade off
many more factors than what's in the iron triangle.

* First write down your customer's expectations - what's driving the project
  from your customers' perspective.
    - What they expect (feature set)
    - When (time to release)
    - How good (defect levels)

* Next write down the constraints you are under
    - Environment
    - Processes
    - Who do you have and what can they do
    - How much money do you have

* Driver
    Look at expectations and constraints.  What jumps out at you as being required
    for your project's success?
* Constraints
    * Which of the remaining items will you need to manage to make the project
      successful?
    * Create a hierarchy with these concerns being a little less critical than
      the driver
    * Choose 2 or 3
* Floats
    - Remaining items
    - Important to the project, but you have flexibility to manage them
    - 3 of them

Go back and do some juggling

"I've seen projects with up to three constraints succeed, but only with
extraordinary effort on the part of the project team.  In my experience, if
you have one driver, two constraints, and three floats, you have a reasonable
chance of success.  The more floats you have, the easier it is to organize the
project."

## Decide on a Driver for Your Project

Early in the project, everything seems possible, especially if no one has
tried to estimate anything.

Don't say OK.  More likely, it's not possible to do everything your sponsor
wants in the time, for the money, with the people, and at the quality they
desire, given your work environment.  In that case, your sponsor needs to make
some hard decisions.

If sponsors don't decide, they push that decision down to the project manager.
If the PM doesn't decide, the team members will decide - and they will all
work to a different driver.

## Ranked list of possible drivers

Project priorities Rank
Cost to release     5
Release date        1
Feature set         2
Low defects         3
People              4
Work enviornment    6

In this project, the release date was the primary driver.  If we had missed
the release date this year, we would have lost all the value of the project.

## Context-Free Questions to Identify Project Drivers

High-level questions that help elicit other people's implicit assumptions
about the project.

* What does success look like?
* Why are these results desirable?
* What is the solution worth to you?
* What problems does this system solve?
* What problems could this system create?

* Why questions
    - The fewer "why" questions, the more you're learning about the business
      needs (and the less you sound like an obnoxious two-year-old)
    - Why questions are more likely to put the other person on the defensive
* How questions
    - Avoid "how" questions.  These sound like you're asking the sponsor to
      design the system.

Ask these questions out of a genuine desire to know about the project, not to
put anyone on the defensive.  You can use these questions to lay the
groundwork for a useful collaboration with your sponsor, not a difficult
relationship.

## 1.6 Project Charter

A project charter identifies the project drivers and constraints, and it helps
a project manager decide how to design the project.

* Vision
* Drivers
* Goals
* Success Criteria
* ROI estimate

### Who Writes the Project Charter?

Involve as many of the team members as possible in writing the charter.

### Vision

If you can't articulate the vision, chances are good that you're starting on
an impossible project.

### Success Criteria

Success criteria are things that define what the customers will be able to do
with the product when you are done.

e.g. Include features 1, 2, and 3 so we can sell to that specific market.

## Know What Quality Means for Your Project

Understanding the project drivers, constraints, and floats is the first step
to understanding what quality means to your sponsors and customers.

* The sponsors are the people who are paying for the product
* The customers are the people who will use the product.

## Remember This

* Start every project with a charter
* Expect to iterate on the project charter.  The charter doesn't have to be
  perfect; it just has to exist to help the entire project team with their
planning.
* Know what quality means and what's driving your project so you and the team
  can make good decisions as you proceed.

# Chapter 2: Planning the Project

## Plan Just Enough to Start

* Your plan does not have to be perfect.  In fact, there's no way it can be.
  Your plan only has to be good enough to start the project with a chance of
success.

### Timebox

* A timebox is a specific amount of time in which the person or team attempt to
  accomplish a specific task.  As much as the person or the team can
accomplish in that duration is what you bring to the next part of the project.
If necessary, the person/team decreases the scope to complete the timebox.

* Empirical planning - planning just a little and then gather information on
  actual progress to feed back into future planning

* Predictive planning, which is attempting to predict the future, doesn't work
  well unless you have a crystal ball

* Your projects have too much uncertainty and risk to bother planning
  everything in advance.  Plan to start and replan every few weeks.

* No matter what life cycle you use, assume you'll be replanning.  Don't
  create a perfect plan; create one that works until you replace it (soon).

* Tip: Start with the End in Mind - If you want to reduce planning time, make
  sure you have release criteria and a risk list.

"Plans are worthless, but planning is everything."

## Develop a Project Plan Template

* Product purpose
* History
* Release criteria
* Goals
* Project organization
* Schedule overview
* Project staffing (staffing curve)
* Proposed schedule
* Risk list

### History

The history can clarify any known technical debt.  The data you can review is
as follows: frequency of releases, number of released defects,
customer-reported problems

Tip: The less you know about any part of your project, the more likely you are
to be surprised.  This applies to technical debt, a new architecture, a
development or testing risk, or planning.  Anytime you don't have previous
experience with a project like this, the more surprises you'll encounter.

### Release Criteria

* "If we don't do that, do we still have a release?"

### Schedule Overview

* If you think the schedule is at risk before you even start, consider
  offering several alternatives for the project so your sponsors can see their
choices.
* Make sure you understand the value, not just the cost of each alternative.

### Project Staffing

* If you need to request people from other groups or teams, this is the place
  to explain how many of which people you'll need when.

### Proposed Schedule

* Outlinethe major milestones, as much as you understand them.

* I tend to schedule with yellow stickies, so I rarely have a full Gantt chart
  for my projects.  I've been known to say, "See the wall in the project room
for the most current WBS."

* Tip: Beware of Early Detailed Schedules: Iterate on your schedules, building
  detail as you proceed.  The earlier in the project you provide a detailed
schedule to your sponsors, the more likely they are to think that there is
little or no risk in your project.  They will see the projected end date and
believe it's the Real End Date for your project.

### Develop a Project Risk List

* Keep at least the top-ten risks in your project plan.  Monitor them
frequently, and update the list when appropriate.

* It's never too early to start identifying and managing risks.

### Define Release Criteria

# Chapter 3 - Using Life Cycles to Design Your Project

* When you organize the overall project, don't idealize your situation.  If
  you've seen issues such as incomplete requirements in your projects before,
don't plan for complete requirements up front this time.

* You'll need to figure out which risks are most important to your customer:
    - Date
    - Defects
    - Features
    - Cost
* Choose a life cycle that optimizes for those risks

* There are four main life cycles to choose from:

** Serial (a.k.a waterfall)
** Iterative
** Incremental
** Iterative and Incremental (Agile)

* Never use "code and fix" as your life cycle. "You guys start coding; I'll
  get the requirements"

## 3.3 Seeing Feedback in the Project

* The first time developers receive feedback on their code is during some test
  of that code.  If testing has not been integrated into the project that
feedback arrives very late in the project.

* If you just look at a Gantt-like picture of the agile life cycles, you can't
  see the feedback loop the agile life cycle provides.  This constant feedback
to the developers and the project manager is at the heart of why the agile
life cycles work.

# Chapter 4: Scheduling the Project

Planning and scheduling are two separate activities.

## 4.1 Pragmatic Approaches to Project Scheduling

You need to schedule enough to start the project.  There's no point scheduling
the whole darn project when you know the project is going to evolve.

If you're working with a customer who wants to see a project schedule before
they will sign a contract, be clear that the initial schedule is your best
first guess.

Projects require both plans and schedules.

You might not need a fancy schmancy Gantt chart for a schedule; yellow sticikes on the wall are fine for many projects.  But you do need to both plan and schedule.

Your schedule will bear some resemblance to the life cycle you choose.
Remember a life cycle is a *model* of how the porject could look.  Remember
that a life cycle is a guide, not a straight jacket.

Scheduling and estimating are two different activities.

a) Scheduling - ordering and showing the interdependencies of tasks
b) Estimating - guessing how many effort-hours a particular task will take

They are linked, because how you organize the schedule might depend on a given
task's estimate of the effort-hours and specific people required.

We generatlly need to estimate things we've never done before.  Estimation of
the unknown is still an art.  On the other hand, if you know what life cycle
you're using, organizing the schedule is easier.

## 4.2 Scheduling Techniques

### Top-Down Scheduling

Top-down scheduling generally starts with milestones.

Organise the project schedule into phases, iterations, or chunks.  ay them out
on a whiteboard or card + string or sticikes

The team starts organising the schedule from the highest-level mielstones and
develops the tasks to support those milestones.  As team members understand
more about what each milestone means, they breka the milestone down into its
component tasks.

The smaller the task at the bottom level , the eaier it is to estimate how
long the task will take.

### Bottom-up scheduling

Bottom-up scheduling starts with specific tasks.  If you're using an
incremental life cycle, it might make sense to start with bottom-up
scheduling.

THe project team devlop the milestones from the tasks.

### Inside-out Scheduling

Mind-map everything you know about the project.

### Hudson Bay Start

"The Hudson Bay Start approach was originated by the Hudson Bay Company in the
1600-1700s in northeastern Canada.  The Hudson Bay Company outfitted fur
traders.  To make sure the traders hadn't forgotten anything they needed, they
left Hudson Bay and camped just a few miles away.  By making camp just a few
miles away, the traders ensured they hadn't forgotten any tools or supplies -
before they abandoned civilization.  With just a short start to their journey,
they had a better idea about their ability to endure the winter."

A Hudson Bay Start is a technique that allows the project to team to push
something through the project's environment.  You want this to be as small a
thing as possible.  The idea is for the project team to see what it would be
like to start working in this environment with this product domain.

If you and the team can't figure out what it would take to estimate any piece,
timebox a Hudson Bay Start.  Start something you can complete in four hours or
less (this doesn't have to be real functionality).  If the team knows only a
little more, start with a short iteration, and then decide what to do.

* Team gains confidence they can accomplish something.
* Team has a little insight into how to organise some tasks

### Start with a Short Iteration

Use a short timeboxed iteration when the team understands the environment but
isn't sure how to esetimate the tasks.  A short iteration helps people see how
much they can accomplish in one or two weeks, so their follow-on estimates are
more accurate.

Combine it with a short retrospective.  By the end of the iteration, the team and you will have a better idea about
the requirements, the risks, and what they dont' know.

## 4.3 Scheduling with a Low-Tech Tool

Yellow-stickies.

It's easy to write a task on a sticky, put the sticky up on the wall, and
discuss with the rest of the project team - sometimes quite loudly - the
sequence of tasks or who will do them or what the risks are.

Yellow stickies involve the whole team in scheduling.  The team will explain
the risk as they proceed, providing you with valuable information you can use
for steering the project.

A tool says to the team, "I'm in charge of the schedule, you're not"

* Ask everyone to write all their tasks down on a sticky, one task per
sticky.
* As the team members write tasks, they post them on the wall.
* Assign one part of the wall as the parking lot - the place where the team
  will collect questions and assumptions you'll need to resolve as part of the
scheduling.
* Stand back, out of the way.  The project team members will start
  collaborating about the sequence of events, any prequisites, assumptions,
and questions.

## Benefits of Using Sticky Scheduling

* No simplisitic critical path line.  It will change daily or weekly so not having it will make people manage it.
* Yellow-sticky schedule will not show you the end date.  That's good because
  you should never estimate a single-point end date.  Because a scheduling
tool does calacuate the end date, people - especially senior management -
believe that end date.

## Deliverable based planning

If you've ever worked on a project that had a milestone such as "requirements
freeze" or "code freeze", you've worked on a phase-planned project.

The problem is that although those people try hard to complete their
deliverables, the freezes are rarely frozen, and the completes are mostly
incomplete.  You end up with slushy milestones.

## Remember this

* Schedule by deliverables, not by functions (phases).

* Plan to iterate the schedule.  A write-once schedule is not worth the time
  you spent generating it.


# Chapter 5 - Estimating the Work

## Separate Sizing and Duration During Estimation

People are not good at estimating tasks they've never done before.  How could
they be?

Sizing - how big the task is.

Cohn suggests using a Fibonacci series to generate a gross estimate for a
task.  A task is of size 1, 2, 3, 5, 8, 13, 21, 34, 55, 89.

1-2 days, 3-4 days
1-2 weeks, 3-4 weeks
1-2 months, 3-4 months

## Planning Poker

You want everyone on the team involved in estimating.

Don't take the average; ask the person to explain their concerns.

### Should We Estimate in Person-Hours or Person-Days?

* Person-Days assumes more hours in a day than you actually have setting you
  up for estimation failure

### Use a Spike to Gather Data Before Estimating

### Tips to Make Estimation Easier

* Remember that an estimate is a "guess".  The bigger the guess, the more
  error you will have.  If you provide an estimation of completion "date" make
sure your audience understands it is a guess.

* Many software people are optimistic.  This will persist unless they learn
  to estimate small pieces and receive feedback on their estimation.

* Tasks will take longer than you think they will.

* It's easier to estimate smaller chunks of work.

* Plan to iterate on the estimates.

* If you've been given a project deadline, you don't need to estimate anything
  at all (or just perform a gross estimation).  deliver the features and implement by priority.

* Timebox phases and tasks if you have an overconstrained project.

* Consider a spike if the task is too big (too much technical risk) to
  estimate well.

### Tip: Use Deliverable-Based Planning for Tasks



### Tip: Schedule Milestones (or Iterations) Midweek

* If an iteration is supposed to end on a Friday afternoon, but the product
  demo isn't until Monday morning, the team will often think, "Oh, we can
finish/fix this one thing over the weekend."  You want to know what the team
can do in a reasonable amount of time - not overtime.

Choose Tuesdays or Wednesdays for major milestones or for beginning/ending
iterations.

## 5.3 How Little Can You Do?

How-little thinking carries these assumptions:

* Understanding the requirements is a scarce resource.  We should focus our
  energies on delivering something that shows we understand the specific
requirement and the value it has to our customer.
* Schedule is critical, and we don't have time to do it again or build
  technical debt.
* Project cost is important, and we need to manage it.

## 5.4 Estimating with Multitasking

* Multitasking can waste anwhere from 20-90% of your time.  In my work,
  multitasking is the single biggest contributor to late projects, projects
that don't deliver what they need and project that don't work as well as they
need to work.

* What you can do is talk to your sponsors.  Explain, "If I don't have the
  people I need at the time I need them, I can't deliver what you want, in
the time you want it, with the quality you want."

## 5.5 

# Chapter 6: Recognizing and avoiding schedule games

## 6.1 Bring Me a Rock

The date you bring is not good enough.  "They" want it faster but don't tell
you when or why.

* Ask some questions: Would you prefer a short schedule or a longer one?  More
  people or fewer?  How about fewer features?
* Discover the reasons for the desired date.  Elicit the strategic reasons for
  this project, and learn what success means.
* Include release criteria with your date.  What if we implemented this
  feature with incredible performance, and ignore that feature?  Can our users
live with more defects?

## 6.2 Hope is Our Most Important Strategy

Hope is not enough to deliver a successful project.

* Recognize and write down where you have risks.  You might have technical
  risks (new language, new platform), schedule risks (shorter schedule, too
few people), or most likely, both.

* Choose any life cycle other than waterfall.  Why?  Because you don't have
  any data that would allow you to be successful with the upfront planning
that waterfall requires.  If you've never done anything like this before,
iterate on some prototypes, or iterate on a few features, to see where your
work takes you.

* Consider a Hudson Bay Start to see whether you can create anything.  This is
  especially good when you have a new technology such as a language, OS,
database, and the like.

* Make sure tha people have the technical functional skills and solution-space
  domain experise.  If necessary, train people.  It's cheaper to train
everyone on the project in a new language than waste time.

* Plan to iterate on everything, especially planning and scheduling.

* solicit help and information in areas wher eyou might lack experience.

* Develop milestone criteria and review those critera at management review
  meetings.  Even if management or your sponsors don't want management
reviews, you can conduct those meetings.  Reviewing your progress regularly
against milestones will help if you aren't sure how to make this project work.

## 6.3 Queen of Denial

* Us: We can't meet your schedule Them: "I'm sure if you put your mind to it,
  you'll meet the date"
* Denial:
  - Manager wants to encourage the project - believe that when they set
    ambitious/impossible dates, the project team will deliver sooner than they
thought they could
  - Fear - ostrich effect

Some possibilities:
  * Investigate why your manager is in denial.  Try some context-free
    questions e.g. For this project, what does success look like?
  * Write down your projects risks and their potential impact.  Use High, Medium, and Low not numbers (to reduce gaming)
  * Show what you can do and measure the velocity
  * Make sure people on the project have the domain expertise

When the manager does see reality, make sure you have some part of the product
working and some data to show that manager so you can discuss what to do next.
This is a good time consider how little can you do.

* Use timeboxed iterations, so you and everyone else can see project progress.
* Develop a ranked backlog that will allow the team to implement by feature in
  value order.

## 6.5 Happy Date

* Implicit agreement *not* to discuss the schedule.  Milestones, and dates are
  missed initially without discussion.

* "I certainly have seen persuasive managers intimidate, cajole, or use
  political pressure to "convince" a project manager or team that they could
meet the Happy Date - the date the manager wants.  Combine that with a culture
of not discussing difficult topics, and you're ripe for the Dream Time/Happy
Date schedule game"

* Happy Date is related to, but not the same as, Queen of Denial - In Happy
  Date both sets of people are in denial about the need to talk about the
schedule.

To prevent this schedule game:
* Explain schedule ranges, especially if you're not using an iterative life
  cycle.
* Use an iterative lifecycle and confidence ranges: "We can do these ten
  features and maybe these other three in the next month.  We'll let you know
before the end of the month"
* Use can agile life cycle with a ranked product backlog
* Use short timeboxes, even in a staged-delivery life cycle, to help people
  make progress, and make that progres visible.

Constructive discussion (a.k.a constructive conflict) can make an organization
stronger.  Avoid conflict and the necessary discussions makes an organization
weaker.

# 6.8 Schedule Equals Commitment

* A reasonable schedule discussion requires discussing the rest of the project
  dirvers, constraints, and flo90ats: at a minimum the feature set desired in
that time and how good the feature set will be at that time.




# Chapter 7: Creating a Great Project Team

* Diversity of experience, personality, and role will help the project team
  identify risks faster, which allows you to manage the risks better.  The
riskier your project is, the more diverse a team you need.

* The best way I know to help teams jell is to have them work together - and
  not on rope courses or laser tag.
    - When people have a common goal, make commitments to each other about
      their interdependent tasks, and use an agreed-upon approach to the work,
they are part of a team.
    - If you want your team to jell, help them determine some short-term goals
      that they can accomplish only together.

* The most efficient organisation for project completion is the projet based
  organisation.  Functional team (e.g. dev, test) and matrixed are harder.

## Responsibility and authority

* No manager ever has enough real authority to do what he or she wants to do.
  There's always someone with a bigger title (even a CEO reports to the
board).

* If the project is trategically important to the organisation, act first
  (doing whatever the project needs), and ask forgiveness later.  You'll know
whether the project is strategically important by how many people ask about
the status and what levels of people ask.

* If the project is important enough to the organisation, you have the
  authority to do just about anything you need to do.  If the project is not
important enough to the organisation, you can never get enough authority to do
what you need to do.  Go to the project portfolio and work on a strategically
important project.

* Build relationships to lay the foundation for influence across the
  organisation before you need it.

    
# Chapter 8: Steering the Project



# Chapter 9: Maintaining Project Rhythm


## CI

If you're managing a project that is supposed to release on multiple
computers, databases, or firmware, make sure your team always compiles and
builds for all platforms every day.

## Implement by Feature, Not by Architecture

Get complete things done.

## Implement the Highest-Value Features First

When implementing by feature, implement the most valuable features first.
Leave the riskiest features until later.  If you're lucky, you won't have to
do them.  If you do, the developers and testers know much more about the
entire system, so they will be able to maintain their rhythm.

## Debugging by Feature, Testing by Feature

Testers test the system by feature.  When testerse report problems, they
rarely report against small architectural components in isolation.

Developers are accustomted to taking problem reports and backtracking to
determine how the feature interacts with the architecture to understand the
problem.  Implementing by feature helps the developer see these potential
problems as the developer designs and writes the code, not wait until the end
of deelopment to see them.

## Get Multiple Sets of Eyes on Work Products



# Chapter 11: Creating and Using a Project Dashboard

Creating a project dashboard provides feedback to the team and reports status
to other interested people.  Use a Big Visible Chart of Information Radiator
so that everyone can see the project's progress.

## 11.1 Measurements Can Be Dangerous

Measurement involves three big problems:

* The project team spending too much time on measurement to the detriment of
  the work
* Gaming the system
* Measuring the people instead of the project

Measuring people begs them to game the system.

### Velocity Charts

* Total Features
* Features Left
* Features Done

### Iteration Chart

Use an iteration contents chart to track overall progress

e.g. 

* Defects
* Changes
* Features

## More Measurements

* Schedule estimates and actuals
* When people (with the appropriate capabilities) are assigned to the project
  vs when they are needed
* Requirements changes throughout the project.  If you use velocity charts,
  you get this as part of velocity
* Cost to fix a defect throughout the project
* Defect find/close/remaining open rates throughout the project

## Fault feedback Ratio

Number of rejected fixes (that don't actually fix the problem) to the number of fixes

"When you fix something here, does a problem pop up over there?"

# Defect charts

* New defects found per week
* Closed defects per week
* Remaining open defects per week

I specifically do not chart defects by priority because the senior management
become too willing to play the promotion/demotion game.  Besides, the
developers have to read through all the defects, even if they are supposedly a
lower priority.

## User a Project Weather Report

* Weather reports can provide more granularity than traffic lights
* Many project managers feel pressured to game the traffic light.

## Remember This

* Data is a tool for your use, not an end in itself.  Remember, the charts
  should serve you.
* If you can't acquire data you think you need, you have a bigger problem than
  the data.  Fix that problem first.

# Chapter 13: Integrating Testing into the Project

* Because each project is unique, you'll need to think about the testing
  required.  Use your project's risks to decide what kinds of testing you
need.

* You the project manager should initiate the planning for testing.  If you
  don't plan to integrate testing into the development, it won't happen.
You'll end up with testing as a separate set of project tasks, tasks that
start later, take longer, and turn whatever life cycle you have into a serial
life cycle.

* First day on a new project, if they have nothing to do, then get people
  fixing defects on a previous release as a way to learn what temptations to
avoid in this project.

## TDD

* TDD is more about design than it is about testing

* Developers write code, but some of them forget they also write defects.

* Unit tests, developed either just before writing the code (TDD) or just
  after writing a few lines of code, are the cheapest way to find and fix
defects.

* If you can't depend on having dedicated testers and dedicating testing
  machines, test-driven development will dramatically reduce the testing risks
on your project.

* With TDD developers will be able to take advantage of symmetry in the code
  (which they will see when they refactor) and the evovling, emerging design.

* If you want to reduce risk, start with TDD on the highest risk areas.  If
  you want to increase value, start with TDD on the highest value areas.

* Ask for one or more volunteers if it's tricky to introduce in one go.

### Unit Testing is Not a Panacea

* Unit tests need to be of good quality to have value

### 13.4 Use a Wide Vaeriety of Testing Techniques

* If you have a system with a substantial GUI, you will need system testing.
  If you want to reduce overall technical risk, you'll need system testing.

### Can Your Testers Do the Job?

* Testing a complex system is just as difficult as creating one.

* Are your testers second class?

* Are you testers routinely excluded from requirements or design meetings?

* Do your tests resort to eavesdropping to hear information about the product?

* Are you testers requests for tools postponed or ignored?

* Are product testability requirements postponed or ignored?

* Is the testers per-person training budget significantly less than the
  developers budget?

* Are all your tests interchangeable, i.e. they have similar skills it doesn't
  matter who works on what projects?

* Do testers work with developers on the code only after the product is built?

First-class testers are sufficiently creative to assess the design and
architecture of the system before the code is written.  While the code is
under construction, first-class testers design and implement their testing
harnesses, both automated and manual, creating tests that stress the system in
ways the developers do not expect.

First-class testers can measure what they've tested, assess the risk of what
they've tested, and know whether they've tested enough of the system to help
you understand the risks of product release.

First-class testers have a peer relationship with developers.  They work as
partners, not as adversaries.  Great testers alter the way developers create
the product.

# Chapter 16: Managing the Project Portfolio

