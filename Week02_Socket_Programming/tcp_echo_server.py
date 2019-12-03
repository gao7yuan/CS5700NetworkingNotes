# This example is using Python 3.
import socket

# Get host name, IP address, and port number.
#
# API: getfqdn()
#   returns a fully qualified domain name.
host_name = socket.getfqdn()
print('hostname is', host_name)
# API: gethostbyname(hostname)
#   translate a host name to IPv4 address format, and return it as a
#   string.
host_ip = socket.gethostbyname(host_name)
print('host IP address is', host_ip)
host_port = 8181

# Make a TCP socket object.
#
# API: socket(address_family, socket_type)
#
# Address family
#   AF_INET: IPv4
#   AF_INET6: IPv6
#
# Socket type
#   SOCK_STREAM: TCP socket
#   SOCK_DGRAM: UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to server IP and port number.
#
# API: bind(address)
#   Bind the socke to address. The socket must not already be bound.
s.bind((host_ip, host_port))

# Start listen to incoming requests.
#
# API: listen()
#   Listen for connections made to the socket.
s.listen()
print('Server started. Waiting for connection...')

# Listen until process is killed.
#
# API: accept()
#   Accept an incoming connection. The return value
#   is a pair (conn, address) where conn is a new socket
#   object usable to send and receive data on the
#   connection, and address is the address bound to the
#   socket on the other end of the connection.
bufsize = 1024
while True:
    # Wait for next client connect.
    conn, addr = s.accept()
    print('Server connected by', addr)

    # Read next line on client socket. Send a reply line to the client
    # until EOF when socket closed.
    while True:
        # API: recv(bufsize)
        #   Receive data from the socket. The return value is a bytes
        #   object representing the data received. The maximum amount of
        #   data to be received at once is specified by 'bufsize'.
        data = conn.recv(bufsize)
        if not data: break
        print('Server received:', data)
        conn.sendall(str.encode('Echo => ') + data)
        # Close TCP connection.
    conn.close()
    print('Server finished talking with', addr)