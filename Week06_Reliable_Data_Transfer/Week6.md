# Week6
10/21/19

- concurrency
- use synchronization
  - lock

## reliable data transfer
- rdt2.2: NAK-free protocol
  - NAK: receiver sends ACK for last packet
- rdt3.0: channel with errors and loss
  - underlying channel can also lose packets (data or ACK)
  - need timeout
  - in case of NAK: use timeout algo (in some cases avoid double traffic in case of delayed ACK)
- rdt3.0: performance
  - inefficient: one packet at a time
- pipelined protocols
  - sender allows multiple "in-flight" (yet-to-be-acked) pkts
  - what needs to be changed
    - sequence number: 2 -> n
    - ACK: semantics
- pipelined protocols: GBN
  - Go-Back-N
  - sender can have up to N un-ACKed packets
  - receiver only sends cumulative ACK (everything up to packet number #)
  - sender has timer for oldest un-ACKed packet
- pipelined protocols: SR
  - Selective-Repeat
  - sender can have up to N un-ACKed packets
  - receiver sends individual ACK for each packet
- SR
  - buffer pkts
  - if sequence number range is not large enough compared with buffer size, problems arise
    - *solution: sequence number is twice the window size*
