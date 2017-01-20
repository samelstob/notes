# "One Size Fits All" Database Architectures Do Not Work For DSS
Clark D. French
SIGMOD
1995

* We can say OLTP and DSS have "opposing laws of database physics"
* "Too Much Data, Not Enough Information"
* "I have found that there is a relationship between certain attributes of the
  data and how data is typically  used within the SQL language for DSS.  These
data attributes are typically static over the life of the data and hence
predictable, where the queries are not.  Some of these data attributes are
cardinality, distribution, and value range."
 
## Data Attributes and SQL

* "There is a relationship between a column's cardinality and it's usage with
  the SQL language."
  - A column that has a low cardinality, say under 1000 unique values, tends
    to be used in SQL WHERE clauses and GROUP BY clauses most frequently in
DSS.  Where used in the SQL WHERE clause a low cardinality column is usually
used in EQ or NE predicates.  It is rate to see a low cardinality column used
in range queries and aggregates"
  - XXXSE Is this because they are low cardinality or because they are
    dimensions?  Are dimensions typically low cardinality?

  Cardinality (K)           SQL Usage
  K < 1000                  EQ, NE predicates and GROUP BY
  1000 < K < 100000         Both
  K > 100000                Range and Aggregation

As stated above data cardinality, distribution and value range tend to be
relatively static over time.
  - SE This does appear to be true.  Some fields like "check in date" don't
    seem to follow this (unless you count the fact they are always
increasing).  This implies that Oracle statistics should be fairly static for
a particular fact table over time - is this true?

Now that we have described the relationship between data and SQL common usage
*is it possible to design an index that takes advantage of known attributes of
the data to increase query time performance"*

## Bitmap Indexes

* Developed in the 1960's this indexing approach gains performance by only
  handling low cardinality data
* It represents each distinct value as arrays of bits where 1 or 0 in a
  relative position in the array represents True or False for that value for
the corresponding relative record within the database relational table

* The traditional OLTP database optimizer approach of building up record
  lists, although great for OLTP small found sets, is cumbersome at best for
large multi-million record found sets typically found in DSS.  Bitmaps are
ideally for representing large found sets.
  - XXXSE Is this what a dataflow engine is?
  - XXXSE A million values can be represented in 2^20 bits = 2^17 bytes =
    128kB
  - A billion values in 128MB, 8 billion values in 1GB
* Good at EQ, NE, and GROUP BY queries
* When multiple predicates are used in a query the arrays of bits for each
  value can easily be combined using boolean operations
* The fundamental question is whether one database approach can be everything
  to everyone.  The answer will come, as it should, from the market, which
will decide if it will accept database products that are focussed exclusively
on DSS but offer better performance
  - XXXSE The market did decide this - NoSQL - although this was as much about
    scaling number of "users" to web scale as it was to OLTP versus DSS
 
