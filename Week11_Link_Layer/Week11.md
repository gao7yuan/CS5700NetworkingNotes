# Week 11

- multiple access protocols
  - type of link
    - point-to-point
    - broadcast
- ideal multiple access protocol
  - given broadcast channel of rate R bps
  - desired criteria
    - one node transmit at rate R
    - M nodes, each send at avg R/M
    - fully centralized
    - simple
- taxonomy
  - channel partitioning
    - divide channel into smaller pieces by time or freq
  - random access
    - channel not divided, allow collisions
    - recover from collisions
- random access protocols
- slotted ALOHA assumptions
  - all frames same size
  - time divided into equal slots
  - nodes start to transmit only slot beginning
  - synchronized
  - collision centralized
- slotted ALOHA operation
  - if collision, retransmit
- pure ALOHA
- CSMA
  - defer transmission
  - can still collide due to propagation delay
- CSMA/CD
- ethernet CSMA/CD algo
  - exponential backoff
- CSMA/CD efficiency
  - if propagation delay is very small, retransmission won't happen
  - smaller frame size is desired

## LANs
- local area networks
- MAC address
  - locally get frame from one interface to another physically-connected interface (aka same network)
- ARP
  - address resolution protocol
    - IP -> MAC
  - each node maintains ARP table
- packet delivery in the same in the same LAN
  - A -> datagram -> B
  - A checks ARP table using B's IP address
  - A uses B's MAC address to create link layer frame and transmit
  - B's NIC detects this frame has its MAC address as destination -> pick up and deliver to upper layer protocol
- discover MAC address
- packet delivery to another LAN
  - assumptions
    - A knows IP of R
    - A knows MAC address of R
- ethernet
  - dominant wired LAN tech
- physical topology
  - bus
  - star
- ethernet frame structure
- ethernet
  - connectionless
  - unreliable
  - CSMA/CD
  - ethernet only cares about if I sent this without collision
- switch
  - link layer device
    - store and forward ethernet frames
- forwarding
  - fill up the forwarding table
- switch vs router
  - both store and forward
  - both have forwarding table
  - router layer 3: IP
  - switch layer 4: MAC address
- what happens when you search for something in browser on google.com
1. DHCP -> IP
2. broadcast to ARP -> MAC (1111111111...)
3. router DHCP returns network mask, local DNS server
4. url -> DNS -> DNS server (DNS is a) -> uses UDP -> get IP of google.com
5. got IP address -> firstly set up TCP connection (SYN packet)
6. send http request (GET) port 80 application layer protocol
7. TCP encapsulate in IP packet. source, dest = google.com
8. now got dest IP. IP layer packet everything to link layer frame. data frame -> MAC address is **routers MAC address**
9. router forward IP packet to comcast network gateway (?) router
10. BGP from one gateway to another
11. inside Google ISP: intra-AS
