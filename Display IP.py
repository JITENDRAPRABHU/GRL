#importing module 
import socket
import os
from tkinter import * 
from tkinter import messagebox

#function to run ipconfig cmd
def mycmd():
    os.system('cmd /c "ipconfig"')

#function to get ip_address
def get_ip():
    Host_name=socket.gethostname()
    ip_add=socket.gethostbyname(Host_name)
    return ip_add

#function to display ip_address as popup msg
def popup(ip_add):
    root = Tk()
    root.withdraw()
    messagebox.showinfo("IP ADDRESS: ", ip_add)

if __name__=="__main__":
    global ip_add
    mycmd()
    ip_add=get_ip()
    popup(ip_add)
