import tkinter as tk

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

def start_scan():
    print("Scanning started...")
    host_name = host_entry.get()
    start_port=int(start_port_entry.get())
    end_port=int(End_port_entry.get())
scan_button = tk.Button(window, text="Scan", command=start_scan)
scan_button.pack()


window.mainloop()

