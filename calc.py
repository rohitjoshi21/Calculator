import tkinter as tk

root = tk.Tk()

exp = tk.StringVar()

def nine():
    exp.set(exp.get()+'9')
def eight():
    exp.set(exp.get()+'8')
def seven():
    exp.set(exp.get()+'7')
def six():
    exp.set(exp.get()+'6')
def five():
    exp.set(exp.get()+'5')
def four():
    exp.set(exp.get()+'4')
def three():
    exp.set(exp.get()+'3')
def two():
    exp.set(exp.get()+'2')
def one():
    exp.set(exp.get()+'1')
def zero():
    exp.set(exp.get()+'0')
def mult():
    exp.set(exp.get()+'*')
def add():
    exp.set(exp.get()+'+')
def sub():
    exp.set(exp.get()+'-')
def div():
    exp.set(exp.get()+'/')
def equal(*args):
    exp.set(eval(exp.get()))
def ac():
    exp.set('')
def delt():
    exp.set(exp.get()[:-1])
    
scnfrm = tk.Frame(root,width = 300, height = 50)
scnfrm.grid(row = 0, column = 0)

display = tk.Entry(scnfrm, width = 20,textvariable = exp,font=('Helvetica',25))
display.grid(row = 0, column = 0)
display.focus()
display.bind('<Return>',equal)
display.insert(tk.END,exp)

bodyfrm = tk.Frame(root, width = 300, height = 400)
bodyfrm.grid(row = 1, column = 0)

exp.set('')

#buttons
def button(symbol,position,func = None,span=1,height = 3,width = 5):
    btn = tk.Button(bodyfrm,height = height,width = width,text=symbol,command=func)
    btn.grid(row = position[0],column = position[1],rowspan=span)




button('9',(0,0),nine)
button('8',(0,1),eight)
button('7',(0,2),seven)
button('Del',(0,3),delt)
button('AC',(0,4),ac)



button('6',(1,0),six)
button('5',(1,1),five)
button('4',(1,2),four)
button('X',(1,3),mult)
button('/',(1,4),div)



button('3',(2,0),three)
button('2',(2,1),two)
button('1',(2,2),one)
button('+',(2,3),add,span=2,height=7)
button('-',(2,4),sub)

button(' ',(3,0))
button('0',(3,1),zero)
button(' ',(3,2))
button('=',(3,4),equal)


root.update()
tk.mainloop()
