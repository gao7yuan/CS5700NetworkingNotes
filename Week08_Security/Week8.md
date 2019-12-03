# Week8

## Network Security
- cryptography
  - symmetric key
    - sender and receiver share the same secret (key)
  - asymmetric
- monoalphabetic cipher

## Confidentiality
### Symmetric Key Algo
- DES
  - data encryption standard
  - 56-bit symmetric key, 64-bit plaintext input
  - block cypher
    - chop into 64-bit blocks
  - how secure
    - key space: 2^56
    - brute force in less than a day
    - no known good analytic attack
      - no frequency information
  - make DES more secure
    - 3DES: encrypt 3 times with 3 different keys
- AES
  - advanced encryption standard
    - replaced DES
  - process data in 128-bit blocks (block cypher)
  - 128, 192, 256 bit keys
  - brute force decryption taking 1 sec on DES, 149 trillion years for AES
- one issue with symmetric key cryptography
  - sender and receiver need to know shared secret key

### Asymmetric Key Algo
- public key cryptography (asymmetric)
  - don't share same key
  - public key known to all
  - private key only known to receiver
- requirements
  - need `kb+` and `kb-` such that `kb-(kb+(m)) = m`
  - given public key `kb+`, should be impossible to compute private key `kb-`
- modular arithmetic
  - x mod n = remainder of x when divided by n
- RSA
  - msg: just a bit pattern
  - bit pattern can be uniquely represented by an integer
  - encrypting an integer
- RSA - public/private key pair
  1. choose two large prime numbers p, q (e.g. 1024 bits each)
  2. compute n = pq, z = (p-1)(q-1)
  3. choose e (with e < n) that has no common factors with z (e, z are "relatively prime")
  4. choose d such that ed - 1 is divisible by z
  5. public key is (n, e). private key is (n, d)
- RSA - encryption and decryption
  0. given (n, e) and (n, d) as computed above
  1. to encrypt msg m (< n), compute
    - c = m^e mod n
  2. to decrypt received bit ???
- RSA - another important property
  - reverse kb+ and kb- does not make a difference
- RSA - why secure
- RSA in practice

## Message Integrity
- digital signature
  - analogous to hand-written signatures
- message digest
  - use hash function
- poor hash function - internet checksum
- good hash functions
  - MD5
  - SHA-1
  - SHA-2, SHA-3
    - good to use
- digital signature = signed message digest

## Authentication
- AP 1.0
  - prove identity
  - someone else wants to fake identity
- AP 2.0
  - IP address
  - easy to fake
- AP 3.0
  - secret password
  - bad idea to show password
- AP 3.1
  - password encrypted
  - record packet and later plays it back
- AP 4.0
  - avoid playback attack
  - **nonce**: number R used only once-in-a-lifetime
  - requires shared symmetric key
- AP 5.0
  - nonce + public key cryptography
  - not secure
- Certification authorities (CA)

## Securing TCP connection: SSL
- SSL: secure socket layer
- TLS
- SSL and TCP/IP
  - SSL provides application programming interface (API)
- Toy SSL
  - handshake
  - key derivation
  - data transfer
  - connection closure
