# python3

# ***** Data structure  *****

# TODO: create a dictionary for each category "lengh" "density".....





# ***** import the required modules. *****
from tkinter import *
from uc import Units


calc = Units()
UNIT_TYPE = 'L'
unitList = list(getattr(calc,UNIT_TYPE).keys())  # TODO：这里有问题需有检查

def doNoting():
    out = entry_1.get()
    print(out)
    entry_2.delete(0,END)
    entry_2.insert(0,out)


def run():  # TODO: 程序运行主函数，　调用单位转换函数。在窗口输出计算值。
    in_unit = variable_1.get()
    out_unit = variable_2.get()
    entry = entry_1.get()
    print(entry, in_unit, out_unit)     # 测试是否赋值成功？
    out = Units.convert(UNIT_TYPE, entry,in_unit, out_unit)   # 调用主外部函数计算输出值。
    print(out)
    entry_2.delete(0,END)   # 刷新输出栏，显示最新计算结果
    entry_2.insert(0,out)


def freshlist():
    variable_1.set('')
    variable_2.set('')
    unit_1['Menu'].delete(0,END)  # 删除原有下拉列表。相当于unit_1.keys().delete()
    unit_2['Menu'].delete(0,END)
    
    UNIT_TYPE = variable.get()  #  只是字符串
    calc = Units()
    unitList = list(getattr(calc,UNIT_TYPE).keys())   # 将字符串转换成对应的单位属性，调取单位列表赋值给unitList.
    print (unitList)  #  TODO: 测试是否赋值成功？
    for unit in unitList:
        unit_1['menu'].add_command(label=unit, command= _setit(variable_1, unit))
        unit_2['menu'].add_command(label=unit, command= _setit(variable_2, unit))

# *****   main GUI   ********************************************************************************
root = Tk()
root.title('Lulus Process Engineer Aux. 0.0.1')

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

# ***********   Category selection**** *****
# TODO: command has not been set up.
frame_2 = Frame(root)
v = StringVar()
v.set('L')  # initializing the choice, Defult choice is 'Lengh'  
selectbar_1 = Radiobutton(frame_2, text = 'Lengh', variable=v,value = 'L', command = freshlist).grid(row = 0, column = 0, sticky = W)
selectbar_2 = Radiobutton(frame_2, text = 'Area', variable=v,value = 'A', command = freshlist).grid(row = 0, column = 1, sticky = W)
selectbar_3 = Radiobutton(frame_2, text = 'Volumn', variable=v,value = 'V', command = freshlist).grid(row = 0, column = 2, sticky = W)
selectbar_4 = Radiobutton(frame_2, text = 'Pressure', variable=v,value = 'P', command = freshlist).grid(row = 0, column = 3, sticky = W)
selectbar_5 = Radiobutton(frame_2, text = 'Temeprature', variable=v,value = 'T', command = freshlist).grid(row = 0, column = 4, sticky = W)
selectbar_6 = Radiobutton(frame_2, text = 'Density', variable=v,value = 'density', command = freshlist).grid(row = 0, column = 5, sticky = W)
selectbar_7 = Radiobutton(frame_2, text = 'Weight', variable=v,value = 'W', command = freshlist).grid(row = 0, column = 6, sticky = W)
selectbar_8 = Radiobutton(frame_2, text = 'Power', variable=v,value = 'P', command = freshlist).grid(row = 0, column = 7, sticky = W)
selectbar_9 = Radiobutton(frame_2, text = 'Velocity', variable=v,value = 'V', command = freshlist).grid(row = 0, column = 8, sticky = W)
#TODO:  这里可以通过 "for" 合并并赋值。 

frame_2.pack(side=TOP, fill=X)

#  ******* entry window ********

frame_entry = Frame(root)

#  TODO: need to update this list per unit list.
#unitList = list(unitDic.keys())


variable_1 = StringVar(frame_entry)
variable_1.set(unitList[1]) # default value is Lengh Units
variable_2 = StringVar(frame_entry)
variable_2.set(unitList[2]) # default value

unit_1 = OptionMenu(frame_entry, variable_1, *unitList)   #   use "*"  + list
unit_2 = OptionMenu(frame_entry, variable_2, *unitList)

label_1 = Label(frame_entry, text='Input')
button = Button(frame_entry, text='Convert', command = run)
label_2 = Label(frame_entry, text='Result')

entry_1 = Entry(frame_entry,)
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
