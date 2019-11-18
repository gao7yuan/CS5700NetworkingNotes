# Week 8 Summary

## security
- what
  - **confidentiality**: who *understands* msg content
  - **authentication**: confirm identity of each other
  - **message integrity**: msg not altered without detection
  - **access and availability**: service accessible and available to users
- who needs security
  - web browser and server for electronic transactions (online purchases)
  - online banking client/server
  - DNS servers
- what can bad guys do
  - eavesdrop 窃听
  - impersonation 伪造: fake source address etc. in packet
  - hijacking 拦截
  - denial of service

## principles of cryptography
- language of cryptography
  - `m`: plaintext message
  - `Ka`: encryption key
    - `Ka(m)`: ciphertext
  - `Kb`: decryption key
    - `m = Kb(Ka(m))`
- symmetric key cryptography
  - sender & receiver share same key `Ks`

### symmetric key cryptography
- **monoalphabetic cipher**
  - key space: 26! - 1
- **DES = data encryption standard**
  - 56-bit symmetric key, 64-bit plaintext input
  - block cypher
    - chop into 64-bit blocks
  - how secure: brute force in less in a day :(
  - 3DES: encrypt 3 times with 3 different keys
- **AES = advanced encryption standard**
  - process data in 128-bit blocks
  - 128, 192 or 256-bit keys
  - Brute force decryption taking 1 sec on DES, takes 149 trillion years for AES
- issue with symmetric key: sender & receiver need to know shared key

### asymmetric key cryptography
- public key cryptography
  - sender & receiver don't share same key
  - public key known to all
  - private key only known to receiver
  - **Diffie-Hellman, RSA**
  - `m = Kb-(Kb+(m))`
    - `Kb+`: public key
    - `Kb-`: private key
- **requirements**
  1. need `Kb+` and `Kb-` such that `Kb-(Kb+(m)) = m`
  2. given public key, it should be impossible to compute private key
- modular arithmetic
- RSA
  - msg: bit pattern (sequence of 0's and 1's)
  - bit pattern uniquely represented by integer
  - encrypting an integer number
- RSA - public/private key pair
  1. two large prime numbers `p`, `q`
  2. `n = pq`, `z = (p-1)(q-1)`
  3. `e` (< `n`) with no common factor with `z`
  4. `d` -> `ed - 1` exactly divisible by `z`
  5. public key = `(n, e)`. private key = `(n, d)`.
  - ???wtf
- RSA - encryption and decryption
  0. public key = `(n, e)`. private key = `(n, d)`.
  1. to encrypt `m` (< `n`):
    - `c = m^e mod n`
  2. to decrypt
    - `m = c^d mod n`
  - `m = (m^e mod n)^d mod n`
- RSA - another property
  - `Kb-(Kb+(m)) = m = Kb+(Kb-(m))`
- RSA in practice
  - Use public key crypto to
    - establish secure connection
    - establish symmetric session key for data encryption

## message integrity
- digital signature
  - sender signs document
  - verifiable & non-forgeable
  - sender: `m`, `Kb-(m)`
- message digest
  - use hash function `H`
  - produce fixed-size message digest `x = H(m)`
- poor hash function: internet checksum - easy collision
- good hash functions
  - MD5
    - 128-bit msg digest
  - SHA-1
    - 160-bit msg digest
  - SHA-2, SHA-3
    - good to use
- digital signature == signed msg digest
  - sender: `m` -> (`H`) -> `H(m)` -> (`Kb-`) -> encrypted msg digest `Kb-(H(m))`
  - receiver:
    - `m` -> (`H`) -> `H(m)`
    - `Kb-(H(m))` -> (`Kb+`) -> `H(m)`
    - two should be equal!

## authentication
- AP1.0
  - "I am Alice."
- AP2.0
  - IP + "I am Alice."
- AP3.0
  - IP + password + "I am Alice."
- AP3.1
  - IP + K(password) + "I am Alice."
  - packet can be recorded by Trudy
- AP4.0
  - **nonce**
  - Bob sends Alice `R`
  - Alice returns `R` encrypted with shared secret key
  - requires symmetric key!
- AP5.0
  - **nonce + public key crypto**
  - Alice:
    - Ka-(R)
    - Ka+
  - Trudy can attack in the middle!
- **certification authorities (CA)**
  - CA binds public key to particular entity E
    - i.e. CA's public key + E
  - E register its public key with CA
    - E provides “proof of identity” to CA *(???)*
    - CA creates certificate binding E to its public key
    - Certificate containing E’s public key, digitally signed by CA
  - e.g. Bob's public key `Kb+` encrypted with `Kca-` -> certificate for Bob's public key, signed by CA
  - when Alice wants' Bob's public key
    - gets Bob's certificate
    - apply CA's public key to Bob's certificate
  - **Q: but how does CA verify Bob?**

## securing TCP connection: SSL
- SSL: secure socket layer
  - provides: confidentiality, integrity, authentication
  - variation - TLS: transport layer security
  - available to all TCP app
- SSL and TCP/IP
  - API
- toy SSL
  - handshake: authenticate each other & exchange shared secret
  - key derivation
  - data transfer: broken up into series of records
  - connection closure
- handshake
  - `Kb+(MS) = EMS`
  - master secret & encrypted master secret
- key derivation
  - different keys for message authentication code (MAC) & encryption
  - 4 keys
    - 2 client => server: encryption key + MAC key
    - 2 server => client: encryption key + MAC key
- data records
  - break stream in series of records
  - each record carries a MAC
- SSL cipher suite
  - Public key algorithms
  - Symmetric encryption algorithms
  - MAC algorithm
