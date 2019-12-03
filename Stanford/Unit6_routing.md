# Unit 6 Routing

## 0. Routing
### Q1: how to get pkt from A to B across large network
- forward and route
- to start
  - packet contains list of routers to pass through (state)
  - **source routing**
  - inefficient & security loophole
- internet uses forwarding table
  - each router
  - for each destination prefix, which next hop to send pkt to
### Q2: how do forwarding tables get populated
- distributed algorithm
- routers build a spanning tree
  - no loop
  - root = destination, leaves are other sources
  - Bellman Ford (distance vector)
  - Dijkstra's algo (link state)
### Autonomous System
- administrative domain of routing within internet
- **within an autonomous system: two basic algos**
  - RIP - distance vector
  - OSPF - link state (people use this one mostly)
- **between autonomous systems: BGP**
  - AS hide internal

## 1. Flooding, source routing and spanning trees
- flooding
  - every pkt will be delivered at least once at the leave
  - maybe loop
  - inefficient
  - use ttl or hop count to stop looping forever
  - simple
    - no state in routers
    - A does not need to know about topology
    - no forwarding tables
  - **used when end host knows nothing about network**
- source routing
  - A knows topology and ordering
  - no forwarding tables
  - pkt carries too many addresses
  - **used when end host wants to control route**
- forwarding table
  - state: destination address -> next hop
  - network takes on the function to optimize it
- spanning tree
- metric
  - choices
    - min distance
    - min hop count
    - min delay
    - max throughput
    - least loaded path
    - most reliable path
    - lowest cost path
    - most secure path
    - ...
- annotated graph
  - node, edge, cost
  - min cost spanning tree
- other types of routing
  - multipath
    - some links could be popular
    - load balancing
  - multicast
    - vs. unicast
    - a host send pkts to a set of hosts
## 2. Bellman Ford
- min cost spanning tree to R8
  - Ri maintains value cost Ci to reach R8
  - vector C = (C1, C2, ..., C7) is the distance vector to R8
  - initially C = (all infinity)
  1. after T seconds, Ri sends Ci to neighbors
  2. if Ri learns lower cost path, update Ci
  3. repeat
- runtime
  - longest loop free path
- problem
  - bad news travels slowly
- fix
  - set infinity = "some small integer" (e.g. 16)
    - stop when count = 16
  - split horizon
    - does not advertise to where it receives from
  - split horizon with poison reverse
    - advertise infinity to where it receives from
## 3. Dijkstra
