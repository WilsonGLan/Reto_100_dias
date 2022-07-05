from tkinter import *

MIN_SIZE_WIDTH = 350
MIN_SIZE_HEIGHT = 100


LABEL_ONE = "Miles"
LABEL_TWO = "is equal to"
LABEL_THREE = "Km"
LABEL_RESULT = ""
FONT_LABEL_TYPE = "Arial"
FONT_LABEL_SIZE = 12
FONT_LABEL_BOLD = "bold"


def button_clicked():
    new_text = input.get()
    miles = float(new_text)
    km = round(miles * 1.609)
    labelR.config(text=km)

window = Tk() # Create a window object
window.title("Mile to Km Converter") # Title of window
window.minsize(MIN_SIZE_WIDTH, MIN_SIZE_HEIGHT) # Size of window
window.config(padx=20, pady=20) # Adds a spaced border around the window


label1 = Label(text=LABEL_ONE, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE))
label2 = Label(text=LABEL_TWO, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE))
label3 = Label(text=LABEL_THREE, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE))
labelR = Label(text=LABEL_RESULT, font=(FONT_LABEL_TYPE, FONT_LABEL_SIZE))

input = Entry(width=10, font= ("Arial", 12))
entrada = input.get()
button = Button(text="Calculate", command= button_clicked)

label1.grid(column=2, row= 0)
label2.grid(column=0, row= 1)
label3.grid(column=2, row= 1)
labelR.grid(column=1, row= 1)
button.grid(column=1, row= 2)
input.grid(column=1, row= 0)

labelR.config(padx=5, pady=10)












window.mainloop()