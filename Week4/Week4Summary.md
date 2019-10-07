# web and http
- web page
  - objects
  - each object accessible by url
    - hostname/pathname

# http
- overview
  - client: browser
  - server: web server
  - **TCP**
  - servers use port 80
  - stateless: server maintains no info about past client requests
- http connections
  - non-persistent
  - persistent
    - multiple object sent over one single TCP connection
- http response time
  - RTT
- http request message
  - ASCII (human-readable)
- http response message
  - status code
    - 200 OK
    - 301 Moved Permanently
    - 400 Bad Request
    - 404 Not Found
    - 505 HTTP Version Not Supported

# cookies
- cookies
  - cookie header line of HTTP response msg
  - cookie header line in next HTTP request msg
  - cookie file kept on user's host, managed by user's browser
  - backend db at server side

# web proxy server
- proxy
  - goal: satisfy client request without involving origin server
  - browser sends all http requests to proxy
    - hit
    - miss - request from origin server
  - act as **both client and server**
  - installed by ISP
- benefits
  - reduce response time
  - reduce traffic to org's access link
  - better UX and save $$$
- conditional GET
  - 304 Not Modified

# CDN
- single web server
  - single point of failure
  - easier to be overloaded
  - long latency
- ISP proxy caching
  - pros
    - reduce latency
  - cons
    - security/authentication
    - find grained control when and where
    - cold start
- CDN - content delivery networks
  - content providers contract with CDN companies
  - CDN companies have service in a lot of networks
  - better coordination with replicas
  - proactively content replication on edge servers
  - win-win for both ISP and content providers
