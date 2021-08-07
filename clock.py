# IMPORTING REQUIRED MODULES
from tkinter import *
from tkinter.ttk import *
from time import strftime

# MAIN WINDOW
clock = Tk()
clock.title('Clock')

# TIME FUNCTION
def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000, time)

# WIDGET STYLING
lbl = Label(clock, font = ('JetBrains Mono', 30, 'bold'), background = 'white', foreground = 'black')
# ALIGNING WIDGET TO CENTER
lbl.pack(anchor = 'center')
time()

# MAKING IT NOR-RESIZABLE
clock.resizable(0,0)

# MAIN APPLICATION
clock.mainloop()