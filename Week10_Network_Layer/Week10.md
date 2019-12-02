# Week 10

- intra-AS routing
  - Interior Gateway Protocols (IGP)
  - most common intra-AS routing protocols
    - RIP: routing info protocol
      - based on distance vector
    - OSPF: open shortest path first
      - based on link state
    - EIGRP: enhanced interior gateway routing protocol
      - proprietary protocol by Cisco

- inter-AS routing
  - BGP: border gateway protocol

- policy-based routing

- when you are singly-homed, you don't need to run BGP.

## SDN - software defined networking
- internet network layer

## Link Layer
- overview
  - transfer datagram from one node to physically adjacent node over a link (directly connected)
  - for network layer the hosts do not have to be directly connected
- link layer services
  - framing, link access
    - encapsulate datagram into frame
    - MAC address -> source & destination
      - why?
      - **no hierarchy in MAC address, hard to scale**
  - reliable delivery between adjacent nodes
- error detection
