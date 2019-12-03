# Week 1
9/9/19

- Internet
  - largest distributed system
- Protocols

## Introduction
- What is the Internet
  - components
    - hosts: running network applications
    - communication links: fiber, copper, radio
    - packet switches: routers and switches (core part of network)
      - routers vs. switches?
  - structure
    - network edge
      - all users!
      - hosts: clients & servers
      - access network (for connecting hosts to core internet)
    - network core
      - interconnected routers: have single job of delivering packets
      - network of networks
- network edge - access network (CentryLink, Comcast)
  - connect end systems to edge router
  - *frequency division multiplexing*
  - info via phone lines: (think about physical media)
    - sampling of frequency of human voice
      - **0-4kHz** -> like talking to someone else
      - -> 64 kbps (kilo bits per second) *Data rate == Bandwidth*
        - how quickly you can push data on physical media
        - this rate OK for text, but not good for multimedia
      - **0-500kHz** -> separate communication of internet data from phone data
        - for internet data using higher frequency
        - This technique: **frequency division multiplexing**
    - higher frequency range: can carry more signals of different frequency range at the same time -> higher data rate == *bandwidth*
    - signal to noice ratio = S/N -> the higher the better <- how well insulated the media is
  - modem: digital (0, 1) to analog (magnetic waves, sin waves)
- network core
  - routers: one job - sending packets *use full capacity* *no FDM*
  - packet switching
    1. large data into smaller packets
    2. store and forward
    3. no resource reservation or sharing
    - each router store and forward
    - end-to-end delay *transmission delay* - due to physical reasons
    - queueing and packet loss
    - arrival rate (bits) exceeds outgoing rate
      - out of room, drop packets
      - even if no loss, it introduces additional delay
      - *queueing delay* -> *digital loss*
    - two key functions in each router
      - routing: routing algorithm populating forwarding table (essentially key-value pair)
      - forwarding: packets from router's input port to output port
    - phone: **circuit switching** (FDM)
    - network researchers: users' pattern bursty. should not waste resources -> packet switching
- Internet structure
  - ISP
  - connect each access ISP -> do not scale O(N^2)
  - connect each access ISP to a global transit ISP (physical distance?)
  - peering link
- Protocol
  - each protocol specifies how to handle one aspect of communication
  - 5-layer reference model
- Key metrics
  - delay (aka latency)
    - processing delay
      - router
        1. determine where to forward
        2. look up the forwarding destination
        3. copy the packet into the queue
    - transmission delay
    - propagation delay
    - queuing delay
      - La: total bits
    - transmission delay vs. propagation delay
      - transmission delay
        - L/R (packet length / link data rate)
        - Mbps (bits, not bytes)
      - propagation delay
        - d/s (length of physical link / propagation speed)
  - throughput
    - rate (bits / time unit) at which bits transferred between sender and receivers
  - loss
iperf
