from tkinter import *
from tkinter import messagebox

# окно
window = Tk()
window.geometry('550x300')
window.resizable(False,False)
window.title('Example solver')

def equate():
    try:
        solution = eval(equetion.get())
        messagebox.showinfo('Ready!', f'Solucion found: {solution}')
    except SyntaxError:
        messagebox.showwarning('WARNING', f'You lost something, reconsider the example')
    except NameError:
        messagebox.showerror('Error', f'You wrote something completely wrong')
    except ZeroDivisionError:
        messagebox.showwarning('Seriosly???', f'Are you devide by zero?')

frame = Frame()
frame.pack(pady=40)

label = Label(text='''Enter a mathematical expression from numbers and signs
            + - * / // % **''')
label.pack()

equetion = Entry(width=30)
equetion.pack(pady=20)
equetion.focus()

button = Button(text='Solve example!',width=13,command=equate)
button.pack(pady=12)


window.mainloop()