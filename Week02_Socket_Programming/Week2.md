# Week2
9/16/19

## Socket Programming
- Socket
  - Door (aka API) between application process and transport protocol
  - Process sends/receives data to/from its socket
- Communication paradigms
  1. Stream paradigm
    - sequence of bytes
    - used by most applications
    - built on **TCP** protocol
  2. Message paradigm
    - sequence of individual messages
    - built on **UDP** protocol
  - two transport layer protocols: TCP && UDP
- Stream paradigm
  - transfer a sequence of bytes
  - connected oriented
  - 1-1 communication (between 2 applications)
  - bidirectional
  - No meaning attached to data
  - No boundaries inserted in data
  - Reliable
- Message paradigm
  - If N bytes in a msg, receiver will find exactly N bytes in incoming msg
    - Boundary
  - Connectionless
  - Unicast, multicast, broadcast
  - *Unreliable (lost, duplicated, out of order)*
- Socket (or socket API)
  - Originally part of BSD Unix -> industry standard
  - Almost every OS has an implementation
  - Two socket types
    - SOCK_STREAM
      - reliable, byte stream-oriented, based on TCP
    - SOCK_DGRAM
      - unreliable datagram, UDP
- Socket[TCP]
  - reliable, in-order, byte-stream: client - server application processes
  - connection oriented
  - 1-1
  - identify an application process
    - address a machine (IP address)
      - IP protocol v4, v6
    - address a process (port number)
- IP address
  - layer 3 logical address assigned by admin
    - unique
    - for routing packets
    - dynamic
  - Hierarchical addressing structure
    - network and host portion
- Address classes
  - A, B, C
    - Internet Assigned Numbers Authority (IANA)
  - D: multicast - scalable
  - E
- class A IPv4
  - 32 bits
  - 8 for network (first bit 0), 24 for host
  - 2^7 = 128, 2^24 = 16 million
- class B IPv4
  - 32 bits
  - 16 for network (first 2 bits 10), 16 for host
  - 2^14, 2^16 = 65536
- class C IPv4
  - 24, 8
  - 2^21 = 2 million, 2^8 = 256
- class D
  - multicast
  - start with 1110
  - 224.0.0.0 -> 239.255.255.255
- Network mask
  - used to determine network and host portion
  - networks
    - mask bits set to 1
  - host
    - mask bits set to 0
  - A: 255.0.0.0
  - B: 255.255.0.0
  - C: 255.255.255.0
- CIDR
  - classless inter domain routing
  - replace classful
  - /X notation: number of 1s in network mask
    - e.g. 10.1.1.1/8
- directed broadcast addresses
  - 1s in the entire host portion
- local broadcast addresses
  - all 1s
- local loopback addresses
  - send a msg to itself for testing
  - canonical loopback address: 127.0.0.1
    - any of 127.x.x.x
    - huge waste
- private address
  - non routable on the internet
- Port number
  - identify application process within a host
  - 16-bit integer
  - well-known ports
    - DNS(53), HTTP(80)
    - TCP: cannot have two application processes that claim the same port. (UDP can)
**Network portion is used for routing!!!**
- Socket: a set of APIs

## Jupytor Notebook Demo
- bits and endianness
- string vs bytes in Python 3
  - utf-8 most common way for unicode encoding
  - need to encode string to bytes, then decode
  - also need to consider endianness
- struct package
```python
import struct

## use pack to pack things you want to send into sequence of bytes
struct.pack(fmt, v1, v2, ...)
struct.unpack(fmt, buffer)
```

- blocking call
  - accepting no msg, put thread to sleep
