#!/usr/bin/py

from os import system
from tkinter import *
from utils import *

root = Tk()

#Menu
menubar = Menu(root)
cmdMenu = Menu(menubar, tearoff = 0)

menus = [
    ('Server', Menu(menubar, tearoff = 0), [('Run',), ('Stop',), ('Restart',), (None,None), ('Exit',root.destroy)]),
    ('Database', Menu(menubar, tearoff = 0), [('Migrate',), ('Make Migrations',)]),
    ('Translation', Menu(menubar, tearoff = 0), [('Make Message',), ('Complie Message',), (None, None), ('Import .po file',), ('Import .mo file',)])
]
createMenu(menus, menubar)


root['menu'] = menubar 

title = Label(root, text="Django Server setting", font='Arial')
title.pack()

traffic = Canvas(root, height = 200, bg = 'gray')
traffic.pack(fill = X)

cmdPan = PanedWindow(orient = HORIZONTAL)
cmdPan.pack(expand=0)
cmdPan.add(Label(cmdPan, text="Server Control"))
for cmd in [('Run',),('Stop',), ('Restart',)]:
    cmdPan.add(Button(cmdPan, text=cmd[0]))

databasePan = PanedWindow(orient = HORIZONTAL)
databasePan.pack(expand=1)
databasePan.add(Label(databasePan, text="Database Control"))
for cmd in [('Migrate',)]:
    databasePan.add(Button(databasePan, text=cmd[0]))

log = Text()
log.pack(fill=BOTH, expand=1)
addLog(log, 'Ready.')

root.mainloop()
