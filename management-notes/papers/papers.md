# Maglev: A Fast and Reliable Software Network Load Balancer

## 1. Introduction

* Google's software network load balancer
* Scale-out with commodity hardware
* Seems to rely on a router feature called Equal Cost Multi path (ECMP) to
  send the same data to each node?  Need to find out what ECMP is
* Uses kernel-bypass techniques to saturate a 10Gbps link
* Does packet re-writing - encapsulating packets in GRE to send them to
  particular backends
* "The load balancer is responsible for matching each packet to its
  corresponding service and forwarding it to one of that service's endpoints."
* Hardware load balancers generally only scale-up.  Though often deployed in
  pairs to avoid SPOF they only provide "1+1 redundancy" which does not meet
Google's requirements for high availability.
* Software load balancing can be iterated on more quickly than hardware "By
  controlling the entire system ourselves, we can quickly add, test, and
deploy new features"
* Maglev provides N+1 redundancy.
* Capacity
  - "Let N be the number of machines in the system and T be the maximum
    throughput of a single machine.  The maximum capacity of the system is
bounded by NxT.  If T is not high enough, it will be uneconomical for the
system ro provide enough capacity for all services" Scale-out alone is not
enough, each node needs to have good enough performance for the system to be
economical.
* Connection persistence: packets belonging to the same connection should
  always be directed to the same service endpoint.
* Maglev uses consistent hashing and connection tracking.

# 2. System Overview

* Every Google service has one or more VIPs.  A VIP is different from a
  physical IP in that it is not assigned to a specific network interface, but
rather served by multiple service endpoints behind Maglev.  Maglev associates
each VIP with a set of service endpoints and announces it to the router over
BGP; the router in turn announces the VIP to Google's backbone.  Aggregations
of the VIP networks are annoucned to the Internet to make them globally
accessible.
* Maglev handles both IPv4 and IPv6
* When the router receives a VIP packet, it forwards the packet to one of the
  Maglev machines through ECMP, since all Maglev machines announce the VIP
with the same cost.
* Maglev selects an endpoint associated with the VIP, encapsulates the packet
  using GRE with the outerp IP header destined to the endpoint.
* When the packet arrives at the selected service end point it is decapsulated
  and consumed.
* The response uses the source address as the VIP and the destination as the
  originating client.  The response uses Direct Server Return (DSR) to send
responses directly the router so that Maglev does not need to handle return
packets, which are typically larger in size.  DSR is out of scope of this
paper.
* To build clusters at scale, we want to avoid the need to place Maglev
  machines in the same lauer-2 domain as the router, so hardware encapsulators
are deployed behind the router, which tunnel packets from routers to Maglev
machines.

### 2.2 Maglev Configuration

* On each Maglev machine, the controller periodically checks the health status
  of the forwader.  Depending on the results, the controller decides whether
to announce or wihdraw all the VIPs via BGP.  This ensure the router only
forwards packets to healthy Maglev machines.
* Back end pools may contain the physical IP of service endpoints; it may also
  recursively contain other backend pools, so that a frequently-used set of
backends does not need to be specified repeatedly.
* "Sharding can be used for performance isolation and ensuring qos.  Also
  testing new features with interfering with regular traffic."

## 3. Forwarder Design

* Steering module - calculates 5-tuple hash assigns them to different
  receiving queues.
* Each queue is attache dto a packet rewriter thread.i
* Thread reads queue
  - Filters unwanted packets
  - Recomputes 5-type and looks up hash value in the connection tracking
    table.
  - "We do not reuse the hash value from the steering module to avoid cross-thread
synchronization"
  - One connection table per thread to avoid contention
  - Encapsulates packet with GRE/IP
  - Sends it to thread-specific transmission queue 
* Mixing module polls all transmission queues and passes packets to the NIC
* If a receive queue fills up the steering module falls back to round-robin. 

### 3.2 Fast Packet Processing

* Engineered to forward at line rate - typically 10Gbps == 813Kpps for
  1500-byte IP packets
* However, for small packets (100 bytes) the forwarder must process packets at
  9.06Mpps
* Uses ring queue of pointsers to achieve kernel bypass
* Pin threads to a dedicated CPU core for performance

### 3.3 Backend Selection

* Select a backend using a new form of consistent hashing which distributes
  traffic very evenly.
* Record the selection in the local connection tracking table
* Fixed sizes hash table mapping 5-tuple hash values to backends. 
* Router in front of Magleve does not usually provide connetion affinity
* Restart or adding/removing Magleve machines from a cluster makes standard
  ECMP shuffle traffic on a large scale.
* In the above cases Maglev also provides consistent hashing to ensure
  reliable packet delivery.

### 3.4 Consistent Hashing

* DHT would negatively affect forwarding performance
* Consistent hashing or rendezvous hashing introduced in the 1990's
* Consistent hashing and rendezvous prioritize minimal disruption over load
  balancing.  Maglev takes the opposite approach
* Hetereogeneous backend weights can be achieved by altering the relative
  frequency of the backend's turns
* 

## 4. Operational Experience

* Maglev was originally active-passive
* Coordination between active and pasasive machines was complex.
* "We gained a great deal of capacity, efficiency, and operational simplicity
  by moving to an ECMP model."
* Kernel bypass improved performance by a factor of five

### 4.3 Fragment Handling

* Some craziness here about forwarding between Maglevs.  Not sure why
  fragments are needed?
* "In practice only a few VIPs are allowed to receive fragments, and we are
  easily able to provide a big enough fragment table to handle them."

### 4.4 Monitoring and Debugging

* Black box: Periodically check the reachability and latency of the configured
  VIPs
* White box: export vairous metrics via HTTP server.  Monitoring system sends
  alerts when it observees abornmal behaviour.
* Tracer packets: Tells Maglev to send debugging information to a specified
  receiver.  Tracer packets are rate-limited as they are expensive to process.

# 5 Evaluation

* The traffic load exhibts a clear diurnal pattern.
* "The overprovision factor is less than 1.2 over 60% of the time.  It is
  notably higher during off-peak hours because it is harder to balance the
load when there is less traffic."

# 5.2.2 Traffic Type

* Tested using constant 5-tuple - reverts to roudn-robin
* 40Gbps NIC - NIC is no longer the bottleneck

### 5.3 Consistent Hashing

* "Magleve hashing provides almost perfect load balancing no matter what the
  table size is.  When table size is 65537 Karger and Rendezvous require
backends to be overprovisioned by 29.7% amd 49.5% respectively.  The numbers
drop to 10.3% and 12.3% as the table size grows to 655373.
* "Since there is one lookup talbe per VIP, the table size must be limited in
  order to scale the number of VIPs"


