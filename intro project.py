import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()

# Create the date, time, name, and staff name input fields
date_input = tk.Entry(root)
time_input = tk.Entry(root)
name_input = tk.Entry(root)
staff_name_input = tk.Entry(root)

# Create labels for the input fields
date_label = tk.Label(root, text='Date')
time_label = tk.Label(root, text='Time')
name_label = tk.Label(root, text='Name')
staff_name_label = tk.Label(root, text='Staff Name')

# Create a function to handle the input and output
def handle_input():
  # Get the input values
  date = date_input.get()
  time = time_input.get()
  name = name_input.get()
  staff_name = staff_name_input.get()

  # Check if any of the input fields are empty
  if not date or not time or not name or not staff_name:
    # Show an error message if any of the input fields are empty
    messagebox.showerror('Error', 'All input fields are required')
    return

  # Format the appointment string
  appointment = f'{date} at {time}: Appointment with {name} (Staff: {staff_name})'

  # Write the appointment to a text file
  with open('appointments.txt', 'a') as file:
    file.write(appointment + '\n')

  # Clear the input fields
  date_input.delete(0, tk.END)
  time_input.delete(0, tk.END)
  name_input.delete(0, tk.END)
  staff_name_input.delete(0, tk.END)
  
  # Create the window that shows that the appointments are saved
  save_window = tk.Toplevel(root)
  save_window.title('Appointments Saved')

  # Create a label for the window
  saved_label = tk.Label(save_window, text='Appointments saved to file')
  saved_label.pack()

# Create the exit button
exit_button = tk.Button(root, text='Exit', command=root.quit)
exit_button.pack()

# Create the Submit button
submit_button = tk.Button(root, text='Submit', command=handle_input)

# Place the input fields and labels in the main window
date_label.pack()
date_input.pack()
time_label.pack()
time_input.pack()
name_label.pack()
name_input.pack()
staff_name_label.pack()
staff_name_input.pack()

# Place the Submit button in the main window
submit_button.pack()

# Start the main loop
root.mainloop()