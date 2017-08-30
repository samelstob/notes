# Oracle Cost-Based Optimizer Basics
Randolf Geist

## Optimizer Basics

* Three main questions when looking for an efficient execution plan

  * How much data? How many rows/volume?
  * How scattered / clustered is the data?
  * Caching?

If you really want to understand what is happening you need to gain an
understanding of what your data looks like, and then understand what the
optimiser might get wrong about your data layout.

* Two main strategies

* "Big Job approach"
  - e.g. Hash join full table scan
  - How much data, volume?

* Many "Small jobs" 
  - e.g. Nested loops, index access path
  - Access a subset in an iterative fashion
  - How many iterations/rows?
  - Effort per iteration? Clustering/Caching 

There is a huge grey zone where both approaches might be applicable.

The CBO estimate doesn't cover all of these questions to the same extent
  * How much data? How many rows/volume? - pretty good coverage by CBO
  * How scattered/clustered - partially covered
  * Caching - not covered at all by the optimizer

*The optimizer doesn't necessarily understand the data the way you might expect it to understand it.*

## How many rows?

The question of how much data can be broadly divided into three categories:

* Single table cardinality
* Join cardinality
* Filter subquery/Aggregation cardinality

* Cardinality - Number of rows
* Selectivity - Filtering

## Single Table Cardinality

* Fairly straightforward - what is the selectivity of the predicates

* Optimizer challenges

Although this might be straightforward the optimizer has some problems coping
with different challenges that can be in your data.  The optimiser might not
have a good understanding of even these seemingly straightforward single table
cardinality

  - Skewed column value distribution
    XXXSE e.g. Request Type
  - Gaps/clustered values
    - XXXSE Could a particular client only be present at certain times of day
  - Correlated column values
    XXXSE e.g. Request Type and Response Type.  The selectivity of
"RequestType=Booking" is probably the same as "RequestType=Booking and ResponseType=Booking" the selectivity is 
  - Complex predicates and expressions
  - Bind variables

### Conclusions - Single Table Cardinality


* Influences the favoured Single table Access Path (FTS, Index Access, etc.)

* Influences the join order and join methods (NESTED LOOP, HASH, MERGE)

An incorrect single table cardinality potentially screws up whole execution
plan.  Impact not limited to a single table!

"A bad single table cardinality estimate can echo through the whole plan."

Simple to verify.  For your critical queries you should make sure your single
table cardinality is in the right ball park.

## Demo

* *Although things might be obvious to you they might not be obvious to the
  optimiser.*

* If the statistics are not representative of your data and your queries
  then it doesn't matter how fresh they are

* A function predicate on a column (TRUNC) with a highly skewed value resulted in a very high proportion of rows returned from a
  FTS compared to the estimate.  This in turn led to use of a NL join which
was very slow.

## How many rows? - Join cardinality

### Key points 

* Oracle joins exactly two row sources at a time

* If more than two row sources need to be joined multiple join operations are
  required

* Many different join orders possible (factorial!)

### Optimizer challenges

Join cardinality - how many rows will be returned by the join

* Getting the join selectivity right

* A join can mean anything between no rows and a Cartesian product!

  T1 1000 rows
  T2 1000 rows

Join could result in anywhere between zero rows and 1M rows

If the inputs to join are estimated incorrectly, even if the optimizer gets
the join selectivity correct, then the join cardinality will be incorrect.

This is an example of why a bad single table cardinality estimate can echo
through the whole plan.

* Semi Joins (EXISTS, ANY)
* Anti Joins (NOT EXISTS, ALL)
* Non-equi joins (Range, Unequal, etc.)

Even for the most common form of a join - the (inner?) Equi-join - there are several
challenges

* Non-uniform join column value distribution
* Partial overlapping join columns
* Correlated column values
* Expressions
* Complex join expressions (multiple AND, OR)

### Demo

*What seems to be potentially obvious to a human being is not necessarily
obvious to the optimiser.*

My summary: A highly skewed column which is a foreign key is joined to it's
parent table and filtered on a single value using a predicate on the parent
table.  The optimiser knows that the data in the FK is skewed and knows that
we are filtering on one value but it doesn't know what value the skewed FK
will join to so underestimates the join cardinality.

XXXSE Is this equivalent to a predicate on a lookup dimension?  Is this why a
star query transformation is useful because it allows the optimiser to know
the values of the filter predicates for the fact table not the dimension
table and therefore have a better chance of estimating the selectivity of
those predicates?

XXXSE Can statistics be gathered for this case i.e. on a FK?

## How scattered/clustered?

* Data is organised in blocks.  Many rows can fit in a single block.

* According to a specific access pattern data can be either scattered across
  many different blocks or clustered in the same or few blocks

* Does make a tremendous difference in terms of efficiency of a "small job"
  approach

### Example - index range scan

An index range scan of 1000 rows in the worse case has to access 1000 table blocks

e.g. 
  1000 * 5ms = 5s

XXXSE How does this change with SSD at all?

1000 rows visiting 10 table blocks (because they are clustered) = 10 * 5 =
50ms = 100X difference

XXXSE Does clustering affect FTS?  Only if you have a way to eliminate looking
through the whole block

* Scattered data means potentially many more blocks to compete for the Buffer
  Cache for the same number of rows
  => Caching

  - you are bringing in "collateral data" into the BC that happens to be in
    the same blocks as the ones you need

* Scattered data can result in increased
  - physical disk I/O
  - logical I/O
  - write disk I/O (Log Writer, DB Writer)
  - free buffer waits

## How scattered/clustered?

* Clustering of data can be influence by physical design

* Physical design matters:
  - Segment space management (MSSM/ASSM)
  - Partitioning
  - Index/Hash Cluster
  - Index Organised tables (IOT)
  - Index design / multi-column composite indexes

e.g. hash partitioning might destroy some of the natural time based
clustering in a data warehouse

* There is a reason why Oracle internal data dictionary uses clusters all over
  the place

XXXSE However PX by default bypasses the buffer cache so clustered tables
would *increase* the amount of I/O required to do a single table FTS

### Clustering and CBO

* There is only a single measure of clustering in Oracle - the index
  clustering factor - this is represented by a single value
* The logic measuring the clustering factor by default does not cater for data
  clustered across few blocks (ASSM)

ICF is calculated by walking the leaf rows and incrementing every time the
block changes.  ICF can be as low as the number of blocks or as high as the
number of rows covered by the index.

* ICF doesn't account for the number of distinct blocks - it may be possible
  to have very few distinct blocks yet have a high ICF

### Clustering Challenges

* There is no inter-table clustering measurement
* The optimiser therefore doesn't really have a clue about the clustering of joins

  XXX Does this mean "clustered table joins"

* You may need to influence the optimiser's decisions

## Caching

* The optimizer's model by default doesn't consider caching of data

* Every I/O is assumed to be physical I/O

* But there is a huge difference between logical I/O (measured in microseconds)
  and physical I/O (measured in milliseconds)

* You might have knowledge of particular application data that is "hot" and
  usually stays in the BC

* Therefore certain queries against this "hot" data can be designed based on
  that knowledge

* The optimizer doesn't know about this.  You may need to influence the
  optimizer's decisions.

## Caching considerations

* It is important to point out that even logical I/O is not "free"

* So even putting all objects entirely in the BC inefficient execution plans
  may still lead to poor performance

* Excessive logical I/O, in particular on "hot blocks", can lead to latch
  contention and CPU starvation

## Summary

* Cardinality and Clustering determine whether the "Big job" or "Small job"
  strategy should be preferred

* If the optimiser gets these estimates right, the resulting execution plan
  will be efficient within the boundaries of the given access paths

* Know your data and business questions

## Notes

* Jonathan Lewis' "Designing Efficient SQL"

* Christian Antognini "Troubleshooting Oracle Performance Ch. 6"

* Be aware of Query Transformations.  The optimiser might rewrite your query
  to something that is semantically equivalent but potentially more efficient

* This might take you by surprise when trying to understand the execution plan
  favored by the optimizer

# Oracle Cost-Based Optimizer - Advanced

## Clustering Factor

## Statistics/Histograms

## Datatype issues
