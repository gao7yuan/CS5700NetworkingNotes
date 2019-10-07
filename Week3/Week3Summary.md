# transport layer service model
- **TCP service model** quiz2
  - *reliable* data transfer
    - no loss, in order
  - *flow control*: sender won't overwhelm receiver
  - *congestion control*: throttle sender when network is overloaded
  - *connection oriented*: setup required between client and server
- UDP
  - unreliable data transfer
    - loss, out-of-order, duplicate

# DNS - domain name system
- DNS
  - at application layer
  - human-readable names -> IP address
  - distributed database
- names
  - rightmost segment: top-level domain (TLD)
- *root name servers*
  - provide which TLD name server to ask next
- *TLD name servers*
  - responsible for com, org, edu, ..., and all top level country domains
  - provide which authoritative name server to ask next
- *authoritative name servers*
  - organization's own name servers
  - provide authoritative hostname to IP mappings for organization's named hosts
- DNS - *local name server*
  - does not belong to hierarchy
  - proxy
- DNS - caching
  - time out after TTL
- DNS records
  - type A: hostname -> IP address
  - type NS: domain -> hostname of authoritative name server for this domain
  - type CNAME: alias for "canonical" name -> canonical name
  - type MX: name -> mail server