#importing module 
import socket
#getting host name and storing it in a variable
Host_name=socket.gethostname()
#getting the host Ip address by passing hostname in gethostbyname() method and displaying ip address
print ("Ip Address:",socket.gethostbyname(Host_name))
