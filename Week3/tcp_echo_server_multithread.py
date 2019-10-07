import socket
import threading
import time

host_name = socket.getfqdn()
print('hostname is', host_name)

host_ip = socket.gethostbyname(host_name)
print('host IP address is', host_ip)

host_port = 8181

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host_ip, host_port))
s.listen()
print('Server started. Waiting for connection...')

def now():
    return time.ctime(time.time())

bufsize = 1024
def handler(conn, addr):
    while True:
        data = conn.recv(bufsize)
        if not data: break
        print('Server received:', data, 'from', addr)
        conn.sendall(str.encode('Echo ==> ') + data)
        time.sleep(10)  # simulating long running program
    conn.close()

# main thread
while True:
    conn, addr = s.accept()
    print('Server connected by', addr, 'at', now())
    threading.Thread(target=handler, args=(conn, addr)).start()