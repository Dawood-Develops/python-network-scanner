import socket 
def check_port(port):
        s=socket.socket()
        s.settimeout(2)
        try:
            s.connect(("www.example.com",port))
            print("port",port, "opened")
        except:
            print("port",port, "not opened")
ports =[22,80,443,53]
for port in ports:
  check_port(port)
