#from cgitb import *
from tkinter import *

MIN_SIZE_WIDTH = 500
MIN_SIZE_HEIGHT = 300

LABEL_ONE = "My first label"
FONT_LABEL_TYPE = "Arial"
FONT_LABEL_SIZE = 24
FONT_LABEL_BOLD = "bold"

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    label1.config(text=new_text)

window = Tk() # Create a window object
window.title("My first GUI Program") # Title of window
window.minsize(MIN_SIZE_WIDTH, MIN_SIZE_HEIGHT) # Size of window
window.config(padx=20, pady=20) # Adds a spaced border around the window

label1 = Label(text=LABEL_ONE, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE, FONT_LABEL_BOLD))
label1.config(text="New Text")
# label1.pack() # Center label in the window (this is one method)
# label1.place(width= 500, height=300) #  Position the label by coordinates
label1.grid(column=0, row= 0)

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)
button2 = Button(text="Button 2", command=button_clicked)
button2.grid(column=2, row=0)

#Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3, row=2)




# the following line of code should be at the end of all the code // la siguiente linea debe estar al final deto el código
window.mainloop() # keeps the window open // mantiene la ventana abierta

