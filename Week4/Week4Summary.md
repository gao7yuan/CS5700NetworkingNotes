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
