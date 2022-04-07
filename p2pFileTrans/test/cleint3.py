import socket

soc = socket.socket()
host = "127.0.0.1"
port = 5050

soc.connect((host, port))
print("connecting")

filename = input("pleas enter a filename for incoming file: ")
file = open(filename, 'wb')
file_data = soc.recv(1024)

while file_data:
    file.write(file_data)
    file_data = soc.recv(1024)

file.close()
print("file received")

soc.close()
