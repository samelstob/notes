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
  * How much data? How many rows/volume?
  * How scattered/clustered (partially)
  * Caching - not covered at all by the optimizer

The optimizer doesn't necessarily understand the data the way you might expect
it to understand it.

## How many rows?

The quesiton of how much data can be broadly divded into three categories:

* Single table cardinality
* Join cardinality
* Filter subquery/Aggregation cardinality

* Cardinality - Number of rows
* Selectivity - Filtering

## Single Table Cardinality

* Fairly straightforward - what is the selectivity of the predicates

* Optimizer challenges

Although this might be straightforward the optmizer has some problems coping
with different challenges that can be in your data.  The optimiser might not
have a good understanding of even these seemingly straightforward single table
cardinality

  - Skewed column value distribution
    XXXSE e.g. Request Type
  - Gaps/clustered values
  - Correlated column values
  - Complex predicates and expressions
  - Bind variables


* Optimizer challenges

