import socket 
import threading
host_name=input("Enter the host name to check:")
ip_address=socket.gethostbyname(host_name)
print("IP address of", host_name, "is", ip_address)
port_start=int(input("Enter the starting port number:"))
port_end=int(input("Enter the ending port number:"))    
def check_port(host_name,port):#function that will take the host name and port and check the conncection
        s=socket.socket()
        s.settimeout(2)
        try:
            s.connect((host_name,port))
            return "OPEN"#wanted the output in the return form so the gui will work properly rather than just printing it on the terminal
        except socket.timeout:
             return "TIMEOUT"
        except ConnectionRefusedError:
             return "CLOSED"
        except OSError:
             return "ERROR"
        finally:
             s.close()
results={}
def scan_ports(host_name, port):
     result = check_port(host_name, port)
     results[port] = result
     
threads =[]
for port in range(port_start, port_end + 1):#running loop from start port to end and print the result
 thread = threading.Thread(target=scan_ports, args=(host_name,port))
 threads.append(thread)
 thread.start()


for thread in threads:
    thread.join()
for port, result in results.items():
    print("Port", port, ":", result)