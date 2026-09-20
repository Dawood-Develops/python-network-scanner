import socket 
def check_port(port):
    s=socket.socket()
    s.settimeout(2)
    try:
        s.connect(("www.example.com",port))
        print("port",port, "opened")
    except:
        print("port",port, "not opened")

check_port(80)
check_port(443)
