import socket
import DataFiles
def server_program():
    host = socket.gethostname()
    port = 50097
    server_socket = socket.socket() 
    server_socket.bind((host, port))  

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    data = open("INFORMATION", "rt")
    if data == None:
        print("""Error "INFORMATION" file is Not found in directory""")
    dfList = DataFiles.doublyLinkedList()
    information = data.readline().split(',', 3)
    dfList.insertToEmptyList(information[0], information[1], information[2])
    for x in data:
        information = x.split(',', 3)
        dfList.insertToEnd(information[0], information[1], information[2])
    while True:
        clientMsg = conn.recv(1024).decode()
        if not clientMsg:
            break
        if clientMsg == "req":
            print("from connected user: " + str(clientMsg))
            n = dfList.start_node
            while n is not None:
                string_file = str(n.fileName + "," + n.IP + "," + n.portNum)
                conn.send(bytes(string_file, encoding="utf-8"))
                n = n.next
            if n is None:
                conn.send(bytes("\n", encoding="utf-8"))
                conn.send(bytes("DONE", encoding="utf-8"))

        def pass1():
        # for x in data:
            #after 3 req, server sends filenames 2-8 (still missing first file name)
            # information = x.split(',', 3)
            # x = bytes(x, encoding="utf-8")
            # conn.send(x)
        pass
    conn.close() 
if __name__ == '__main__':
    server_program()
