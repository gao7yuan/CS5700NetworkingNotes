# Week 7 Summary

## TCP

- overview
  - point to point
  - reliable, in-order, byte stream, no msg boundary
  - pipelined
  - connection
  - flow control
  - congestion control

## TCP: reliable data transfer
- seq number
  - offset of first byte in byte stream **(?)**
- ack
  - sequence number of next byte expected
  - cumulative
- RTT and timeout
  - timeout value should be longer than RTT
  - safety margin
  - EstimatedRTT and DevRTT
- fast retransmit
  - long delay before resending lost pkt
  - detect lost segments via duplicate ACKs

## TCP: connection management
- setup connection
  - SYN
- close connection
  - FIN
  - respond to received FIN with ACK
    - on receiving FIN, ACK can be combined with its own FIN

## TCP: flow control
- flow control
  - avoid sending data too quickly
  - receiver claims free buffer space by *rwnd* value in header space
  - sender limits data in-flight to *rwnd*
  - guarantees receiver buffer will not overflow

## TCP: congestion control
- congestion control
  - too many resources sending too much data too fast for network to handle
  - observations
    - lost packets (buffer overflow at routers)
    - long delays (queueing in router buffers)
- congestion signs
  - lose a packet
    - timeout
    - duplicate ACKs
- how to control data rate - *cwnd*
  - controls window size
- TCP's approach
  - additive increase
  - multiplicative decrease
- slow start
  - initial cwnd = 1 MSS
  - double cwnd every RTT
  - increase linearly 1 MSS every ACK
- reaction to loss
  - timeout
    - cwnd = 1 MSS
    - slow start to threshold, then increase linearly
  - 3 duplicate ACKs
    1. cwnd cut half then grows linearly
    2. same as timeout
