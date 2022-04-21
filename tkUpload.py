import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile

my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window
my_w.title('www.plus2net.com')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Upload File & read', width=30, font=my_font1)
l1.grid(row=1, column=1)
b1 = tk.Button(my_w, text='Upload File',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1)

my_str = tk.StringVar()
l2 = tk.Label(my_w,textvariable=my_str,fg='red' )
l2.grid(row=3,column=1)
my_str.set("")
def upload_file():
    f_types = [('All Files', '*.*'),
               ('Python Files', '*.py'),
               ('Text Document', '*.txt'),
               ('CSV files', "*.csv"),
               ('PDF Files', "*.pdf"),
               ('PNG image', "*.png"),
               ('JPEG', "*.jpeg")
               ]
    file = filedialog.askopenfilename(
        filetypes=f_types)


    if(file):
        my_str.set(file)
        fob=open(file,'r')
        print(fob.read())

    
    else: # user cancel the file browser window
        print("No file chosen")



my_w.mainloop()  # Keep the window open
