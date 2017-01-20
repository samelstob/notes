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
cardinatlity, distribution, and value range."
 
## Data Attributes and SQL

* "There is a relationship between a column's cardinatlity and it's usage with
  the SQL language."
  - A column that has a low cardinality, say under 1000 unique values, tends
    to be used in SQL WHERE clauses and GROUP BY clauses most frequently in
DSS.  Where used in the SQL WHERE clause a low cardinality column is usually
used in EQ or NE predicates.  It is rate to see a low cardinality column used
in range queries and aggregates"
  - SE Is this because they are low cardinality or because they are
    dimensions?  Are dimensions typically low cardinality?

  Cardinality (K)           SQL Usage
  K < 1000                  EQ, NE predicates and GROUP BY
  1000 < K < 100000         Both
  K > 100000                Range and Aggregation

As stated above data cardinality, distribution and value range tend to be
relatively static over time.
  - SE This does appear to be true.  Some fields like "check in date" don't
    seem to follow this (unless you count the fact they are always increasing)

Now that we have described the relationship between data and SQL common usage
*is it possible to design an index that takes advantage of known attributes of
the data to increase query time performance"*

## Bitmap Indexes

* Developed in the 1960's this indexing approach gains performance by only
  handling low cardinality data
* Good at EQ, NE, and GROUP BY queries
 
