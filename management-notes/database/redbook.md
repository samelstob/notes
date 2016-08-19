# Chapter 12: A Biased Take on a Moving Target: Data Integration

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
entities such as customers, employees, sales, purchases, suppliers etc.  Then
carefully curate a master data set for each entity type and get everyone in
the enterprise to use this master.

*Example 1:* Informix new CEO "How many employees do we have?"  Human Resources
VP "I don't know and there is no way to find out".  Informix operated in 58
counties, each with its own labor laws, definition of an employee, etc.  The
only way to answer the CEOs question would be to perform data integration on
these 58 data sources to resolve the semantic issues.

Why would a company allow this situation to occur?  Business agility.  MDM is
the opposite of business agility.

*Example 2:* Large manufacturing enterprise.  Each business unit has its own
purchasing system - there are 300 of these systems.  Why?  The enterprise grew
largely by acquisition.  Each acquisition became a new business unit, and came
with its own data systems, contracts in place, etc.

Data integration

1. *Ingest* A data source must be located and captured.  This requires parsing
   whatever data structure is used for storage.

2. *Transform* For example, Euros to dollars or airport code to city name

3. *Clean* Data errors must be found and rectified

4. *Schema integration* Your wages is my salary

5. *Consolidate (dedupelication)* Mike Stonebraker and M.R. Stonebraker must
   be consolidated into a single record.

The ETL vendors do this at high cost and with low scalability.

What are the research challenges?
* Semi-automatically generate connectors
* Scripting/visualization to specify transforms e.g. Data Wrangler
* Data cleaning
* Schema Matching
* Entity Consolidation

In my opinion, the real problem is an end-to-end system:
  * Perform all steps
  * Seamless integrated
  * Perform curation at scale

## Commentary: Joe Hellerstein

* Data transformation is increasingly a user-centric task, and depends
  critically upon the user experience: the interfaces and languages for
interactively assessing and manipulating data

* To understand if data is dirty, you have to know what it is "supposed" to
  look like

* Even in a single organization, the context of how data is going to be used
  and what it needs to be like varies across people and across time.

* You need to design tools for the people who best understand the data and the
  use case, and enable them to do their own data profiling and transformation
in an agile, exploratory manner.

* In most organizations, the user who understand the data and the context are
  closer to the "business" than the IT department.

* As a footnote, in my experience modern "data scientists" tend to wrangle
  data via ad-hoc scripts in Python, R, or SAS DataStep, and are shockingly
lax about code quality and revision control for these scripts.

* I believe the most relevant solutions will be based on interfaces that
  enable people to understand the state of their data intuitively and
collaborate with algorithms to get the data better purposes for use.
  - We need interactive data systems that can do things like provide
    instantaneous data profiles (vairous aggregates) over the results of
ad-hoc transformation steps, and speculate ahead to suggest multiple
alternative transformations.

