#!/usr/bin/env python3

# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

#  .d8b.   .d8b.  d8888b.  .d88b.  d8b   db .d8888.
# d8' `8b d8' `8b 88  `8D .8P  Y8. 888o  88 88'  YP
# 88ooo88 88ooo88 88oobY' 88    88 88V8o 88 `8bo.  
# 88~~~88 88~~~88 88`8b   88    88 88 V8o88   `Y8b.
# 88   88 88   88 88 `88. `8b  d8' 88  V888 db   8D
# YP   YP YP   YP 88   YD  `Y88P'  VP   V8P `8888Y'
#
#    .o88b.  .d88b.  d8b   db db    db d88888b d8888b. d888888b d88888b d8888b. 
#   d8P  Y8 .8P  Y8. 888o  88 88    88 88'     88  `8D `~~88~~' 88'     88  `8D 
#   8P      88    88 88V8o 88 Y8    8P 88ooooo 88oobY'    88    88ooooo 88oobY' 
#   8b      88    88 88 V8o88 `8b  d8' 88~~~~~ 88`8b      88    88~~~~~ 88`8b   
#   Y8b  d8 `8b  d8' 88  V888  `8bd8'  88.     88 `88.    88    88.     88 `88. 
#    `Y88P'  `Y88P'  VP   V8P    YP    Y88888P 88   YD    YP    Y88888P 88   YD

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("My TKinter Hack")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

# Create your variables to store data that is typed in by the user 
number1 = tk.StringVar()
units1 = tk.StringVar()
number2 = tk.StringVar()
units2 = tk.StringVar()

# Helper Functions

def pressButtonConvertLengh():

    # Necessary conversion from metric to imperial length units
    # that is used as a reference.
    IN_to_MM = 25.4
    
    number1_string = (number1.get())
    units1_string = (units1.get())
    units2_string = (units2.get())

    #
    # MAKE SURE num1 IS ACTUALLY A NUMBER
    #
    
    # ???

    num1 = float(number1_string)

    #
    # MAKE SURE units1_string IS ACTUALLY A PROPER UNIT
    #

    # ???
    
    #
    # MAKE SURE units2_string IS ACTUALLY A PROPER UNIT
    #

    # ???

    #
    # DEFAULT ERROR FLAG IS TRUE UNTIL SUCCESSFUL CONVERSION IS PERFORMED
    #

    error = True    

    #
    # PROCESS THE UNIT CONVERSION
    #

    if (units1_string == "mm"):
        if (units2_string == "mm"):
            result = num1
            error = False
        elif (units2_string == "cm"):
            result = num1 / 10.0
            error = False
        elif (units2_string == "m"):
            result = num1 / 1000.0
            error = False
        elif (units2_string == "km"):
            result = num1 / 1000000.0
            error = False
        elif (units2_string == "in"):
            result = num1 / IN_to_MM
            error = False
        elif (units2_string == "ft"):
            result = num1 / IN_to_MM / 12.0
            error = False
        elif (units2_string == "yd"):
            result = num1 / IN_to_MM / 12.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 / IN_to_MM / 12.0 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "cm"):
        if (units2_string == "mm"):
            result = num1 * 10.0
            error = False
        elif (units2_string == "cm"):
            result = num1
            error = False
        elif (units2_string == "m"):
            result = num1 / 100.0
            error = False
        elif (units2_string == "km"):
            result = num1 / 100000.0
            error = False
        elif (units2_string == "in"):
            result = num1 * 10.0 / IN_to_MM
            error = False
        elif (units2_string == "ft"):
            result = num1 * 10.0 / IN_to_MM / 12.0
            error = False
        elif (units2_string == "yd"):
            result = num1 * 10.0 / IN_to_MM / 12.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 * 10.0 / IN_to_MM / 12.0 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "m"):
        if (units2_string == "mm"):
            result = num1 * 1000.0
            error = False
        elif (units2_string == "cm"):
            result = num1 * 100.0
            error = False
        elif (units2_string == "m"):
            result = num1
            error = False
        elif (units2_string == "km"):
            result = num1 / 1000.0
            error = False
        elif (units2_string == "in"):
            result = num1 * 100.0 * 10.0 / IN_to_MM
            error = False
        elif (units2_string == "ft"):
            result = num1 * 100.0 * 10.0 / IN_to_MM / 12.0
            error = False
        elif (units2_string == "yd"):
            result = num1 * 100.0 * 10.0 / IN_to_MM / 12.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 * 100.0 * 10.0 / IN_to_MM / 12.0 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "km"):
        if (units2_string == "mm"):
            result = num1 * 1000000.0
            error = False
        elif (units2_string == "cm"):
            result = num1 * 100000.0
            error = False
        elif (units2_string == "m"):
            result = num1 * 1000.0
            error = False
        elif (units2_string == "km"):
            result = num1
            error = False
        elif (units2_string == "in"):
            result = num1 * 100000.0 / IN_to_MM
            error = False
        elif (units2_string == "ft"):
            result = num1 * 1000000.0 / IN_to_MM / 12.0
            error = False
        elif (units2_string == "yd"):
            result = num1 * 1000000.0 / IN_to_MM / 12.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 * 1000000.0 / IN_to_MM / 12.0 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "in"):
        if (units2_string == "mm"):
            result = num1 * IN_to_MM
            error = False
        elif (units2_string == "cm"):
            result = num1 * IN_to_MM / 10.0 
            error = False
        elif (units2_string == "m"):
            result = num1 * IN_to_MM / 1000.0
            error = False
        elif (units2_string == "km"):
            result = num1 * IN_to_MM / 1000000.0
            error = False
        elif (units2_string == "in"):
            result = num1
            error = False
        elif (units2_string == "ft"):
            result = num1 / 12.0
            error = False
        elif (units2_string == "yd"):
            result = num1 / 12.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 / 12.0 / 5280.0
            error = False
        else:
            error = True
        
    elif (units1_string == "ft"):
        if (units2_string == "mm"):
            result = num1 * 12.0 * IN_to_MM
            error = False
        elif (units2_string == "cm"):
            result = num1 * 12.0 * IN_to_MM / 10.0
            error = False
        elif (units2_string == "m"):
            result = num1 * 12.0 * IN_to_MM / 1000.0
            error = False
        elif (units2_string == "km"):
            result = num1 * 12.0 * IN_to_MM / 1000000.0
            error = False
        elif (units2_string == "in"):
            result = num1 * 12.0
            error = False
        elif (units2_string == "ft"):
            result = num1
            error = False
        elif (units2_string == "yd"):
            result = num1 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "yd"):
        if (units2_string == "mm"):
            result = num1 * 3.0 * 12.0 * IN_to_MM
            error = False
        elif (units2_string == "cm"):
            result = num1 * 3.0 * 12.0 * IN_to_MM / 10.0
            error = False
        elif (units2_string == "m"):
            result = num1 * 3.0 * 12.0 * IN_to_MM / 1000.0
            error = False
        elif (units2_string == "km"):
            result = num1 * 3.0 * 12.0 * IN_to_MM / 1000000.0
            error = False
        elif (units2_string == "in"):
            result = num1 * 3.0 * 12.0
            error = False
        elif (units2_string == "ft"):
            result = num1 * 3.0
            error = False
        elif (units2_string == "yd"):
            result = num1
            error = False
        elif (units2_string == "mi"):
            result = num1 * 3.0 / 5280.0
            error = False
        else:
            error = True
            
    elif (units1_string == "mi"):
        if (units2_string == "mm"):
            result = num1 * 5280.0 * 12.0 * IN_to_MM
            error = False
        elif (units2_string == "cm"):
            result = num1 * 5280.0 * 12.0 * IN_to_MM / 10.0
            error = False
        elif (units2_string == "m"):
            result = num1 * 5280.0 * 12.0 * IN_to_MM / 100.0
            error = False
        elif (units2_string == "km"):
            result = num1 * 5280.0 * 12.0 * IN_to_MM / 1000000.0
            error = False
        elif (units2_string == "in"):
            result = num1 * 5280.0 * 12.0
            error = False
        elif (units2_string == "ft"):
            result = num1 * 5280.0
            error = False
        elif (units2_string == "yd"):
            result = num1 * 5280.0 / 3.0
            error = False
        elif (units2_string == "mi"):
            result = num1
            error = False
        else:
            error = True

    else:
        error = True

    #
    # PRESENT THE RESULT
    #

    # The print statement is not very nice because the result can
    # have a large disparity in terms of decimal places and number
    # of zeros.

    #
    # MAKE THE STRING FORMATTING OF RESULT BETTER :)
    #
        
    if not error:
        label2.config(text="Result is %20.10f" % result + " " +  units2_string)
    else:
        label2.config(text="Invalid calculation requested.")
            


    
planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

############## Start Frame 1 ##############

tab1 = tk.Frame(planner, bg='light blue', width=200, height=200)

label1 = tk.Label(tab1, text="Enter length and units:")
label1.grid(row=0, column=0)

entryNum1 = tk.Entry(tab1, textvariable=number1)
entryNum1. grid(row=1, column=0)

entryUnits1 = tk.Entry(tab1, textvariable=units1)
entryUnits1. grid(row=2, column=0)

label1 = tk.Label(tab1, text="Enter desired units:")
label1.grid(row=3, column=0)

entryUnits2 = tk.Entry(tab1, textvariable=units2)
entryUnits2. grid(row=4, column=0)

button1 = tk.Button(tab1, text="Calculate!", command = pressButtonConvertLengh)
button1.grid(row=5, column=0)

label2 = tk.Label(tab1, text="")
label2.grid(row=6, column=0)

############## End Frame 1 #############@

# These frames have not been implemented yet
tab2 = tk.Frame(planner, bg='orange', width=200, height=200)
tab3 = tk.Frame(planner, bg='yellow', width=200, height=200)
tab4 = tk.Frame(planner, bg='green', width=200, height=200)
tab5 = tk.Frame(planner, bg='blue', width=200, height=200)
tab6 = tk.Frame(planner, bg='indigo', width=200, height=200)
tab7 = tk.Frame(planner, bg='violet', width=200, height=200)

# Add the tabs/frames to the notebook object called "planner" 
# Referred to Stack Overflow for assistance

planner.add(tab1, text='Distance')
planner.add(tab2, text='Tempurature')
planner.add(tab3, text='Weight')
planner.add(tab4, text="Wednesday")
planner.add(tab5, text="Thursday")
planner.add(tab6, text="Friday")
planner.add(tab7, text="Saturday")


# Tabs will be added to the "top" of the "frame"
#planner.pack(side=tk.TOP)
planner.grid(row = 0, column = 0)

root.mainloop()
