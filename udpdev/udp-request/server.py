
import socket
import DataFiles
import pickle

def server_program():

    host = socket.gethostname()
    port = 50080

    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:

        data2 = conn.recv(1024).decode()
        if not data2:
            
            break
        print("from connected user: " + str(data2))


        
        data = open("INFORMATION", "rt")
        if data == None:
            print("""Error "INFORMATION" file is Not found in directory""")
        dfList = DataFiles.doublyLinkedList()
        information = data.readline().split(',', 3)
        dfList.insertToEmptyList(information[0], information[1], information[2])

        for x in data:
            information = x.split(',', 3)
            dfList.insertToEnd(information[0], information[1], information[2])
        info = pickle.dumps(information)
        conn.send(info) 
        
        # message = input(" -> ") 
        # server_socket.send(message.encode())

    
    conn.close() 


if __name__ == '__main__':
    server_program()
