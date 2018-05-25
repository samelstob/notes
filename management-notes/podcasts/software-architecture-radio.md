# Tudor Girba on Solving Problems Without

Software developers transform data problems into decision making problems

When developers have their own problem they fall back to the most basic means
- reading source code.  Trying to put it all in your head - it's in humane -
  like plowing the field with you bare hands.

When developers read code they want to understand enough to make a decision.
Instead of code reading I call it assessment.  No two systems have the exact
problems - they may have the same classes of problems but not the exact same
problem.

# 004: The New Normal with Michael Nygard
Cognitec - Clojure

Release It - The canonical book about how to write code that will run well in
production and keep running

## Complex Systems, Complex Adaptive Systems

* Ants can create rafts
* Complex systems can adapt and exhibit some amazing emergent behaviours, but
  they also have some really amazing emergent failure modes too.  e.g. the Ant
Death Spiral
Slime moulds can optimize the Tokyo subway system
* Emergent behaviours aren't always desirable.  One of the ongoing challenges
  in any complex system is how you design the rules of a system so that the
emergent behaviours are ones that you as the system like - that there are
favourable outcomes.

## Continuous Partial Failure

* Large, interconnected, interdependent, networks of systems.  We are turning
  our enterprises into one giant distributed system.  Distributed systems -
their primary characteristic is that things fail.
* If I am service provider there is no difference to a consumer between
  downtime and a release
* CPF is both a statistic reality and a way of loosening the coupling so they
  can each be upgraded and deployed at their own rate.
* Why are we doing microservices?  To gain speed and manourverability or
  because Netflix is doing microservices and Netflix is succeeding?  It has
become the vernacular - the language of the day for talking about systems.
  - If you go down that road you might find you still can't achieve a strategic
    objective because you now have to negotiate with 25 product owners instead
of one.
* You still need some way of communicating priorities and deciding where you
  need new services and where you kill old ones.
  - That decision making can be centralised in which case you are fighting
    Conway's law and your org structure down'st match your software structure,
or you can de-centralise but you need some way to radiate to people what the
values, motives and organisational priorities are.
* Let's look a year into the future and talk at the problems you are going to
  encounter then and figure out how we can address them now.
* So you want to be agile why?  What is it you are trying to achieve?  What do
  you want to accomplish?
* The early adopters of the CMM saw a dramatic success with it and then it
  got translated into bunch of document templates.  Almost any advance that we
make can be cargo culted and reduced to a series of rote template actions.

## Anti-fragility

* The tighter the coupling, the more synchornus the processes are, and the
  more production pressure the more you are going to get catastrophic
failures.  This was written about in a book called Normal Accidents which
looked at chemical plant and oil platform disasters.
  - Dynamic coupling - two things that don't correlate today may suddenly
    become correlated.  When that occurs the system has moved into a new
regime of behaviour and you don't really know how it's going to behave - often
it beahves quite vadly.
  - As we are building tehse integrated distributed systems, they are all
    running synchronusly, and they all exposed to unpredictable demand volume
from the internet we have all the charactersitcs of systems that we can't
understand, can't control and that are oging to fail.
XXXSE This is what we have laernt intuititivly from managing complex systems
in production so it is great to have it expressed here
  - I can point to lots other systmes like that in society today.
* One approach is to make them robust.  Robust means that when you distrub
  them away from equalibrium they will return to an equilibrium state on their
own.  However robust systems don't necessarily accomoodate change very well.
* Leap second
  - Using configuration management to ensure systems don't deviate might be
    robust but they are all vulnerable to the same.
* The organisation that flows like water as Sun Tzu states - shaping it's
  course according to the nature of the ground over which it flows.
  - One way you are discovering the terrain is in your business competing with
    other businesses.  Your fitness within the competitive landscape is always
being challenged and tested.
  - Organisims create a new niche for other organisms to occupy.  Some of the
    companies could not exist without the niches created by other organisms.
This competitive landscape is continuously changing, you can't just map a
course over the next several years and say this is where we are going to be in
our five year plan - you ahve to plan to adapt and manevour and continue
changing what you are doing over that time.
XXXSE This is really interesting - I had some thoughts about this a few years
ago when I did a presentation on Agile and I could empahsise it more
  - S3 and EBS faciliated all these other services.  A group will make a
    ervice that makes a bunch of things that were economocally unfrasbible to
attack and makes the possible, maybe even more efficient than what you were
doing before.  What's going on inside my company that's it's own ecosystem
inside the company.
  - XXXSE This is very relevant
  - We have to be uncomfortable with some inefficiencies at micro level to
    gain that competitive advanatage at the macro level.
* Companies don't look at the inventory side of software - by keeping code
  around we continue to pay maintenance costs.  With microservies dispoability
is what youa re after - you want to be able to rewrite things on a very short
term basis.

## DRY and YAGNI

* DRY makes sense within a code base.  Between code bases and teams I'm very
  skeptical.  If we factor something out into a library now we have coupling
between the teams and their release schedule.
* YAGNI is another heuristic that got elevated to the status of commandment.
  We need to rethink that when we are looking at boundaries between teams.

## How to design interfaces for Microservices so that you get the benefit

* The default CRUD REST service interface to an entity approach leads to disaster 

### Nouns versus adjectives

When people look at their domain, and look at the nouns from their domain and
turn them into services.

We are fooled by the noun into thinking we have one unitary concept.  Take an
example from a shopping cart service - I prefer to look at what is the
behaviour - no one could agree on what the data needed to be - when we looked
at the behaviour the shopping cart object was doing many different things.
Every time you looked at the shopping cart it would reprice the items, unless
it was a flagged as being a quote in which case the prices were fixed for a
certain period of time but had an expiration.  Here we had two quite different
behaviours.

If you try and create a single service that does all these things it's going
to have a very complex interface - the consumers of that interface are going to
have to have a lot of semantic knowledge about what the cart does in all these
different modes.

We need an order service that takes a document which is the list of stuff we
are going to order at that time.

That way of partitioning things looks like duplication but it has broken the
dependencies between teams in a way which is much easier to manage.

What you pass to the service is not nouns but adjectives - what do you pass to
the order service - it is stuff that is *orderable*.

* Hexagonal architecture
* Ports and adapters architecture

In Java it's difficult to work with data as data, as opposed to data as domain
objects.  Even when using maps you have to access objects.  It's easier to
navigate an object graph than a map of maps.

c2 wiki is a fantastic resource - the discussions around the patterns are all
there.

Pattern oriented system architecture
