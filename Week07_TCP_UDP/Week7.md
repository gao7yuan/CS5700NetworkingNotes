# Week 7

## TCP

- TCP overview
  - flow control: end-to-end
  - congestion control: network overall
- TCP segment structure
  - *header length* - overhead: 20 bytes

## TCP: reliable data transfer
- sequence number
  - offset of the first byte in byte stream **(why good?)**
- ACK
  - sequence number of next byte expected
  - cumulative
  - why:
    1. save traffic
    2. acknowledge that previous packets are received
- timer
  - ?
- RTT and timeout
  - timeout value should be longer than RTT
  - too short: premature timeout, unnecessary retransmission
  - too long: slow reaction to data loss
- how to estimate RTT?
  - [20, 15, 25, 20, 18]
  - option1:
    - estimate = (20+15+25+20+18)/5
  - option2:
    - take most recent one?
    - estimate = 18
    - may have outlier
  - option3:
    - exponential weighted moving average
    - estimate = 18 * 1/2 + 20 * (1/2)^2 + 25 * (1/2)^3 + 15 * (1/2)^4 + 20 * (1/2)^5
- now estimate variance
  - use exponential weighted moving average
- fast retransmit
  - detect lost segments via duplicate ACKs

## TCP: connection management
- setup connection

## TCP: flow control

## TCP: congestion control
- cwnd
  - cwnd controls window size

## Security
- cryptography
  - symmetric key cryptography
  
