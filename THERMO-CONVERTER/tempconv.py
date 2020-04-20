# TEMPERATURE CONVERTER
import tkinter as tk
from tkinter import *
import random
# declare global_Variables
temp_c = None
temp_f = None

#create the main window
root = tk.Tk()
root.title("AUTO-THERMO_CONVERTER")

# create main container
frame = tk.Frame(root,bg="yellow")

# Layout the main contaner, specify that we want it to grow with  the window size
frame.pack(fill = tk.BOTH,expand=True)
# allow middle cell of the grid to grow when the window grows
frame.columnconfigure(1,weight=1)
frame.rowconfigure(1,weight =1)

# Variables for holding temperature data
temp_c = tk.DoubleVar()
temp_f = tk.DoubleVar()
#__________________________________________________________________________________________________________________________________
# This function is called whenever the button is pressed
def convert():

    global temp_c
    global temp_f

    # convert celsuis to fahrenhiet and update (through textvariable)
    try:
        val = temp_c.get()
        temp_f.set((val*9.0/5)+32)
    except:
        pass
#____________________________________________________________________________________________________________________________________

# This secoond function is also called

# Canvas  
C = tk.Canvas(frame,bg="yellow", height=30,width=180)
oval = C.create_oval(0,0,40,40,fill = "pink")
oval2 = C.create_oval(0,0,200,200,fill="red")
oval3 = C.create_oval(0,0,150,150,fill="white")
C.grid(row=4,column=0)

# create widgets
label_input = tk.Label(frame,width = 15, text = "Enter a Value ",bg = "pink", font=("times",17))
entry_celsuis = tk.Entry(frame, width = 15, textvariable = temp_c)
label_unitc = tk.Label(frame,width = 5, text =" 'C",fg="blue",font=("times",20))
label_equal = tk.Label(frame, width = 15, text = "Equivalent To    ",bg = "pink",font=("times",17))
label_fahrenheit = tk.Label(frame,width= 10,textvariable=temp_f,font=("times",20))
label_unitf = tk.Label(frame,width = 5, text = " 'F",fg="blue",font=("times",20))
button_convert = tk.Button(frame,height = 2,text= "CONVERT",command=(convert),bg="red")
developer = tk.Label(frame,text = "Developed By DERA",fg = "Blue",font=("times",12))
info = tk.Label(frame,text="Stay Safe from COVID-19",fg = "pink",bg="orange",font=("times",14,"italic"))
# label for displaying warning msg about the covid 19 pandemic
# Initiallising

#_________________________________________________

# Scaling widget

def start():
    def sel():
        myinfos = ["The normal body\n temperature range is\n typically stated as\n[36.5 - 37.5'C]or[97.7-99.5'F]",
                   "Ensure you take serious \n precautions and preventive\nmeasures against COVID-19",
                   "The [ WHO ] is constantly\n strengthening measures\nto ensure that the\nPandemic is contolled",
                   "Normal human body\ntemperature(normothermia,\neuthemia) is the typical\n temperature found in human",
                   "Maintain at least 1 & half\nmetres distance between\nyou and a person who\nis coughing or sneezing",
                   "People coughing or sneezing\n persistently should keep a\nsocial distance but not mix up\nwith a crowd",
                   "if you notice symptoms\n related to covid-19 please call\nemergency hotlines:\n+2348023169485,\n+2348033565529",
                   "whatever you do will seem\ninsignificant but it is\nvery important you do it\n.(Mahtma Gandhi)\n... STAY SAFE ...",
                   ]
        selection = random.choice(myinfos)
        label.config(text = selection)
    var = DoubleVar()
    scale = (Scale(frame,variable = var,orient = HORIZONTAL,bg="orange"))
    scale.grid(row=0,column=3)
    scale.set(40)
    scale.focus_set()
    #scale.current(60)
    button = Button(frame,width = 20,fg="blue",bg="red",text="Virtual Scale info's",command=sel)
    button.grid(row=1,column=3)

    label = Label(frame,width=22,height=5,bg="light grey")
    label.grid(row=2,column=3)

start()

#___________________
# lay out widgets
label_input.grid(row=0,column = 0,padx=5,pady=5,sticky=tk.E)
entry_celsuis.grid(row = 0, column=1, padx=5, pady=5)
label_unitc.grid(row = 0, column=2, padx=5, pady=5, sticky=tk.W)
label_equal.grid(row = 1, column=0, padx=5, pady=5, sticky=tk.E)
label_fahrenheit.grid(row = 1, column=1, padx=5, pady=5)
label_unitf.grid(row = 1, column=2, padx=5, pady=5, sticky=tk.W)
button_convert.grid(row = 2, column=1,columnspan=1, padx=5, pady=5, sticky=tk.E)
developer.grid(row = 4,column = 0,padx=5, pady=5, sticky=tk.E)
info.grid(row = 2,column = 0,padx=5, pady=5, sticky=tk.E)
# Place the cursor
entry_celsuis.focus()

# Run forever
root.mainloop()
