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
root.title("The Master Converter")
#This a constant that will be used later for adjusting the positioning of functions
HEIGHT = 700
WIDTH = 1000
NOTEBOOK_ADJUST = 50
#root.minsize(300, 300)
root.geometry("1000x700")

fontStyle = ("Courier",25)

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#--------------------------- Planner -----------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
    
planner = ttk.Notebook(root, width=WIDTH-NOTEBOOK_ADJUST, height=HEIGHT-NOTEBOOK_ADJUST)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#----- Helper Routine for Printing Floats ------------------------
#-------------- with Variable Number of Decimal Places -----------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

def SmartFloatToString(number):

    # Future work:  Take a better look at how to present the
    # number.  E.g. reapeating decimals, really small numbers, etc.
    result = str(number)
    return(result)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------- Length Conversion Helper Function -----------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#Defining these length variables
Length_number1 = tk.StringVar()
Length_units1 = tk.StringVar()
Length_number2 = tk.StringVar()
Length_units2 = tk.StringVar()
#defining the button
def pressButtonConvertLength():

    # Necessary conversion from metric to imperial length units
    # that is used as a reference.
    IN_to_MM = 25.4
    
    #Creating an input
    number1_string = (Length_number1.get())
    units1_string = (Length_units1.get())
    units2_string = (Length_units2.get())

    
    # This will make sure the number is actually a number and if not then it will
    # say there is an error
    try:
        num1 = float(number1_string)
    except ValueError:
        error = True
        LengthConvertLabel3.config(text = "Invalid calculation requested.")
        return

    # Perform the conversion through a proccess of if, else and elif statments
    
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

    
    # This function will visual present the result to the view, unless there is an invaild input
    # If so the user will be told, this is done through a if and else statments along with strings    
    if not error:
        LengthConvertLabel3.config(text = "Result is " + SmartFloatToString(result) + " " +  units2_string)
    else:
        LengthConvertLabel3.config(text = "Invalid calculation requested.")

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------------ Length Conversion Frame ----------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# Set the number of widgets

N_WIDGETS = 7

# Percentage offset from the top (and bottom)
RELY_LOC = 0.12

# Automatically compute the size of the fields

REL_HEIGHT = (1 - 2 * RELY_LOC ) / N_WIDGETS
RELX_LOC = RELY_LOC
REL_WIDTH = 1 - 2 * RELX_LOC

#-----------------------------------------------------------------

LengthConvertTab = tk.Frame(planner, bg='light blue', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------

# This function is a more precise way of placing labels and buttons around the page
# By using the Rel funciton, this is great as it postions the function through a proccess
# Of seeing what percent it will take up of the page
LengthConvertLabel1 = tk.Label(
    LengthConvertTab,
    text = "Enter length then units:",
    font = fontStyle)
LengthConvertLabel1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

entryNum1 = tk.Entry(
    LengthConvertTab,
    textvariable = Length_number1,
    font = fontStyle)
entryNum1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

LengthConvertUnits1 = tk.Entry(
    LengthConvertTab,
    textvariable = Length_units1,
    font = fontStyle)
LengthConvertUnits1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

LengthConvertLabel2 = tk.Label(
    LengthConvertTab,
    text = "Enter desired units:",
    font = fontStyle)
LengthConvertLabel2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

LengthConvertUnits2 = tk.Entry(
    LengthConvertTab,
    textvariable = Length_units2,
    font = fontStyle)
LengthConvertUnits2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

LengthConvertButton = tk.Button(
    LengthConvertTab,
    text = "Calculate!",
    command = pressButtonConvertLength,
    font = fontStyle)
LengthConvertButton.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

LengthConvertLabel3 = tk.Label(
    LengthConvertTab,
    text = "",
    font = fontStyle)
LengthConvertLabel3.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#----------- Temperature Conversion Helper Function --------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------


# Defines the tempuratre related conversion functions
Temperature_number1 = tk.StringVar()
Temperature_units1 = tk.StringVar()
Temperature_number2 = tk.StringVar()
Temperature_units2 = tk.StringVar()

def pressButtonConvertTemperature():

    # convert C and F to upper case if the user enters lower case
    # Creates a varible that will store the users input that will be used to 
    # find calculate the results
    number1_string = (Temperature_number1.get()).upper()
    units1_string = (Temperature_units1.get()).upper()
    units2_string = (Temperature_units2.get()).upper()

    # Make sure the number is actually a number
    # and if not it will inform the user of the Invaild input
    
    try:
        num1 = float(number1_string)
    except ValueError:
        error = True
        TemperatureConvertLabel3.config(text = "Invalid calculation requested.")
        return

    # Perform the conversion through a series of if, elif and else statments 
    
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
        
   


    
    #This will present the rsults to the user and if there was an invalild input will inform that
        
    if not error:
        TemperatureConvertLabel3.config(text = "Result is " + SmartFloatToString(result) + " " +  units2_string)
    else:
        TemperatureConvertLabel3.config(text = "Invalid calculation requested.")

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------- Temperature Conversion Helper Function ------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

# Set the number of widgets

N_WIDGETS = 7

# Percentage offset from the top (and bottom)
RELY_LOC = 0.12

# Automatically compute the size of the fields

REL_HEIGHT = (1 - 2 * RELY_LOC ) / N_WIDGETS
RELX_LOC = RELY_LOC
REL_WIDTH = 1 - 2 * RELX_LOC

#-----------------------------------------------------------------

TemperatureConvertTab = tk.Frame(planner, bg='light blue', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------
# This function is a more precise way of placing labels and buttons around the page
# By using the Rel funciton, this is great as it postions the function through a proccess
# Of seeing what percent it will take up of the page
TemperatureConvertLabel1 = tk.Label(
    TemperatureConvertTab,
    text = "Enter temperature then units:",
    font = fontStyle)
TemperatureConvertLabel1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

entryNum1 = tk.Entry(
    TemperatureConvertTab,
    textvariable = Temperature_number1,
    font = fontStyle)
entryNum1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

TemperatureConvertUnits1 = tk.Entry(
    TemperatureConvertTab,
    textvariable = Temperature_units1,
    font=fontStyle)
TemperatureConvertUnits1.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

TemperatureConvertLabel2 = tk.Label(
    TemperatureConvertTab,
    text = "Enter desired units:",
    font = fontStyle)
TemperatureConvertLabel2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

TemperatureConvertUnits2 = tk.Entry(
    TemperatureConvertTab,
    textvariable = Temperature_units2,
    font = fontStyle)
TemperatureConvertUnits2.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

TemperatureConvertButton = tk.Button(
    TemperatureConvertTab,
    text = "Calculate!",
    command = pressButtonConvertTemperature,
    font = fontStyle)
TemperatureConvertButton.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

RELY_LOC += REL_HEIGHT

TemperatureConvertLabel3 = tk.Label(
    TemperatureConvertTab,
    text = "",
    font = fontStyle)
TemperatureConvertLabel3.place(relx=RELX_LOC, rely=RELY_LOC, relwidth=REL_WIDTH, relheight=REL_HEIGHT)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#----------------------- Reference Frame -------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#-----------------------------------------------------------------

ReferenceTab = tk.Frame(planner, bg='blue', height=HEIGHT, width=WIDTH)

#-----------------------------------------------------------------

RELX_LOC = 0.02
REL_WIDTH = 1 - 2*RELX_LOC

# Increment for height of fields and shift

RELY_ADD = 0.1
RELY_HEIGHT = RELY_ADD / 2


# This function is a more precise way of placing labels and buttons around the page
# By using the Rel funciton, this is great as it postions the function through a proccess
# Of seeing what percent it will take up of the page
ReferenceLabel1 = tk.Label(
    ReferenceTab,
    text = "Length Units:  mm , cm , m , km , in , ft , yd , mi",
    font = fontStyle)
ReferenceLabel1.place(relx=RELX_LOC, rely=RELY_ADD, relwidth=REL_WIDTH, relheight=RELY_HEIGHT)

RELY_ADD += 0.1

ReferenceLabel2 = tk.Label(
    ReferenceTab,
    text = "Temperature Units:  C , F",
    font = fontStyle)
ReferenceLabel2.place(relx=RELX_LOC, rely=RELY_ADD, relwidth=REL_WIDTH, relheight=RELY_HEIGHT)

#-----------------------------------------------------------------
#-----------------------------------------------------------------
#------------------ Merge Frames into Planner --------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------

#this allows you to add more planner/tabs within the program
planner.add(LengthConvertTab, text='Length')
planner.add(TemperatureConvertTab, text='Tempurature')
planner.add(ReferenceTab, text='Reference')

# Tabs will be added to the "top" of the "frame"
planner.grid(row = 0, column = 0)



root.mainloop()
