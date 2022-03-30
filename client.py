# import socket
#
# soc = socket.socket()
# host = "127.0.0.1"
# port = 5050
# soc.connect((host, port))
# print("connecting")
#
# filename = input("pleas enter a filename for incoming file: ")
#
# file = open(filename, 'wb')
# file_data = soc.recv(1024)
# file.write(file_data)
# file.close()
# print("file received, Yeah it actually worked evan!!!!!!!!")

import socket


def send_file(server, port):

    filename = input("please enter the filename of file to send: ")
    file = open(filename, 'rb')

    file_data = file.read(1024)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.sendto(file_data, (server, port))

    print("file sent")



def recv_file(host2, port2):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    filename = input("pleas enter a filename for incoming file: ")
    file = open(filename, 'wb')
    file_data = client_socket.recv(1024)
    file.write(file_data)
    file.close()
    print("file received")


if __name__ == '__main__':
    # ip = input('Enter IP address:')
    # port = int(input('Enter port: '))
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 5050
    response = ''
    print("connecting")
    while response != 'SHUTDOWN!':
        response = input('type "send" to a file or type "receive" to get your file : ')
        if response == 'send':
            send_file(host, port)
        elif response == 'receive':
            recv_file(host, port)
        else:
            print('invalid message try again')