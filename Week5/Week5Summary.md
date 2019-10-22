# Week 5

## Application Layer

### SMTP
- email
  - three major components
    - user agents
    - mail servers
    - SMTP (simple mail transport protocol)
- SMTP
  - TCP
  - port 25
  - command: ASCII code
  - response: status code and phrase

### DHCP
- DHCP
  - dynamic host configuration protocol
  - dynamically get address from a server
- overview
  - host broadcasts "DHCP discover" message
  - DHCP server responds with "DHCP offer" message
  - host requests IP address with "DHCP request"
  - DHCP sends address with "DHCP ack" message
- *what DHCP returns*
  - ip address
  - network mask
  - name and ip address of local dns server
  - address of first-hop router

## Transport
- transport services and protocols
  - provide logical communication between application processes
  - run in end systems (not the core)
  - more than one
    - tcp and udp
- network layer service model
  - logical communication between hosts
  - packet treated individually
  - **best effort**
### UDP
- udp header
  - source port
  - destination port
  - length
  - checksum
  - each 16 bits
- udp checksum
  - 16-bit int -> add up -> checksum
### reliable data transfer
- sender
  - add sequence number to packets (0 or 1)
  - retransmit if NAK
  - retransmit if ACK/NAK is corrupted
- receiver
  - check if received packet is duplicate (use seq #)
  - send ACK or NAK for each packet
