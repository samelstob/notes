# Designing Agile Data Pipelines

* Kafka as a shared infrastructure
* Decoupled producer and consumer
* Keep all data
  - Can keep the intermediatry data
  - Alerts could be fired before data has gone through all processes and
    aggregation 
  - Can go back and trace errors not have to reprocess everything
  - Ability to debug
  - Databus
  - Create topics for intermediate sessions, send data from topic to topic
  - Experiment - subscribe to a topic without any change to what is already
    working
* Can start a new stream for backlog of data

## You need a schema
* Schema on read is kind of a bullshit thing
* After a week you know what the data is like - if you don't sort this out you
  are being lazy.  You are wasting time for everyone who has to read the data.
  - When you do analytics you have to know what the data means - the fields
    are important
  - Storing everything as strings is a waste of space and CPU
  - Everyone downstream will thank you
  - There are normally many more programs downstream
* In large organisations it's impossible to upgrade every application at the
  same time.
* Could put a schema in every message (avro, thrift, protobuf) or put the
  schema in a central repository as it's not going to change very often
* Schemas slow you down in the way that stop lights slow you down.  If you are
  alone at 4am then perhaps you don't need them, but in busy city it's
helpful.
* Schemas can be agile - they allow you to evolve, validate the data
* Microbatch fine down to 0.5s - then need to look at individual records
