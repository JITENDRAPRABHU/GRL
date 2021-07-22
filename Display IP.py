#importing modules
from subprocess import check_output
import os
from tkinter import * 
from tkinter import messagebox

#class name-Ip
class Ip:
     #Constructor     
     def __init__(self,cmd_out_list=[]): 
          process = check_output('ipconfig').decode('utf-8')
          print(process)
          self.cmd_out_list=process.split('\n')
          
     #show method to display IP address as popup message
     def show(self):
          op=[]
          for each_line in self.cmd_out_list:
               if("IPv4 Address" in each_line):
                    t=each_line.replace("\r","")
                    t=t.split(":")
                    op.append(t[1])

               if("Link-local IPv6 Address" in each_line):
                    t=each_line.replace("\r","")
                    t=t.split(":",1)
                    op.append(str(t[1]))
          root = Tk()
          root.withdraw()
          res=''  
          for i in range(len(op)):
               if(i==0):
                    res+="Link-local IPv6 Address : "+op[i]+"\n"
               else:
                    res+="IPv4 Address : "+op[i]+"\n"
          messagebox.showinfo("IP ADDRESS: ", res)

if __name__=="__main__":
     global cmd_out_list
     cmd_out_list=[]
     #object creation
     IP1=Ip(cmd_out_list)
     #function call
     IP1.show()

