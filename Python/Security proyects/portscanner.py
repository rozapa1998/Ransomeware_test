import socket

ip = input("Enter IP to scan: ")

for port in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    res = sock.connect_ex((ip, port))

    if res == 0:
        print("Open port: " + str(port))
    else:
        print("Closed port: " + str(port))