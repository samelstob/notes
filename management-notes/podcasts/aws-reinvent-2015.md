# AWS re:Invent 2015 - BDT314: A Big Data & Analytics App on Amazon EMR & Amazon Redshift
Nate Salmons

* Nasdaq - invented electronic trading >40 years ago
* 1000 tables, 100's sources
* 2 years of data
* Average +7B rows a day (peak +20B)
* 23 nodes DS2 8X large
* 828 vCPUs, 5.5TB RAM, 1PB raw (368TB database), 92GB/s disk bandwidth
* Resize every ~3 months 
* 2.7T rows - 1.8T external, 0.9T aggregates and derived
* 90 tables > 1B rows, 8 tables > 100B
* Larges table 370B - 20TB (59 bytes/row)
* Stream captures from seven equities, options and futures exchanges - orders,
  quotes, trade executions and other market tick data, security master
information (metadata), membership information
* Surveillance and policing, economic research
* "Data continues to grow to fill any container you attempt to place it in"

* Resizing a 300TB warehouse is an over-weekend activity - has to planned and
  managed by operations group
* A lot of data is accessed very infrequently
* Don't want to throw anything, but don't want to pay to keep it at high cost
* On premise -> S3 (CSV) -> Redshift
* S3 (CSV) -> S3 (Parquet) long term storage <- Presto (EMR cluster) 
* SQL JDBC
* Everything lands in Redshift first
* "We are a SQL centric shop"
* In practice access drops off very rapidly (yesterday, versus last month,
  versus last year).

## Security

* Lots of innovation around security and encryption

## Presto

* Presto - open source, MPP, SQL database released by Facebook
* JDBC, ODBC drivers
* Connectors e.g. S3, Hive
* Bootstrap actions e.g. download Java 8 and Presto

## Data Formats

* Row oriented: Parquet, Orc
  +Highly structured, schema validated, metadata
  +File level metadata
* Orc
  +Timestamps are supported by Presto
  -Rigid schema ordering requirements (accessed by column index, not name)
  -Java API for encoding Orc files is clunky
  -Orc Terrible performance with encryption - didn't investigate
* Parquet
  +Widely support: Presto, Spark, Drill
  +Actively developed
  +Columns addressed by name rather than position
  +Accetpible performance when encrypted
  +Clean Java API
  +Data types are not supported by Hive and Presto
    - Transparently encoded dates as integers 
    - Timestamps encoded as big integers (64 bit long)
    - Nanoseconds stored separately

## Schema and data management

* Hive metastore is system of record for Presto: Tables, Locations and how
  they are partitioned
* Migration - ingest data goes into new tables - human is notified to work out
  how to migrate.
* Need to manage a logical and a physical schema for each table 
* Partition tables by date - mostly daily
* Correct data in Redshift, unload to S3, then reprocess into Parquet

# ISM303: Migrating Your Enterprise Data Warehouse to Amazon Redshift

* Multiple ways to get data in: S3, ETL, Kinesis Streaming, Direct Connect,
  Import/Export tool (fedex), Snowball - send the data, Amazon Data Migration
services, System integration partners
* DS2 - HDD, DC1 - SSD 
* Don't just lift and shift - think about what you want
* EMR for less structured data
* COPY command - highly parallel - if used correctly will scale with the size
  of the cluster
* UPSERT/MERGE not directly supported.  Need to DELETE then INSERT
* COMPUPDATE - analyze data and recommend a compression type - a variety of
  algorithms are available
* PKs are not enforced but define keys for efficient query plans
* Manifest JSON file for S3 - ensure load what you intend to

## Boingo Wireless

* Previously Oracle11gR2
* Used SAP data services to ingest into Oracle ($55k/yr)
* Business Objects front end
* Were looking for low TCO
* 15TB +2-3TB/yr
* Evaluated Oracle Exadata, SAP HANA, AWS
* Fully managed, no upfront CapEx
* Cost: ETL, UI, migration
* ETL: Evaluated Informatica and Talend as a service ($6.5k/yr)
* Estimated needed 50DB servers - $48.5
* 2 months to migrate
* Dense storage $1k/yr
* Dense compute $5.5k/yr
* Cut down the data after starting - saved money!
* Reserved instances
* Replaced ETL tool with Python scripts
* Monitor using cloud watch
* AWS Trusted advisor - evaluates unused instances, security, etc.
* Running multiple instances for test

## Edmunds
* Car info
* 30 node Redshift cluster
* 1/5th cost
* Painfully slow queries after a few months
  - Didn't design structure using best practices
  - Didn't invest in real-time monitoring
  - Need additional investment over what Redshift provides
  - Monitor and trend everything
* Some syntactical differences
* Resizing - 2 days of downtime
* Design tables - ensure sort key is correct e.g. timestamp, distribution key,
  compression
* Use single COPY command from S3
* Vacuum - run after loading the data
* Redshift utils 

