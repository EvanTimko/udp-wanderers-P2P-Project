
import socket
import pickle


def client_program():
    host = socket.gethostname() 
    port = 50080

    client_socket = socket.socket() 
    client_socket.connect((host, port)) 
    print("type 'quit' to close connection")
    message = input(" -> ") 

    while message.lower().strip() != 'quit':
        message = (message).encode()
        client_socket.send(message)
        data = client_socket.recv(1024)
        data = pickle.loads(data)

        print(data) 

        message = input(" -> ") 

    client_socket.close() 


if __name__ == '__main__':
    client_program()
