import tkinter as tk

root = tk.Tk()

exp = tk.StringVar()
state = ''
todelete = False

def enter(symbol):
    global state, todelete
    if not todelete:
        state = state + symbol
        exp.set(state)
    else:
        if symbol.isdigit():
            state = ''
            todelete = False
            enter(symbol)  
        else:
            todelete = False
            enter(symbol)
            
def equal(*args):
    global state, todelete
    try:
        state = str(eval(exp.get()))
        exp.set(state)
    except:
        exp.set('Syntax Error')
    todelete = True
    
def ac():
    global state
    state = ''
    exp.set(state)
    
def delete():
    global state
    state = state[:-1]
    exp.set(state)
    state = ''
    
def keytyped(event):
    global state
    #print(event)
    if len(event.keysym) > 1:
        if event.keysym == 'Return' or event.keysym == 'KP_Enter':
            equal()
            key = None
        else:
            key = event.char if len(event.char) == 1 else None
    else:
        key = event.keysym
    if key != None: 
        enter(key)
    
        
scnfrm = tk.Frame(root,width = 300, height = 50)
scnfrm.grid(row = 0, column = 0)

display = tk.Entry(scnfrm, width = 20,textvariable = exp,font=('Helvetica',25))
display.grid(row = 0, column = 0)
display.focus()
display.bind_all('<KeyPress>',keytyped)
display.insert(tk.END,exp)

bodyfrm = tk.Frame(root, width = 300, height = 400)
bodyfrm.grid(row = 1, column = 0)

exp.set('')

def button(symbol,position,span=1,height = 3,width = 5,func = None):
    
    btn = tk.Button(bodyfrm,height = height,width = width,text=symbol)
    btn.grid(row = position[0],column = position[1],rowspan=span)
    if func == None:
        btn['command'] = lambda:enter(symbol)
    else:
        btn['command'] = func
    


button('9',(0,0))
button('8',(0,1))
button('7',(0,2))
button('Del',(0,3),func = delete)
button('AC',(0,4),func = ac)



button('6',(1,0))
button('5',(1,1))
button('4',(1,2))
button('X',(1,3))
button('/',(1,4))



button('3',(2,0))
button('2',(2,1))
button('1',(2,2))
button('+',(2,3),span=2,height=7)
button('-',(2,4))

button(' ',(3,0))
button('0',(3,1))
button(' ',(3,2))
button('=',(3,4),func = equal)


root.update()
tk.mainloop()
