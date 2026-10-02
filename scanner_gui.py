import tkinter as tk
import socket
import threading

window = tk.Tk()
window.title("Network Port Scanner")
window.geometry("600x500")

title_label = tk.Label(window, text="Network Port Scanner")
title_label.pack()
host_label = tk.Label(window, text="Target Host")
host_label.pack()
host_entry = tk.Entry(window)
host_entry.pack()

port_frame = tk.Frame(window)
port_frame.pack()
start_port_label = tk.Label(port_frame, text="Start Port")
start_port_label.grid(row=0, column=0)
start_port_entry = tk.Entry(port_frame)
start_port_entry.grid(row=1, column=0)

End_port_label = tk.Label(port_frame, text="End Port")
End_port_label.grid(row=0, column=1)
End_port_entry = tk.Entry(port_frame)
End_port_entry.grid(row=1, column=1)
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
def start_scan_thread():
    scan_thread = threading.Thread(target=start_scan)
    scan_thread.start()
def start_scan():
    results_text.delete(1.0, tk.END)  # Clear the text area before starting a new scan
    host_name = host_entry.get()
    start_port=int(start_port_entry.get())
    end_port=int(End_port_entry.get())
    for port in range(start_port, end_port + 1):#running loop from start port to end and print the result
        result = check_port(host_name, port)
        results_text.insert(tk.END, f"Port {port}: {result}\n")

scan_button = tk.Button(window, text="Scan", command=start_scan_thread)
scan_button.pack()
results_label = tk.Label(window, text="Results:")
results_label.pack()
results_text = tk.Text(window, height=15, width=60)
results_text.pack()

    


window.mainloop()

