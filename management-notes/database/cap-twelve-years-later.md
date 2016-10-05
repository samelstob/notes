# CAP Twelve Years Later: How the "Rules" Have Changed
Eric Brewer, University of California, Berkley

The CAP theorem asserts that any *networked shared-data system* can have only
two of three desirable properties:

* *Consistency* equivalent to having a single up-to-date copy of the data
* *Availability* of that data to (for updates)
* *Partition* tolerance (Network partitions)

* CAP opened the minds of designers to a wider range of systems and tradeoffs
* The "2 of 3" formulation tended to oversimplify the tensions among
  properties
* CAP prohibits only a tiny part of the design space: perfect availability and
  consistency in the presence of partitions, which are rare (arguably not that
rare on mobile networks)
* There is an incredible range of flexibility for handling partitions and
  recovering from them
* The modern CAP goal should be to maximize combinations of C and A that make
  sense for the specific application

## ACID and BASE

* The relationship between CAP and ACID is more complex and often
  misunderstood
* *Atomicity*
  - Common to ACID and CAP.  All systems benefit from atomic operations.
* *Consistency*
  - ACID
    - A transaction preserves all database rules, such as unique keys
  - CAP
    - Single-copy consistency, a strict subset of ACID consistency.
    - ACID consistency cannot be maintained across partitions - partition
      recovery will need to restore ACID consistency.
    - Maintaining invariants during partitions might be impossible (e.g.
      unique keys), thus the need for careful thought about which operations
to disallow and how to restore invariants during recovery
* *Isolation*
  - Serializability - concurrent transactions complete as if executed
    serially.  In otherwords, transactions do not see intermediate state of
other transactions.
  - Serializability requires communication and thus fails across partitions.
    If the system requires ACID isolation, it can operate on at most one side
during a partition.
* *Durability*
  - No reason to forfeit durability although CAP may choose to avoid needing
    it via soft state due to its expense
  - In general ACID transactions on each side of a partition make recovery
    easier

* "Revenue goals and contract specifications (presumably SLAs), system
  availability was at a premium, so we found ourselves regularly choosing to
optimize availability through strategies such as employing caches or logging
updates for later reconciliation"
* ACID versus BASE (1998) was not well received at the time, primary because
  people love the ACID properties and are distant to give them up.

1. Little reason to forfeit C or A when the system is not partitioned
2. Choice between C and A can occur many times within the same system at very
   fine granularity; subsystems can make different choices, the choice can
change according to the operation or even the specific data or user involved
3. CAP properties are not vinary
  - Availability 0-100%
  - Even partition have nuances, including disagreement within the system
    about whether a partition exists

## CAP-Latency Connection

* Latency and partitions are deeply related.  The essences of CAP takes place
  during a timeout - the *partition decision*
  C - Cancel the operation and thus decrease Availability
  A - Proceed with the operation and thus risk Consistency

Retrying communication e.g. via Paxos or 2PC just delays the decision.  At some
point the program must make a decision - retrying indefinitely is choosing C
over A. 

* There is no global notion of a partition - some nodes might detect a
  partition, and others might not.
* Nodes that detect a partition can enter a *partition mode*

* Yahoo - PNUTS
  - master copies are local - maintain remote copies asynchornously
* Facebook
  - master copy in one location, updates go to master so users must read from
    master for e.g 20 seconds after an update until local copy is consistent

## Managing Partitions

Challenging case for designers is to mitigate a partition's effects on C and A

1. Detect the start of a (network) partition
2. Enter an explicit *partition mode* that may limit some operations (A)
3. Initiate partition recovery when communication is restored (C)
  - a plan for all invariants that might be violated

Partition mode:
1. Limit some operations (A)
2. Record extra information about operations that will be helpful during
   partition recovery (C)

## Which Operations Should Proceed?

* Externalized events e.g. charging a credit card
  a. Record the intent and execute it after the recovery



## CAP Confusion

* If users cannot reach the service at all there is no choice between C and A
  except when part of the service runs on the client (offline mode)
* Scope of consistency - within some boundary state is consistent, outside all
  bets are off
  - In Google, the primary partition usually resides within one datacentre;
    however Paxos is used on the wide area to ensure global consensus, as in
Chubby and Megastore.
* In pratice, most groups assume that a datacentre (single site) has no
  partitions and thus design for CA within a single site.
  - Although partitions are less likely they are possible.
  - Given high latency across WAN it is relatively common to forfeit perfect
    consistency for performance
* A hidden cost of forfeiting C is the need to know the system's invariants.
  - In a consistent system invariants tend to hold even when a designer does
    not know what they are.
  - A requires restoring invariants after a partition so designers must be
    explciit about all the ivnariatns, which is both challenging and prone to
error.

 

## What I learned

* A much better understanding of what the CAP theorem is
  - A is availability to updates (remaining available for read-only is
    trivial)
  - Network partition means that not all of the nodes can communicate
* Network partition is really a timeout - at some point you have to make a
  decision whether there is a network partition.  At the point you make a
choice between A or C
* Partition tolerance is pretty much unavoidable
* It isn't a black and white choice between A and C - it is more nuanced
* Tradeoffs between C and A can be made not just at the system level but at the component or even business operation level
  - e.g. 
* Choosing Availability during a Network partition means some mechanism is
  needed to resolve consistency.  This could involve escalation to a human
  - CRDT - Commutative Replicated Data Types
  - Commutative - Result is the same regardless of the order - A + B = B + A
  - e.g. To represent a set, we could store a log of additions and
    removals, not just the set itself.
additions and removals are applied (hmmm)
