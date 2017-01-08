from tkinter import *

def createMenu(menu_config, menubar):
    for menu in menu_config:
        menubar.add_cascade(label=menu[0], menu = menu[1])
        for i in menu[2]:
            if i[0] is None:
                menu[1].add_separator()
            else:
                menu[1].add_command(label=i[0])

def addLog(widget, logStr):
    widget['state'] = 'normal'
    if not logStr[-1] == '\n':logStr += '\n'
    widget.insert(END, logStr)
    widget['state'] = 'disabled'
