# Oracle Parallel Execution Plans Deep Dive
5/5
Randolf Geist

## Introduction

* PX usually works harder than a serial execution to solve the same problem

## PX Building Blocks

* Parallel Access Operators
  - Block range, row id range or partitions
* Producer / Consumer model
  - Child DFO (Producer) -> Parent DFO (consumer)
  - Two sets of PX servers required
  - Table queue (sometimes valled virtual table) is the Oracle construct that
    is used to exchange data between child and parent.  It is in memory
allocated from the shared pool or large pool
  - This is not a zero cost operation!  It costs time, memory and potentially
    network (in RAC).  This is overhead that comes with PX that is not there
in serial.
  - Partition Wise operations can minimise this overhead

## Method - SQL Monitoring

* Look at Activity tab and check how the actual degree of parallelism
  throughout the execution

* Look at the Parallel tab and check for skew

* Look at Plan Statistics tab

## PX Distribution and Skew

* PX skew is not uncommon but hard detect and measure and therefore possible
  one of the most overlooked and underestimated performance problems.

* Look at the Parallel tab in SQL Monitoring to check skew

* ASH can be used for analysing PX skew - XPLAN_ASH

* Methods for influence skew
  - Data volume estimates
  - Query hint - PQ_DISTRIBUTE, join order
  - Partition wise operations
  - Rewrite queries
  - Change application design

* PX SEND HASH distribution does not need to be related to hash join

## DFOs and DFO Trees

* DFO - Data Flow Operation
* However, a lot of these terms are not officially documented by Oracle
* DFO Tree begins at PX coordinator
* Each DFO tree is identified by the TQ number before the comma e.g. Q1, or
  TQ1
* Most plans have one DFO tree (and this is generally what you want for
  simplicity).  If you do have multiple DFO trees you might end up with more
parallel slave sets active at the same time than expected.
* Each DFO tree is optimised separately, has it's own parallel slave sets
  assigned, and can have it's own degree
* 12c has improvements to eliminate situations where multiple DFO trees are
  needed e.g. PX SEND 1 SLAVE

## Buffered operations in PX

*Key limitation about Oracle PX implementation*

* Producer Consumer model limitation: Only one active pair of DFOs per DFO
  tree allowed
* Depending on plan shape and operations multiple DFO pairs could be active
* To prevent this Oracle adds artificial blocking operations that buffer data
* Increased PGA/TEMP requirements
  - This means that PX may have much higher demands for PGA and temp than
    serial
  - RG knows that Oracle has internally discussed whether they want to address this

e.g. HASH JOIN BUFFERED

Two send operations can not be active at the same time (e.g. sending to the hash
join and sending to the QC).

In addition to the in memory hash tables it has already built based on the
data it has received for the first row source, it buffers the data that is
sent from the second row source.

A hash join usually operates that the estimated larger data volume will be
performed as the second row source because this means the smaller row source
will be attempted to be kept in memory.

The larger row source due to this buffering now also needs to be kept in
memory.  In most cases this simply doesn't work - there isn't sufficient PGA
memory available and this buffering has to spill to disk.

Oracle then re accesses the data buffered - if you are lucky taking from PGA if
you are unlucky re-reading it from TEMP - and then performs the actual join
operation and then it can activate the send (e.g. to QC).

Whenever you see HASH JOIN BUFFERED or BUFFER SORT which are not there for
serial executions - Oracle, due to this limitation, has introduced this
artificial blocking and has to perform this additional work - put the data
aside and re access it after having consumed all the data - an important
limitation of PX.

# Analysing and Troubleshooting Oracle PX
Randolf Geist, James Murtagho

## Introduction

* Number of workers assigned matters
  - Too few can be bad
  = Too many can be bad, too

* Communication between worker units required - data needs to be (re-)
  ristributed (overhead!)

* It's not trivial to keep you workers busy all the time (think of e.g. a
  merge sort)

* Can the given task be divided into sub-tasks that can efficiently and
  independently be processed by the workers? ("Parallel Unfriendly")

* Can all assigned workers be kept busy all the time?

  - Possibly only a few or a single worker will be active and have to do all
    the worker.  In this case PX can actually be slower than serial execution.
  - Need to *measure* how busy the workers are kept

## Keeping workers busy

* Busy workers doesn't tell you anything about the efficiency of the actual
  operation / execution plan

  - It's possible to have a completely inefficient execution [plan that keeps
    all the workers happily busy

* An efficient PX plan can only scale if the expected number of workers is
  kept busy ideally all the time

* If your system cannot scale the required resources (like I/O) you just end
  up with more workers waiting

# Analyzing PX Skew

## Systematic approach

1. Detect/measure PX skew
2. Identify execution plan operations causing the problem

1. Use - Activity tab
  - For most of the execution time you want to see at least as many active
    servers as you have a degree
  - In 12c can select "by plan line" from the drop down - altough still
    dificult to see if these lines were the cause or the effect of the skew
  - Under Plan Statistics can filter by individual PX slaves
  - Under the parallel tab it is possible that different servers had skew at
    different points in the execution which resulted in a similar level of
activity in overall!

2. Real-time SQL monitoring can not currently identify skew on a plan line level 

## Multiple DFO trees

  - Multiple DFO trees are not displayed correctly in SQL Monitoring -
    different trees can have different degrees of parallelism

- Under the Parallel tab you will see Parall Group which shows the degree of
  each set

- You can look careful at the Plan Statistics e.g. PX BROADCAST executions to
  see the degree of each tree

- Another consequence is that you get multiple child cursors

- Check that you really do have skew and the Activity chart is not skewed due
  to multiple DFO trees with different parallel degrees
