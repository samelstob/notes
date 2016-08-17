# Chapter 12: Data Integration

Began with major retailers in 90s consolidating their sales data into a data
warehouse.  A buyer would figure out that pet rocks are "out" and barbie dolls
are "in".  A typical retail data warehouse paid for itself with a year through
better buying and stock rotation decisions.  In the late 90s and 2000's there
was a giant "pile on" as essentially all enterprises followed.

A new industry was spawned to support the loading of data warehouses, called
ETL:

a) Construct a global schema in advance
b) Send a programmer out to the owner of each data source and have him figure
out how to do the extraction
c) Have him write transformations and cleaning routines
d) Have him write a script to load the data in the warehouse

Scales to about a dozen data sources:

1. A global schema is needed up front.  An upfront global schema is incredibly
   difficult to construct for a broad domain.  This limits the plausible scope
of data warehouses.

2. Too much manual labour.  A skilled programmer is required to perform most
   of the steps.

3. Data integration and cleaning is fundamentally difficult.  The typical DW
   project in the late 90's was 2X over budget and 2X late.  Planners
underestimated the difficult of data integration.  Data is dirty - as a rule
of thumb 10% of your data is incorrect.  De-dupe is hard - one has to decide
if Mike Stonebraker and M.R. Stonebraker are the same entity or different
ones.  Equally challenging is two restaurants at the same address.  They might
be in a food court, one might have replaced the other, or this might be a data
error.  It is expensive to figure out ground truth in such situations.

Fast forward to the 2000's and the new buzzword is Master Data Management
(MDM).  The idea is to standardize the enterprise representation of important
entities such as customers, employees, sales, purchases, suppliers etc.
