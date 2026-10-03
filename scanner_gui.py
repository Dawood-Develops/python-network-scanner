import tkinter as tk
import socket
import threading

window = tk.Tk()
window.title("Network Port Scanner")
window.geometry("600x500")
window.configure(bg="#0d1117")

title_label = tk.Label(window, text=" Dawood Network Port Scanner" , font=("Arial", 22, "bold"), fg="white", bg="#0d1117") 
title_label.pack(pady=20)
host_label = tk.Label(window, text="Target Host", fg="white", bg="#0d1117")
host_label.pack(pady=5)
host_entry = tk.Entry(
    window,
    width=35,
    fg="white",
    bg="#0d1117",
    insertbackground="white"
)
host_entry.pack(pady=5)

port_frame = tk.Frame(window, bg="#0d1117")
port_frame.pack()
start_port_label = tk.Label(port_frame, text="Start Port", fg="white", bg="#0d1117")
start_port_label.grid(row=0, column=0 , padx=10)
start_port_entry = tk.Entry(
    port_frame,
    width=15,
    fg="white",
    bg="#0d1117",
    insertbackground="white"
)
start_port_entry.grid(row=1, column=0)

End_port_label = tk.Label(port_frame, text="End Port" , fg="white", bg="#0d1117")
End_port_label.grid(row=0, column=1 , padx=10)
End_port_entry = tk.Entry( port_frame,
    width=15,
    fg="white",
    bg="#0d1117",
    insertbackground="white")
End_port_entry.grid(row=1, column=1, padx=10)
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
    results_text.delete(1.0, tk.END)
    scan_thread = threading.Thread(target=start_scan)
    scan_thread.start()
def show_result(port, result):
      
     results_text.insert(tk.END, f"Port {port}: {result}\n")
def start_scan():
   
     # Clear the text area before starting a new scan
    host_name = host_entry.get()
    start_port=int(start_port_entry.get())
    end_port=int(End_port_entry.get())
    results = {}
    threads = []
    for port in range(start_port, end_port + 1):
        port_thread = threading.Thread(target=scan_port, args=(host_name, port, results))
        port_thread.start()
        threads.append(port_thread)
    for thread in threads:
        thread.join()
    for port in sorted(results):
          result = results[port]
          window.after(0, show_result, port, result)
               
def scan_port(host_name, port, results):
     result=check_port(host_name ,port)
     results[port] = result 
scan_button = tk.Button(
    window,
    text="START SCAN",
    command=start_scan_thread,
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#238636",
    activebackground="#2ea043",
    activeforeground="white",
    cursor="hand2",
    width=20
)
scan_button.pack(pady=20)
results_label = tk.Label(window, text="Results:", fg="white", bg="#0d1117")
results_label.pack()
results_text = tk.Text(window, height=15, width=60, fg="white", bg="#0d1117", insertbackground="white")
results_text.pack()

    


window.mainloop()

