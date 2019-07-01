import tkinter as tk


root = tk.Tk()
root.title('Calculator')

exp = tk.StringVar()
ans = tk.StringVar()
state = ''
todelete = False
syms = {'÷':'/','×':'*','%':'*0.01'}

# Main GUI
#-----------------------------------------------------------------------------
scnfrm = tk.Frame(root,width = 300, height = 50)
scnfrm.grid(row = 0, column = 0)

display = tk.Entry(scnfrm,bd=0, width = 21,highlightthickness=0,bg='#AAAAAA',textvariable = exp,font=('Helvetica',25),relief=tk.FLAT)
display.grid(row = 0, column = 0)
display.focus()
display.insert(tk.END,exp)

anscr = tk.Label(scnfrm,bd=0,bg='#AAAAAA',anchor=tk.E, width = 21, textvariable = ans, font=('Helvetica',25))
anscr.grid(row = 1, column = 0)

bodyfrm = tk.Frame(root)
bodyfrm.grid(row = 1, column = 0)
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
            display.icursor(i+1)
        else:
            if symbol.isdigit():
                state = ''
                todelete = False
                enter(symbol)  
            else:
                todelete = False
                enter(symbol)
    ans.set('')
            
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
        
    return str(eval(expr))
    
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
    
#-----------------------------------------------------------------------------

        



display.bind_all('<KeyPress>',keytyped)
exp.set('')
ans.set('')

def button(symbol,position,span=1,height = 80,width = 80,func = None):
    ss = tk.Frame(bodyfrm,height=height,width=width)
    ss.grid(row = position[0],column = position[1],rowspan=span)
    ss.propagate(False)
    
    btn = tk.Button(ss,text=symbol,bg='#222222',fg='#EEEEEE',font=('Arial',15))
    btn.pack(expand=True,fill=tk.BOTH)
    if func == None:
        btn['command'] = lambda:enter(symbol)
    else:
        btn['command'] = func
    

# Buttons

button('9',(0,0))
button('8',(0,1))
button('7',(0,2))
button('Del',(0,3),func = delete)
button('AC',(0,4),func = ac)



button('6',(1,0))
button('5',(1,1))
button('4',(1,2))
button('×',(1,3))
button('÷',(1,4))



button('3',(2,0))
button('2',(2,1))
button('1',(2,2))
button('+',(2,3),span=2,height=160)
button('-',(2,4))

button('.',(3,0))
button('0',(3,1))
button('%',(3,2))
button('=',(3,4),func = equal)


root.update()
tk.mainloop()
