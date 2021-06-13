# Some packages are imported in full or twice due to problems with py-to-exe in getting the modules
import tkinter as tk
from tkinter import *



# UI
root = Tk()
root.title('P.O.P Calculator')
root.geometry('250x300')


# Title
title = Label(root, text="Calculator")
title.pack()

# Formula is 100 - (Max Profit / Strike Width)
strategies = ['Vertical Spreads']  # TODO: Add more as required


def Initialize():
    global pop_label
    global max_profit
    global strike_width

    # Create strategies dropdown selector
    string_var = StringVar()
    string_var.set(strategies[0])
    strategies_dropdown = OptionMenu(root, string_var, *strategies)

    strategies_dropdown.pack(side=TOP, anchor=NW)

    label_info = Label(root, text="Formula: 100 - (Max Profit / Strike Width)")
    label_info.pack(side=TOP, anchor=NW)

    space = Label(root, text="")
    space.pack()

    # Max Profit Input
    label_1 = Label(root, text="Max Profit")
    label_1.pack(side=TOP, anchor=NW)

    max_profit = Entry(root)
    max_profit.pack(side=TOP, anchor=NW)

    # Strike Width Input
    label_2 = Label(root, text="Strike Width")
    label_2.pack(side=TOP, anchor=NW)

    strike_width = Entry(root)
    strike_width.pack(side=TOP, anchor=NW)

    space_2 = Label(root, text="")
    space_2.pack()

    # Pop Results Label
    pop_label = Label(root, text="P.O.P: ")
    pop_label.pack(side=TOP, anchor=NW)

    space_3 = Label(root, text="")
    space_3.pack()

    # Start Button
    start = Button(root, text="Calculate", command=CalculatePop)
    start.pack()

def CalculatePop():
    try:
        max_prof = int(max_profit.get())
        strk_width = int(strike_width.get())
        result = 100 - (max_prof / strk_width)
        final_pop = "P.O.P: " + str(result) + "%"
        if result < 0:
            result = str(result).strip("-")
            final_pop = "P.O.P: " + str(result) + "%"
            pop_label['text'] = final_pop
            return

        pop_label['text'] = final_pop
    except:
        pass



def Update():
    root.update()
    root.update_idletasks()


if __name__ == '__main__':
    # Main Program
    Initialize()

    # Main Loop
    while True:
        Update()
