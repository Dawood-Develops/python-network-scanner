import socket
import threading
import time   
try:
    host_name=input("Enter the host name to check:")
    ip_address=socket.gethostbyname(host_name)
    print("IP address of", host_name, "is", ip_address)
except socket.gaierror:
    print("Unable to resolve host name. Please check the host name and try again.")
    exit()  
port_start=int(input("Enter the starting port number:"))
port_end=int(input("Enter the ending port number:"))   


def grab_banner(host_name,port):
     s=socket.socket()
     try:
         s.settimeout(2)
         s.connect((host_name,port))
         data=s.recv(1024)
         banner=data.decode(errors='ignore')
     except socket.timeout:
         banner="Unable to grab banner"
     except OSError:
         banner="Unable to grab banner"
     finally:
         s.close()
     return banner 
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
# thread = threading.Thread(target=check_port, args=(host_name,port))
def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except OSError:
        return "Unknown Service"       
threads =[]
start_time = time.time()
for port in range(port_start, port_end + 1):#running loop from start port to end and print the result
#   result = check_port(host_name, port)
#   print("Port",port,":",result)
 thread = threading.Thread(target=scan_ports, args=(host_name,port))
 threads.append(thread)
 thread.start()


for thread in threads:
    thread.join()
end_time = time.time()
for port, result in sorted(results.items()):
     if result == "OPEN":
          service_name = get_service_name(port)
          banner=grab_banner(host_name,port)
          print("Port", port, ":", result, "(", service_name, ")")
          print("Banner for port", port, ":", banner)
     else:
          print("Port", port, ":", result)

scan_time = end_time - start_time
print("Scanning completed in", round(scan_time, 2), "seconds")
