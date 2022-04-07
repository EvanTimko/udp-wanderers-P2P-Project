import socket

soc = socket.socket()
host = "127.0.0.1"
port = 5050
soc.bind((host, port))
soc.listen()

print(host)
print("currently waiting")
conn, addr = soc.accept()
print(addr, "has connected")

filename = input("please enter the filename of file: ")
file = open(filename, 'rb')
file_data = file.read(1024)

while file_data:
    conn.send(file_data)
    file_data = file.read(1024)

file.close()
print("file sent")

soc.close()
conn.close()
