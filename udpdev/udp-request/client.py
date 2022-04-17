import socket

def client_program():
    host = socket.gethostname() 
    port = 50097

    client_socket = socket.socket() 
    client_socket.connect((host, port)) 
    print("type 'quit' to close connection")

    message = input(" -> ") 
    data = None

    while message.lower().strip() != 'quit':
        message = (message).encode()
        client_socket.send(message)
        # data = client_socket.recv(1024).decode('utf8')
        # data = pickle.loads(data)
        # print(data) 
        print("HI")
        while data != "DONE":
            data = client_socket.recv(1024).decode('utf8')
            print(data)
        print("HEY TOO")
        message = input(" -> ") 

    print("GOODBYE")
    client_socket.close() 


if __name__ == '__main__':
    client_program()
