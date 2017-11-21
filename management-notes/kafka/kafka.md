# Kafka

# Kafka Connect

https://www.slideshare.net/KaufmanNg/data-pipelines-with-kafka-connect?qid=5172ac08-a903-437b-9649-fb35f45039b2&v=&b=&from_search=1

# Billions of Messages a Day - Yelp's Real-time Data Pipeline

* Considered a raw bulk-data API e.g. arbitrary SQL
  - This leads to tight coupling between systems - a major violation of
    service boundaries
  - DB snapshots/dumps - The database doesn't always have much meaning without
    the underlying code e.g. enums, flags
* Difficult to make service notifications work correctly with transactions:

  session.begin()
  business = Business()
  session.add(business)
  my_service_client.notify_business_changed(business.id)
  session.commit()
* Message bus: n²->n connections
  - What happens if the service notification succeeds but the transaction
    fails?  Or vice-versa?  End up with complicated retry-fail logic.
* DB event stream - use log compaction to keep the most recent version of each
  key
* Avro allows forwards and backwards compatible schema casting
  - JSON is easy for someone to break downstream users
* Think carefully about the envelope of all messages - including an owner
  - uuid
  - timestamp
  - schema_id
  - payload
  - previous_payload
  - meta attributes (tuples of schema_id & payload)
* Flat-First schemas - simpler, easy to write to flat data sinks e.g. RDBMS 
* Python's process cycle doesn't fit well with Kafka consumers

# Microservices with Kafka - Kafka Streams API
NY 2016

## Spark Streaming with Kafka
  - 2 connectors - compromises with each
  - Have to deal with offsets and failures 
  - Checkpoints require a shared filesystem e.g. HDFS, S3 and Java
    serializable
  - Micro-batches
    - If there is a lot of data to read e.g. after restarting after failure
     it will use a lot of memory and may crash - 1 RDD per Kafka partition
    - Allocation of resources in Spark
      - CPU and memory are allocated when the job is submitted and cannot be
        updatedi on the fly
* Python cod ein production
  - Harder to deploy than a JAR file
* Spark 2.0 Structured Streaming - looks good

## Kafka Streams

* One message at a time - low memory usage
* Natively consumes, pushes, handles offsets
* No separate cluster - Kafka is the cluster manager (consumer groups)

## Parallelism

* One JVM: 1 task per partition, number of worker threads set by the developer
* Multi-JVM: Consumer group, 1 consumer per JVM
  - Partition reassignment when a consumer is stopped or dies

## KStream vs Ktable
