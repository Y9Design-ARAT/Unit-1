
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
# style.configure('lefttab.TNotebook', tabposition='ws')

# Helper Functions

def pressBtn1():
    num1 = (number1.get())
    #num2 = (number2.get())
    result = int(num1) * 1000
    # labelAns.config(text="Result is %d" % result + "m")
    labelAns.config(text="Result is %d" % result + "m")


planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions
tab1 = tk.Frame(planner, bg='red', width=200, height=200)
tab2 = tk.Frame(planner, bg='orange', width=200, height=200)
tab3 = tk.Frame(planner, bg='yellow', width=200, height=200)
tab4 = tk.Frame(planner, bg='green', width=200, height=200)
tab5 = tk.Frame(planner, bg='blue', width=200, height=200)
tab6 = tk.Frame(planner, bg='indigo', width=200, height=200)
tab7 = tk.Frame(planner, bg='violet', width=200, height=200)


# Add the tabs/frames to the notebook object called "planner" 
# Referred to Stack Overflow for assistance

planner.add(tab1, text='Distance')
btn1 = tk.Button(planner, text = "Convert", command = pressBtn1, padx = 20)

planner.add(tab2, text='Tempurature')
planner.add(tab3, text='Weight')
planner.add(tab4, text="Wednesday")
planner.add(tab5, text="Thursday")
planner.add(tab6, text="Friday")
planner.add(tab7, text="Saturday")
#tab1.add(btn1, text="Convert")

b1 = Button(tab1,text="Convert",fg="red")

# Tabs will be added to the "top" of the "frame"
planner.pack(side=tk.TOP)

root.mainloop()
