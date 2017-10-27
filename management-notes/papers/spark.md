# Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-memory Cluster Computing
Matei Zaharia, Mosharaf Chowdhury, et. al.

## My summary

Describes RDDs which are the central abstraction of Spark and key to it's
performance as compared to Hadoop.

RDDs are a partitioned, in memory, read-only, data set that tracks it's lineage - not
sure how.

### Key insights/takeaways

* Code as data - this idea is not on my radar - I would never have thought of
  this design.  Java/Scala code is compiled and sent to the cluster for
execution.  This avoids the need to manually distribute e.g. JARs to the
cluster and can allow a much more agile approach e.g. REPL
* REPL  - again this idea would not have occurred to me - by combining the
  ability to send compiled Classes to the cluster with the Scala REPL they
were able to create an interactive Big Data cluster
* It supports Python and Java but not in the same operation (as far as I can tell) - i.e. either of these languages can interact with RDDs but there is no cross-language data interchange (except through RDDs I suppose)
* Failures - optimistic approach - Checkpoints are not used (I think) -
  instead upon failure an RDD is reconstructed from it's lineage.  In the case
of no failures there is no performance penalty.
* RDDs are read-only - with all the benefits that brings - very much like functional programming
* Spark's performance over Hadoop seems to come through two key points -
  neither that surprising
  i) Significantly reducing disk access
  ii) Reducing serialization/de-serialization overhead

i) Spark RDDs are in-memory.  I think they can also spill to disk if they get
large?
ii) Spark can represent data as bogo Java objects (i.e. not serialized) to reduce overhead
* Although RDDs are a sort of "share memory" by restricting the way that
  programs interact with it to "coarse-grained transformations" it can be made
much more efficient
* RDDs as compared to general shared memory recognize that the key use case is
  applying the same operation to many data items - there is no need for fine
grained access for these use cases

## Interesting References

G. Ananthanarayanan Disk-locality in datacenter computing considered
irrelevant.  HotOS 2011
J. W. Young.  A first order approximation to the optimum checkpoint interval.
CACM 1974
Delay Scheduling: A simple technique for achieving locality and fairness in
cluster scheduling

## Abstract

* RDDs are motivated by two types of applications that current computing
  frameworks handle inefficiently (presumably Hadoop); iterative algorithms
and interactive data mining tools.

## 1 Introduction

* Current frameworks are inefficient for applications that reuse intermediate
  results across multiple computations.  Data reuse is common in many
iterative machine learning and graph algorithms, including PageRank, K-means
clustering, and logistic regression.  In most frameworks the only way to reuse
data between computations e.g. between two MR jobs is to write it to an external stable storage system e.g. HDFS.  This incurs overheads due to replication, disk I/O, serialization (and presumably network I/O)

* If a partition of an RDD is lost, the RDD has enough information about how
  it was derived from other RDDs to recompute just that partition.

* Spark provides a convenient language-integrated programming interface
  similar to DryadLINQ in the Scala programming language.  In addition, Spark
can be used interactively to query big datasets from the Scala interpreter. 

## 2. RDDs

* Formally, an RDD is a read-only, partitioned collectio nof records.  RDDs
  can only be created through deterministic operations on either (1) data in
stable storage or (2) other RDDs.
* Example transformations include map, filter, and join
* RDDs do not need to be materialized at all times.  Instead, an RDD has
  enough information about how it was derived from other datasets (it's
lienage) to compute it's partitions from data on stable storage; a program
cannot reference an RDD that it cannot reconstruct after a failure.
* Users can control two other aspects:
  - Persistence - indicate which RDDs they will reuse and choose a storage
    strategy (e.g. in-memory stroage)
  - Partitioning based on a key in each record - useful for placement
    optimizations, suc as ensuring that two datasets that will be joined
together are hash-partitioned in the same way

### Advantages of the RDD Model

RDD compared to Distributed Shared Memory (DSM)

* In DSM systems, applications read and write to arbitrary locations in a
  global address space.  RDDs can only be created ("written") through
coarse-grained transformations, while DSM allows reads and writes to each
memory location.

* RDDs immutable nature lets a system mitigate slow nodes (stragglers) by
  running backup copies of slow tasks as in MR.  Backup tasks would be hard to
implement with DSM

## 3 Spark Programming Interface

* To use Spark, developers write a driver program that connects to a cluster
  of workers.  The driver defines one or more RDDs and invokes actions on
them.  Spark code on the driver also tracks the RDDs' lineage.  The workers
are long-lived processes that can store RDD partitions in RAM across
operations.

* Users provide arguments to RDD operations like map by passing closures
  (function literals).  Scala represents each closure as a Java object, and
these objects can be serialized and loaded on another node to pass the closure
across the network.  Scala also saves any variables bound in the closure as
fields in the Java object.

* Our function names are chosen to match other APIs in Scala and other
  functional languages: for example, map is a one-to-one mapping, while
flatMap maps each input value to one or more outputs (similar to map in
MapReduce)

* "consistent partitioning across iterations is one of the main optimizatons
  in specialized frameworks like Pregel.  RDDs let users express this goal
directly"

## 4. Representing RDDs

We propose representing each RDD through a common interface that exposes five
pieces of information
* Partitions - which are atomic pieces of the dataset
* Dependencies on parent RDDs
* A function for computing the dataset based on it's parents
* Metadata about it's partitioning scheme
* Metadata about data placement

* How to represent dependencies between RDDs - we found it both sufficient and
  useful to classify dependencies into two types:
  - Narrow dependencies, where each partition of the parent RDD is used by at
    most one partition of the child RDD
    - e.g. map, filter, union, join with
inputs co-partitioned (e.g. hash partitioned on the same key)
  - Wide dependencies, where multiple child partitions may depend on it
    - e.g.  join with inputs not co-partitioned, groupByKey

## 5. Implementation

* We have implemented Spark in about 14k lines of Scala.  The system runs over
the Mesos cluster manager, allowing it to share resources with hadoop, MPI and
other appliactions.

* Moving processing close to the data: "Our scheduler assigns tasks to machines based on data locality using delay scheduling.  If a task needs to process a partition that is available in memory on a node, we send it to that node.  Otherwise, if a task processes a partition for which the containing RDD provide spreferred locations (e.g. an HDS file) we send it to those.

* "We do not tolerate scheduler failures, though replicating the RDD lineage
  graph would be straightforward"

### 5.2 Interpreter Integration

* "The Scala interpreter normally operates by compiling a class for each line
  typed by the user, loading it into the JVM, and invoking a function on it"

We made two changes:

1. Class shipping: To let the worker nodes fetch the bytecode for the classes
   created on each line, we made the interpreter serve these classes over
HTTP

    XXXSE: I never really internalised the "think of HTTP as default protocol" approach

2. Modified code generation: To ensure that object graph dependencies are
   correctly shipped to worker nodes

### 5.3 Memory Management

* Three options for storage of persistent RDDs
  1 In-memory as deserialized Java objects
  2 In-Memory storage as serialized data
  3 On disk

LRU used at the level of RDDs

### 5.4 Support for Checkpointing

Recovery from lineage can be time-consuming for long lineage changes (just
like recovering from Redo) - thus it can be helpful to checkpoint some RDDs to
stable storage

In general, checkpointing is useful for RDDs with long lineage graphs
contaiing wide dependencies.

Spark leaves the decision of which data to checkpoint to the user.

Read-only nature of RDDs makes them simpler to checkpoint than general shared
memory - can be written out in the background.

## 6 Evaluation

Overheads of Hadoop
1) Job setup
2) HDFS (memory copies and checksums)
3) "Converting pre-parsed binary data into Java objects took 3 seconds, which
is still almost as expensive as the logicistic regression itself" 

## 7 Discussion

"One final question is why previous frameworks have not offerred the same
level of generality.  We believe that this is because these systems explored
specific problems that MR and Dryad do not handle well, such as iteration,
without observing that the common cause of these problems was a lack of data
sharing abstractions"



