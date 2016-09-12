# Scaling Logstash - A Collection of War Stories

* Pere Urbon Bayes

* Logstash -  you are as fast as the slowest output you have
* logstash-forwareder
  - Light weight shipper written in Go

* Seems to suggest you need another component e.g. RabbitMQ to decouple and
  buffer
* I am surprised as I thought logstash bufferred

https://qbox.io/index.php/blog/kafka-and-elasticsearch-a-perfect-match-1
http://engineering.chartbeat.com/2015/05/26/logstash-deployment-and-scaling-tips/
  - Issues with logstash forwarder.  Now forked by etsy.

Using AWS? You definitely want to be using the AWS plugin .  This allows
Elasticsearch to use the EC2 APIs for host discovery, instead of relying on
hardcoding a list of the servers.

* https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html

https://github.com/elastic/elasticsearch-cloud-aws
* https://github.com/elastic/elasticsearch-hadoop
* http://www.flax.co.uk/blog/2015/09/28/faster-bulk-indexing-in-elasticsearch/
  - "This makes error handling a little more tricky (although doable), but we
    found that it doubled indexing speed again, and this time CPU was pretty
much maxed out across the cluster."
* http://www.slideshare.net/sematext/tuning-elasticsearch-indexing-pipeline-for-logs?qid=8a21beaa-76c0-4b1c-a244-1cb6ed1e87d7&v=&b=&from_search=12

* https://github.com/miku/esbulk

  - Client Node is probably not appropriate
* https://www.elastic.co/guide/en/logstash/current/pipeline.html
