# Bigtable: A Distributed Storage System for Structured Data
Fay Change, Jeffrey Dean, Sanjay Ghemawat, et al.
2006

* Scale from a handful to thousands of servers, and store up to several hundred terabytes of data

## Data Model

* A Bigtable is a sparse, distributed, persistent multi-dimensional sorted map
  - Sparse (not sure what this means for a map?)
  - Distributed - across multiple machines
  - Multi-dimensional - not sure what this means in context of a map either

### Rows

* Row keys are arbitrary strings (currently up to 64kB, although 10-100 bytes
  is typical)
* Every read or write of data under a single row key is atomic (regardless of
  the number of different columns being read or written in the row)
* Bigtable maintains data in lexicographic order by row key.
* The row range for a table is dynamically partitioned.
* Each row range is called a tablet, which is the unit of distribution and
  load balancing

### Column Families

* Column keys are group into sets called column families
* A column familiy must be created before data can be stored under any column
  key in that family
* It is our intent that the number of disitinct column families in a table be
  small (in the hundreds at most) and that families rarely change during
operation.  In contrast, a table may have an unvounded numer of columns
* A column key is named using the following syntax "family:qualifier"
* An example column familiy is "anchor".  Each column key in this family
  represents a single achor.  The qualifier is the name of the referring site,
the cell contents is the link text e.g. anchor:cnnsi.com->CNN, anchor:my.look.ca->CNN.com 
* Access control and disk and memory accounting are performed at the
  column-family level

### Timestamps

* Each cell in a Bigtable can contain multiple veresions of the same data;
  these versions are indexed by timestamp
* Bigtable can garbage-collect cell versions either last 'n' or last 'n' days

## API

* "We could restrict the scan above to only produce anchors whose columns
  match the regular expression anchor:.cnn.com or to only produce anchors
whose timestamps fall within ten days of the current time"

  - This sounds like a misuse of columns to me 

* Bigtable does not currently support general transactions across row keys

## Building Blocks

* Bigtable uses GFS to store log and data files
* The Google SSTable file format is used internally to store Bigtable data.
  An SSTable provides a persistent, ordered immutable map from keys to values
* Bigtables relies on a highly-available and persistent distributed lock
  service called Chubby
  - Column family information and ACLs are stored in Chubby

## 5. Implementation

Big table has three major components
  - A library that is linked into every client
  - One master server
  - Many tablet servers

* Tale servers are dynamically added or removed to accommodate changes in
  workloads
* Each table server manages typically 10-1000 tables
* Client data does not move through the master
* Bigtable clients do not rely on the master for table location information,
  most clients never communicate with the master.  As a result, the master is
lightly loaded in practice
* As a table grows, it is automatically split into multiple tables, each
  approximately 100-200MB in size

### 5.1 Tablet Location

  Chubby -> Root tablet (METADATA) -> Other METADATA tablets -> User Tables
* The client library caches tablet locations
* If the client does not know the location, or it is discovered that the
  cached location is incorrect, then it recursively moves up the tablet
location hierarchy.  if the client's cache is empty, the location algorithm
requires three network round-trips, including one read from Chubby.

### 5.3 Tablet Serving

* Sounds a bit like
