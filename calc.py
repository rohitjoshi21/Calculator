#!/usr/bin/python3

import tkinter as tk
import math
import re

root = tk.Tk()
root.title('Calculator')

exp = tk.StringVar()
ans = tk.StringVar()
state = ''
todelete = False
syms = {'÷':'/','×':'*','%':'*0.01','^':'**','MOD':'%'}

# Main GUI
#-----------------------------------------------------------------------------

master = tk.Frame(root,width=400,height=600,bd=10,bg='#9AC')
master.grid(row = 0, column = 0)
master.propagate(False)

#Display Screen
scnfrm = tk.Frame(master,width=380,height=100,relief=tk.SUNKEN,bd=4)
scnfrm.grid(row = 0, column = 0,pady=10,padx=10)
scnfrm.propagate(False)

display = tk.Entry(scnfrm,bd=0,highlightthickness=0,bg='#AAAAAA',textvariable = exp,font=('Helvetica',25))
display.pack(expand=True,fill=tk.BOTH)
display.focus()

anscr = tk.Label(scnfrm,bd=0,bg='#AAAAAA',anchor=tk.E, width = 21, textvariable = ans, font=('Helvetica',25))
anscr.pack(expand=True,fill=tk.BOTH)

#-----------------------------------------------------------------------------


#Functions
#-----------------------------------------------------------------------------
def enter(symbol,keyboard = False):
    global state, todelete
    i = display.index(tk.INSERT)
    if symbol == None:
        exp.set(state)
    else:
        if keyboard:
            if symbol in syms.values():
                symbol = list(syms.keys())[list(syms.values()).index(symbol)]
            i -= 1
            
        if not todelete:
            state = state[:i] + symbol + state[i:]
            exp.set(state) 
            display.icursor(i+len(symbol))
        else:
            if symbol.isdigit():
                state = ''
                todelete = False
                enter(symbol)  
            else:
                todelete = False
                enter(symbol)
    ans.set('')

def keytyped(event):
    global state
    if len(event.keysym) > 1:
        if event.keysym == 'Return' or event.keysym == 'KP_Enter':
            equal()
            key = None
        elif event.keysym == 'BackSpace':
            delete(True)
            key = None
        else:
            key = event.char if len(event.char) == 1 else None
    else:
        key = event.keysym
    if key != None:
        if key.isalpha():
            enter(None)
        else:
            enter(key,True)
            
def equal(*args):
    global state, todelete
    try:
        ans.set(solve(state))
    except:
        ans.set('Syntax Error')
    todelete = True

def solve(expr):
    for z in syms:
        expr = expr.replace(z,syms[z])
    if '!' in expr:
        pass
    ans = eval(expr)
    return str(int(ans)) if ans == int(ans) else str(ans)
    
def ac():
    global state
    state = ''
    exp.set(state)
    ans.set('')
    
def delete(keyboard = False):
    i = display.index(tk.INSERT) - 1
    if keyboard:
        i += 1
    global state
    state = state[:i]+state[i+1:]
    exp.set(state)
    display.icursor(i)
    ans.set('')
    

    
#-----------------------------------------------------------------------------

        

display.bind_all('<KeyPress>',keytyped)
exp.set('')
ans.set('')

bodyfrm = tk.Frame(master,relief=tk.FLAT,bd=2)
bodyfrm.grid(row = 1, column = 0)

def button(symbol,position,rspan=1,height = 80,width = 80,func = None):
    ss = tk.Frame(bodyfrm,height=height*rspan,width=width)
    ss.grid(row = position[0],column = position[1],rowspan=rspan)
    ss.propagate(False)
    
    btn = tk.Button(ss,text=symbol,bg='#222222',fg='#EEEEEE',font=('Arial',15))
    btn.pack(expand=True,fill=tk.BOTH)
    if func == None:
        btn['command'] = lambda:enter(symbol)
    else:
        btn['command'] = func
    

# Buttons
x = 0

button('(',(x,0))
button(')',(x,1))
button('^',(x,2))
button('!',(x,3))
button(' MOD ',(x,4))

x += 1
button('7',(x,0))
button('8',(x,1))
button('9',(x,2))
button('Del',(x,3),func = delete)
button('AC',(x,4),func = ac)


x += 1
button('4',(x,0))
button('5',(x,1))
button('6',(x,2))
button('×',(x,3))
button('÷',(x,4))


x += 1
button('1',(x,0))
button('2',(x,1))
button('3',(x,2))
button('+',(x,3),rspan=2)
button('-',(x,4))

x += 1
button('.',(x,0))
button('0',(x,1))
button('%',(x,2))
button('=',(x,4),func = equal)


#buttons = [['7',],rspan=1,func=None],]

root.update()
tk.mainloop()
