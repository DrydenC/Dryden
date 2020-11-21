from tkinter import *

root = Tk()
root.title("Simple Calculator")

def numberClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def addClick():
    global firstNum
    firstNum = int(e.get())
    e.delete(0, END)
    global opvar
    opvar = 1

def subClick():
    global firstNum
    firstNum = int(e.get())
    e.delete(0, END)
    global opvar
    opvar = 2

def multClick():
    global firstNum
    firstNum = int(e.get())
    e.delete(0, END)
    global opvar
    opvar = 3

def equalClick():
    secNum = int(e.get())
    e.delete(0,END)

    if opvar == 1:
        result = firstNum + secNum
    if opvar == 2:
        result = firstNum - secNum
    if opvar == 3:
        result = firstNum * secNum

    e.insert(0, str(result))

def clearClick():
    e.delete(0, END)


e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10)

button1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: numberClick(1))
button2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: numberClick(2))
button3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: numberClick(3))
button4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: numberClick(4))
button5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: numberClick(5))
button6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: numberClick(6))
button7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: numberClick(7))
button8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: numberClick(8))
button9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: numberClick(9))
button0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: numberClick(0))
buttonPlus = Button(root, text = '+', padx = 40, pady = 20, command = addClick)
buttonMinus = Button(root, text = '-', padx = 40, pady = 20, command = subClick)
buttonMulti = Button(root, text = '*', padx = 40, pady = 20, command = multClick)
buttonClear = Button(root, text = 'clear', padx = 30, pady = 20, command = clearClick)
buttonEqual = Button(root, text = '=', padx = 40, pady = 20, command = equalClick)

button1.grid(row = 1, column = 0)
button2.grid(row = 1, column = 1)
button3.grid(row = 1, column = 2)
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
button7.grid(row = 3, column = 0)
button8.grid(row = 3, column = 1)
button9.grid(row = 3, column = 2)
button0.grid(row = 4, column = 0)
buttonPlus.grid(row = 4, column = 1)
buttonMinus.grid(row = 4, column = 2)
buttonMulti.grid(row = 5, column = 0)
buttonEqual.grid(row = 5, column = 1)
buttonClear.grid(row = 5, column = 2)

root.mainloop()