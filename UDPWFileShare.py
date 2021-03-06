import os
import socket
from threading import Thread
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

import requests

from server import *

# Setting up window parameters for the GUI
root = Tk()
root.geometry("305x600")
root.resizable(False, False)
root.title("UDP WANDERERS FILE SHARE")

frame = Frame(root)
frame.pack()

# Displaying Host Name

host_name = Label(frame, text="HOST NAME: " + socket.gethostname(), font=("Arial", 13, "bold"), bg="lightblue",
                  fg="darkblue")
host_name.pack(ipadx=80, fill=BOTH)

# Displaying Ip Address
ip_name = Label(frame, text="IP ADDRESS: " + socket.gethostbyname(socket.gethostname()), font=("Arial", 13, "bold"),
                bg="lightblue", fg="darkblue")
ip_name.pack(ipadx=80, fill=BOTH)

# Creating List For File Adding
file_list = Listbox(root, bg="lightgrey", width=20)
file_list.pack(ipadx=90)

# Creating Message Box
note = Label(root, text="Wait Checking Your Connectivity...", bg="black", fg="green", font=("Arial", 10, "bold"))
note.pack(ipadx=150)

# Checking Internet Connection

url = "https://pyprogrammercode.blogspot.com"
timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    note.config(text="Online")

except (requests.ConnectionError, requests.Timeout) as exception:
    note.config(fg="red", text="Offline")
    ip_name.configure(padx=19)


# Add Function to enable adding files to the file list
def add():
    global filename
    filename = filedialog.askopenfilename()
    c = str(filename)
    name = os.path.basename(filename)
    if bool(c) is True:
        box.configure(fg="green")
        file_list.insert(END, name)
        box.insert(END, "File Added Successfully......\n")
    else:
        box.insert(END, "File Not Selected ......\n")


# Remove function enables the removal of files from the list.
def remove():
    file_list.delete(ACTIVE)


# File Sharing
# Function to send files
def rec():
    soc = socket.socket()#socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 5050

    soc.bind((host, port))
    soc.listen()

    messagebox.showinfo(host, "currently waiting")
    conn, addr = soc.accept()
    messagebox.showinfo(addr, "has connected")

    # filename = filedialog.askopenfilename()
    # file = open(filename, 'rb')
    # file_data = file.read(1024)

    filename = simpledialog.askstring("Incoming File", "Please enter a filename for incoming file: ", parent=root)

    file = open(filename, 'wb')
    file_data = conn.recv(1024)

    # while file_data:
    #     conn.send(file_data)
    #     file_data = file.read(1024)
    while file_data:
        file.write(file_data)
        # .decode('utf8')
        file_data = conn.recv(1024)

    file.close()
    messagebox.showinfo("file received")

    soc.close()
    conn.close()


# Receiving File

def send():
    soc = socket.socket()
    newWin = Tk()
    newWin.withdraw()
    host = simpledialog.askstring("Sending File", "Please enter a the receiver address: ", parent=root)
    newWin.destroy()
    port = 5050

    soc.connect((host, port))
    messagebox.showinfo("connecting")

    # filename = simpledialog.askstring("Incoming File", "Please enter a filename for incoming file: ", parent=root)
    # file = open(filename, 'wb')
    # file_data = soc.recv(1024)
    filename = filedialog.askopenfilename()
    file = open(filename, 'rb')
    file_data = file.read(1024)

    # while file_data:
    #     file.write(file_data)
    #     file_data = soc.recv(1024)
    while file_data:
        soc.send(file_data)
        file_data = file.read(1024)

    file.close()
    messagebox.showinfo("file sent")

    soc.close()


# Sending Thread
def Sender():
    send()


# Receiving Thread
def Receiver():
    rec()


# Function to start thread after Share button is clicked.
def clicked():
    Thread(target=Sender).start()


def clicked2():
    Thread(target=Receiver).start()



# frame for Button
frame1 = Frame(root, bg="lightgrey")
frame1.pack()

# Creating Button For Adding and Removing Files #Removing
add = Button(frame1, text="RECEIVE", font=("Arial", 10, "bold"), command=clicked2)
add.grid(row=4, padx=5, ipadx=58, ipady=30)

# remove=Button(frame1,text="REMOVE FILE",font=("Arial",10,"bold"),bg="#fa8e70",command=remove)
# remove.grid(row=4,column=2,ipadx=15,ipady=30)

# remove = Button(frame1, text="REMOVE FILE", font=("Arial", 10, "bold"), command=remove)
# remove.grid(row=4, column=2, ipadx=15, ipady=30)

# Creating Send Button
# share=Button(frame1,text="SHARE",font=("Arial",10,"bold"),bg="lightblue",command=clicked).pack()
share = Button(frame1, text="SHARE", font=("Arial", 10, "bold"), command=clicked)
share.grid(row=5, padx=5, ipadx=60, ipady=30)

# creating Message Box
box = Text(root, font=("Arial"), height=10, width=50, bg="black", fg="green")
box.pack()

root.mainloop()
