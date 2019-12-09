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
HEIGHT = 700
WIDTH = 1000
NOTEBOOK_ADJUST = 50
#root.minsize(300, 300)
root.geometry("1000x700")

fontStyle = ("Courier",25)

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

# Create your variables to store data that is typed in by the user 
number1 = tk.StringVar()
units1 = tk.StringVar()
number2 = tk.StringVar()
units2 = tk.StringVar()

# Helper Functions



#-----------------------------------------------------------------
#-----------------------------------------------------------------
#--------------------------- Planner -----------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
    
planner = ttk.Notebook(root, width=WIDTH-NOTEBOOK_ADJUST, height=HEIGHT-NOTEBOOK_ADJUST)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------- Length Conversion Helper Function -----------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

def pressButtonConvertLength():

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
        LengthConvertLabel3.config(text="Result is %20.10f" % result + " " +  units2_string)
    else:
        LengthConvertLabel3.config(text="Invalid calculation requested.")

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------------ Length Conversion Frame ----------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

N_WIDGETS = 7
RELY_LOC = 0.12
REL_HEIGHT = (1 - 2 * RELY_LOC ) / N_WIDGETS
RELX_LOC = RELY_LOC
REL_WIDTH = 1 - 2 * RELX_LOC

#-----------------------------------------------------------------

LengthConvertTab = tk.Frame(planner, bg='red', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------

LengthConvertLabel1 = tk.Label(
    LengthConvertTab,
    text="Enter length and units:",
    font=fontStyle)
LengthConvertLabel1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

entryNum1 = tk.Entry(
    LengthConvertTab,
    textvariable=number1,
    font=fontStyle)
entryNum1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

LengthConvertUnits1 = tk.Entry(
    LengthConvertTab,
    textvariable=units1,
font=fontStyle)
LengthConvertUnits1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

LengthConvertLabel2 = tk.Label(
    LengthConvertTab,
    text="Enter desired units:",
    font=fontStyle)
LengthConvertLabel2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

LengthConvertUnits2 = tk.Entry(
    LengthConvertTab,
    textvariable=units2,
    font=fontStyle)
LengthConvertUnits2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

LengthConvertButton = tk.Button(
    LengthConvertTab,
    text="Calculate!",
    command = pressButtonConvertLength,
    font=fontStyle)
LengthConvertButton.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

LengthConvertLabel3 = tk.Label(
    LengthConvertTab,
    text="",
    font=fontStyle)
LengthConvertLabel3.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#----------- Temperature Conversion Helper Function --------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

def pressButtonConvertTemperature():

    
    number1_string = (number1.get())
    units1_string = (units1.get())
    units2_string = (units2.get())

    num1 = float(number1_string)

    error = True    

    if ( units1_string == "C" ):
        if ( units2_string == "C" ):
            result = num1
            error = False
        elif ( units2_string == "F" ):
            # CONVERT TO FAHRENHEIT
            result = 9 / 5 * num1 + 32
            error = False
        else:
            error = True
    elif ( units1_string == "F" ):
        if ( units2_string == "F" ):
            result = num1
            error = False
        elif ( units2_string == "C" ):
            # CONVERT TO CELSIUS
            result = (num1 - 32) * 5 / 9 
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
        TemperatureConvertLabel3.config(text="Result is %20.10f" % result + " " +  units2_string)
    else:
        TemperatureConvertLabel3.config(text="Invalid calculation requested.")

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------- Temperature Conversion Helper Function ------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

N_WIDGETS = 7
RELY_LOC = 0.12
REL_HEIGHT = (1 - 2 * RELY_LOC ) / N_WIDGETS
RELX_LOC = RELY_LOC
REL_WIDTH = 1 - 2 * RELX_LOC

#-----------------------------------------------------------------

TemperatureConvertTab = tk.Frame(planner, bg='red', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------

TemperatureConvertLabel1 = tk.Label(
    TemperatureConvertTab,
    text="Enter temperature and units:",
    font=fontStyle)
TemperatureConvertLabel1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

entryNum1 = tk.Entry(
    TemperatureConvertTab,
    textvariable=number1,
    font=fontStyle)
entryNum1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

TemperatureConvertUnits1 = tk.Entry(
    TemperatureConvertTab,
    textvariable=units1,
font=fontStyle)
TemperatureConvertUnits1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

TemperatureConvertLabel2 = tk.Label(
    TemperatureConvertTab,
    text="Enter desired units:",
    font=fontStyle)
TemperatureConvertLabel2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

TemperatureConvertUnits2 = tk.Entry(
    TemperatureConvertTab,
    textvariable=units2,
    font=fontStyle)
TemperatureConvertUnits2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

TemperatureConvertButton = tk.Button(
    TemperatureConvertTab,
    text="Calculate!",
    command = pressButtonConvertTemperature,
    font=fontStyle)
TemperatureConvertButton.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC +=REL_HEIGHT

TemperatureConvertLabel3 = tk.Label(
    TemperatureConvertTab,
    text="",
    font=fontStyle)
TemperatureConvertLabel3.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#----------------------- Reference Frame -------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#-----------------------------------------------------------------

ReferenceTab = tk.Frame(planner, bg='green', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------

RELY_ADD = 0.1

ReferenceLabel1 = tk.Label(
    ReferenceTab,
    text="Length Units:  mm , cm , m , km , in , ft , yd , mi",
    font=fontStyle)
ReferenceLabel1.place(relx=0.1, rely=RELY_ADD, relwidth=0.80, relheight=0.05)

RELY_ADD += 0.1

ReferenceLabel2 = tk.Label(
    ReferenceTab,
    text="Temperature Units:  C , F",
    font=fontStyle)
ReferenceLabel2.place(relx=0.1, rely=RELY_ADD, relwidth=0.80, relheight=0.05)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------------ Merge Frames into Planner --------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

planner.add(LengthConvertTab, text='Length')
planner.add(TemperatureConvertTab, text='Tempurature')
planner.add(ReferenceTab, text='Reference')

# Tabs will be added to the "top" of the "frame"
planner.grid(row = 0, column = 0)



root.mainloop()
