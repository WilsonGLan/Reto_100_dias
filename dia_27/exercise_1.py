import tkinter

MIN_SIZE_WIDTH = 500
MIN_SIZE_HEIGHT = 300

LABEL_ONE = "My first label"
FONT_LABEL_TYPE = "Arial"
FONT_LABEL_SIZE = 24
FONT_LABEL_BOLD = "bold"


window = tkinter.Tk() # Create a window object
window.title("My first GUI Program") # Title of window
window.minsize(MIN_SIZE_WIDTH, MIN_SIZE_HEIGHT) # Size of window

label1 = tkinter.Label(text=LABEL_ONE, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE, FONT_LABEL_BOLD))
label1.pack() # Center label in the window





# the following line of code should be at the end of all the code // la siguiente linea debe estar al final deto el código
window.mainloop() # keeps the window open // mantiene la ventana abierta

