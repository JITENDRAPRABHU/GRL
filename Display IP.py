#importing module
from subprocess import check_output
import os
from tkinter import * 
from tkinter import messagebox

#running ipconfig cmd
process = check_output('ipconfig').decode('utf-8')
print(process)
cmd_out_list = process.split('\n')
op=[]

#iterating the output
for each_line in cmd_out_list:
     #print(each_line.split(':')[0])
     #condition to check required IP address
     if("IPv4 Address" in each_line):
          t=each_line.replace("\r","")
          t=t.split(":")
          op.append(t[1])

          #print(op)
     if("Link-local IPv6 Address" in each_line):
          t=each_line.replace("\r","")
          t=t.split(":",1)
          op.append(str(t[1]))
    
#function-calling tkinter
root = Tk()
root.withdraw()
res=''
#joining address in string
for i in range(len(op)):
     if(i==0):
          res+="Link-local IPv6 Address : "+op[i]+"\n"
     else:
          res+="IPv4 Address : "+op[i]+"\n"
     
#displaying popup message
messagebox.showinfo("IP ADDRESS: ", res)
