import tkinter as tk
from tkinter import ttk
from tkinter import *

#Main Window for the program here.
main = tk.Tk()
main.geometry("600x600")
main.title("Main Page.")

#Scheduling Window for the program here.
Schedule = tk.Tk()

def open_win():
    new = Toplevel(Schedule)
    new.geometry("600x600")
    new.title("Schedule")

#Button for Adding client
Client_button = ttk.Button(
    main,
    text = "Add Client",
    command=()
)

Client_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


#Buttone for Adding Staff
Staff_button = ttk.Button(
    main,
    text = "Add Staff",
    command=()
)

Staff_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


#Button for scheduling
Schedule_button = ttk.Button(
    main,
    text = "Add New Schedule",
    command = ()
)

Schedule_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)


#Button to Exit.
exit_button = ttk.Button(
    main,
    text= "EXIT",
    command=lambda: main.quit()
)

exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

main.mainloop()