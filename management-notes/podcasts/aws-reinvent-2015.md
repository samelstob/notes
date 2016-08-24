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
