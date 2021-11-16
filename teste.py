
from tkinter import * 
 
root = Tk() # create root window
root.title("Frame Example")
root.config(bg="skyblue")
 
# Create Frame widget
left_frame = Frame(root, width=200, height=400)
left_frame.grid(row=10, column=2, padx=10, pady=5)
 
root.mainloop()