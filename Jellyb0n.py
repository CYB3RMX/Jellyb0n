#!/usr/bin/env python3

import os,sys
from tkinter import *

# Checking permissions
perm = int(os.getuid())
if perm != 0:
    print("You must be a root to use this program.")
    sys.exit(1)
# Creating window
window = Tk()
window.geometry("600x250")
window.title("Jellyb0n Simple Firewall")
# Creating labels
target_port = Label(window, text="Enter port to close: ")
target_port.grid(column=0, row=0)
port = Entry(window, width="15")
port.grid(column=1, row=0)
information = Label(window, text="")
information.grid(column=1, row=2)
info2 = Label(window, text="")
info2.grid(column=1, row=5)
restoree = Label(window, text="Restore firewall rules => ")
restoree.grid(column=0, row=4)
open_port = Label(window, text="Enter port to open: ")
open_port.grid(column=0, row=6)
open_enter = Entry(window, width="15")
open_enter.grid(column=1, row=6)
listen_area = Label(window, text="")
listen_area.grid(column=0, row=7)
blocker_lbl = Label(window, text="Enter IP address to block: ")
blocker_lbl.grid(column=0, row=8)
blocker_ent = Entry(window, width="15")
blocker_ent.grid(column=1, row=8)
blocker_inf = Label(window, text="")
blocker_inf.grid(column=0, row=9)
# Defining button commands
def closer():
   try:
      killer0 = "iptables -A INPUT -p tcp --destination-port {} -j DROP".format(port.get())
      killer1 = "iptables -A OUTPUT -p tcp --destination-port {} -j DROP".format(port.get())
      os.system(killer0)
      os.system(killer1)
      information.configure(text="Port {} successfully closed.".format(port.get()))
   except:
      information.configure(text="An error occured while closing the port.")
def restore():
   try:
       os.system("sudo iptables -F")
       info2.configure(text="Firewall rules restored.")
   except:
       info2.configure(text="An error occured while restoring the rules.")
def openn():
   try:
       listen_area.configure(text="Port {}/tcp opened and listening connections.".format(open_enter.get()))
       server = "nc -lvp {}".format(open_enter.get())
       os.system(server)
   except:
       listen_area.configure(text="An error occured while listening the server.")
def blocker():
   try:
       block = "iptables -A INPUT -s {} -j DROP".format(blocker_ent.get())
       os.system(block)
       blocker_inf.configure(text="IP Address: {} successfully blocked.".format(blocker_ent.get()))
   except:
       blocker_inf.configure(text="An error occured while blocking.")
# Creating buttons
buttons = Button(window, text="Close", command=closer)
buttons.grid(column=2, row=0)
buttons2 = Button(window, text="Restore", command=restore)
buttons2.grid(column=1, row=4)
buttons3 = Button(window, text="Open", command=openn)
buttons3.grid(column=2, row=6)
buttons4 = Button(window, text="Block", command=blocker)
buttons4.grid(column=2, row=8)
window.mainloop()
