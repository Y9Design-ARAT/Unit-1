# A simple calculator example
# Based on example found in programminginpython.com
# Modified for instructional purposes

import tkinter as tk

#Creates a window of a particular size
MyWindow = tk.Tk()
MyWindow.title("A Simple Calculator")
MyWindow.geometry('600x400')

OPTIONS = [
"Option A",
"Option B",
"Option C",
"Option D",
"Option E",
"Option F"
""
] #etc

# This one currently adds two numbers together
def clicked():
    num1 = (number1.get())
    #num2 = (number2.get())
    result = int(num1) * 1000
    # labelAns.config(text="Result is %d" % result + "m")
    labelAns.config(text="Result is %d" % result + "m")

# Helper function to give the button functionality
# Helper functions always go above the widgets that are created

#def clickedmenu():
 #   info = "Welcome to " + txt.get()
  #  lbl.configure(text= info)


# Create the widgets - a Label, Textbox, Button, Dropdown Menu (in that order)

# This label is to provide an instruction
lbl = tk.Label(MyWindow, text = "Please enter the value here to be converted")

# This is where we input information
txt = tk.Entry(MyWindow, width = 10)

# This is a button that does the conversion
# btn = tk.Button(MyWindow, text = "Click Me", command = clicked)

#variable = tk.StringVar(MyWindow) # needed for the dropdown menu (ddm)
#variable.set(OPTIONS[0]) # default value
#ddm = tk.OptionMenu(MyWindow, variable, *OPTIONS)


# Place all of the widgets into the "imagnary" grid


lbl.grid(column = 0, row = 0) # first column, first row
txt.grid(column = 1, row = 0) # second column, first row
btn.grid(column = 2, row = 0) # third column, first row
#ddm.grid(column = 3, row = 1)


# Helper functions to support button action

# This one is not currently being used

'''
def clicked2():

    radius = float(txt.get())
    area = 3.14 * (radius ** 2)
    info = "The area of the circle is:"
    lbl.configure(text= info)
'''


 
# Create your variables  
number1 = tk.StringVar()
#number2 = tk.StringVar()

# Creating all of the labels with text information
labelTitle = tk.Label(MyWindow, text="What do you want to convert?")
labelNum1 = tk.Label(MyWindow, text="Enter the number of km")
# labelNum2 = tk.Label(MyWindow, text="Enter second number")
labelAns = tk.Label(MyWindow, text="The answer is")

# Arranging all of the labels in a "grid" where row "0", column "0" 
# represents the upper left hand corner
labelTitle.grid(row=1, column=0)
labelNum1.grid(row=2, column=0)
#labelNum2.grid(row=2, column=0)
labelAns.grid(row=3, column=0)

# Here is where we go to input our numbers
entryNum1 = tk.Entry(MyWindow, textvariable=number1)
entryNum1. grid(row=1, column=2)
# entryNum2 = tk.Entry(MyWindow, textvariable=number2)
# entryNum2. grid(row=2, column=2)

# Here is where we set up the button to perform "call" the calculation
# Calculation is performed when the "clicked" function is called
buttonCal = tk.Button(MyWindow, text="Calculate", command=clicked)
buttonCal.grid(row=5, column=0)

# Main Loop
MyWindow.mainloop()
