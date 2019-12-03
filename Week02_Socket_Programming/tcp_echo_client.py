# This example is using Python 3.
import socket

# Specify server name and port number to connect to.
#
# API: getfqdn()
#   returns a fully qualified domain name.
server_name = socket.getfqdn()
print('Hostname: ', server_name)
server_port = 8181

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

# Connect to server machine and port.
#
# API: connect(address)
#   connect to a remote socket at the given address.
s.connect((server_name, server_port))
print('Connected to server ', server_name)

# messages to send to server.
message = ['Hello network world', 'This is Zhifeng']

# Send messages to server over socket.
#
# API: send(bytes)
#   Sends data to the connected remote socket.  Returns the number of
#   bytes sent. Applications are responsible for checking that all
#   data has been sent
#
# API: recv(bufsize)
#   Receive data from the socket. The return value is a bytes object
#   representing the data received. The maximum amount of data to be
#   received at once is specified by 'bufsize'.
#
# API: sendall(bytes)
#   Sends data to the connected remote socket.  This method continues
#   to send data from string until either all data has been sent or an
#   error occurs.
bufsize = 1024
for line in message:
  s.sendall(str.encode(line, 'utf-8'))
  data = s.recv(bufsize)
  print('Client received: ', data)

# Close socket to send EOF to server.
s.close()