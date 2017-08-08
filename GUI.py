# python3

# ***** Data structure  *****

# TODO: create a dictionary for each category "lengh" "density".....





# ***** import the required modules. *****
from tkinter import *
from uc import Units


calc = Units()
unitList = list(calc.L.keys())

def doNoting():
    print('ok ok i won...')


def length():
    unitList = list(calc.L.keys())
 #   result = calc.convert(type, unit1, unit2, value)


def area():
    unitList = list(calc.A.keys())
 #   result = calc.convert(type, unit1, unit2, value)

def run():
    if entry_1.get().isnumeric():
        result = convert_temperature(float(entry_1.get()), variable_1.get(), variable_2.get())
        print(result)
    else:
        tkinter.messagebox.showinfo('error!', 'Invalid entry. \n\nIt has to be a number.')


# *****   main GUI   ********************************************************************************
root = Tk()
root.title('Engineering Units Converter 0.0.1')

# ******* The Main menu ********
menu = Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label='File', menu=submenu)
submenu.add_command(label='Now project...', command=doNoting)
submenu.add_command(label='Now...', command=doNoting)
submenu.add_separator()
submenu.add_command(label='Exit', command = doNoting)
editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label = 'Redo', command=doNoting)
menu.add_cascade(label='Help', menu=editMenu)
editMenu.add_command(label = 'About', command=doNoting)

# ******* The Toolbar ********
toolbar = Frame(root, bg='gray')
insertButt = Button(toolbar, text='Insert', command = doNoting)
insertButt.pack(side=LEFT, padx=2, pady=2, )
printButt = Button(toolbar, text='Print', command = doNoting)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***********   images and icons *****
frame_2 = Frame(root)
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
selectbar_1 = Radiobutton(frame_2, text = 'Lengh', variable=v,value = 1, command = length).grid(row = 0, column = 0, sticky = W)
selectbar_2 = Radiobutton(frame_2, text = 'Area', variable=v,value = 2, command = area).grid(row = 0, column = 1, sticky = W)
selectbar_3 = Radiobutton(frame_2, text = 'Volumn', variable=v,value = 3, command = doNoting).grid(row = 0, column = 2, sticky = W)
selectbar_4 = Radiobutton(frame_2, text = 'Pressure', variable=v,value = 4, command = doNoting).grid(row = 0, column = 3, sticky = W)
selectbar_5 = Radiobutton(frame_2, text = 'Temeprature', variable=v,value = 5, command = doNoting).grid(row = 0, column = 4, sticky = W)
selectbar_6 = Radiobutton(frame_2, text = 'Density', variable=v,value = 6, command = doNoting).grid(row = 0, column = 5, sticky = W)
selectbar_7 = Radiobutton(frame_2, text = 'Weight', variable=v,value = 7, command = doNoting).grid(row = 0, column = 6, sticky = W)
selectbar_8 = Radiobutton(frame_2, text = 'Power', variable=v,value = 8, command = doNoting).grid(row = 0, column = 7, sticky = W)
selectbar_9 = Radiobutton(frame_2, text = 'Velocity', variable=v,value = 9, command = doNoting).grid(row = 0, column = 8, sticky = W)


frame_2.pack(side=TOP, fill=X)

#  ******* entry window ********

frame_entry = Frame(root)

#  TODO: need to update this list per unit list.
#unitList = list(unitDic.keys())


variable_1 = StringVar(frame_entry)
variable_1.set(unitList[1]) # default value
variable_2 = StringVar(frame_entry)
variable_2.set(unitList[2]) # default value

unit_1 = OptionMenu(frame_entry, variable_1, *unitList)   #   use "*"  + list
unit_2 = OptionMenu(frame_entry, variable_2, *unitList)

label_1 = Label(frame_entry, text='Input')
button = Button(frame_entry, text='Convert', command = run)
label_2 = Label(frame_entry, text='Result')

entry_1 = Entry(frame_entry)
entry_2 = Entry(frame_entry)

unit_1.grid(row = 1, column = 3)
label_1.grid(row = 1, column = 0)
button.grid(row = 3, column = 1)
label_2.grid(row = 5, column = 0)

entry_1.grid(row = 1, column =1)
entry_2.grid(row = 5, column =1)
unit_2.grid(row = 5, column = 3)

frame_entry.pack()


# ******* Status Bar ********
status = Label(root, text = 'Engineering Units Converter 0.0.0 Beta', bd =1,relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)


root.mainloop()