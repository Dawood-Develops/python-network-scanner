import socket 
host_name=input("Enter the host name to check:")
ip_address=socket.gethostbyname(host_name)
print("IP address of", host_name, "is", ip_address)
port_start=int(input("Enter the starting port number:"))
port_end=int(input("Enter the ending port number:"))    
def check_port(port):
        s=socket.socket()
        s.settimeout(2)
        try:
            s.connect((host_name,port))
            print("port",port, "opened")
        except socket.timeout:
             print("port",port, "timeout")
        except s.connectionRefusedError:
             print("port",port, "closed")
        
            
        
        s.close()
for port in range(port_start, port_end + 1):
  check_port(port)
