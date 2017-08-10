from tkinter import *


UNITLIST = [1,2,3,4,5,6,7]
UNITLIST2 = [10,20,30,40,50,60,70]
unitList = UNITLIST[:]

root = Tk()
root.geometry('+400+200')
root.minsize(400,200)
root.title("test")


def doNoting():
    print(unitList)

def area(n):
    print(n,'area!!')
    unitList = UNITLIST2[:]
    print(unitList)

def density(n):
    print(n,'area!!')
    unitList = UNITLIST[:]
    print(unitList)


frame_2 = Frame(root)
v = IntVar()
v.set(1)  # initializing the choice, Defult choice is 'Lengh'
selectbar_1 = Radiobutton(frame_2, text = 'Lengh', variable=v,value = 1, command = lambda: doNoting).grid(row = 0, column = 0, sticky = W)
selectbar_2 = Radiobutton(frame_2, text = 'Area', variable=v,value = 2, command = lambda: area(33)).grid(row = 0, column = 1, sticky = W)
selectbar_3 = Radiobutton(frame_2, text = 'Volumn', variable=v,value = 3, command = doNoting).grid(row = 0, column = 2, sticky = W)
selectbar_4 = Radiobutton(frame_2, text = 'Pressure', variable=v,value = 4, command = doNoting).grid(row = 0, column = 3, sticky = W)
selectbar_5 = Radiobutton(frame_2, text = 'Temeprature', variable=v,value = 5, command = doNoting).grid(row = 0, column = 4, sticky = W)
selectbar_6 = Radiobutton(frame_2, text = 'Density', variable=v,value = 6, command = doNoting).grid(row = 0, column = 5, sticky = W)
selectbar_7 = Radiobutton(frame_2, text = 'Weight', variable=v,value = 7, command = doNoting).grid(row = 0, column = 6, sticky = W)
selectbar_8 = Radiobutton(frame_2, text = 'Power', variable=v,value = 8, command = doNoting).grid(row = 0, column = 7, sticky = W)
selectbar_9 = Radiobutton(frame_2, text = 'Velocity', variable=v,value = 9, command = doNoting).grid(row = 0, column = 8, sticky = W)

frame_2.pack(side=TOP, fill=X)
#***************************************************************************************************************
frame_entry = Frame(root)

variable_1 = StringVar(frame_entry)
variable_1.set(unitList[1]) # default value is Lengh Units

unit_1 = OptionMenu(frame_entry, variable_1, *unitList)   #   use "*"  + list

label_1 = Label(frame_entry, text='Input')
button = Button(frame_entry, text='Convert', command = doNoting)


entry_1 = Entry(frame_entry,)


unit_1.grid(row = 1, column = 3)
label_1.grid(row = 1, column = 0)
button.grid(row = 3, column = 1)


entry_1.grid(row = 1, column =1)


frame_entry.pack()



root.mainloop()