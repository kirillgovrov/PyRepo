from tkinter import*
from math import sqrt
from tkinter import messagebox
# поле
window = Tk()
window.geometry('250x300')
window.resizable(False, False)
window.title('Equation solver')

# функция 
def equate():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        D = b**2 - 4*a*c
        if D==0:
            x1 = (-b + sqrt(D)/2*a)
            output.delete('0.0', 'end')
            output.insert('0.0',f'The discriminant is {D}\nx1 = {x1}')
        elif D>=0:
            x1 = (-b + sqrt(D)/2*a) 
            x2 = (-b - sqrt(D)/2*a) 
            output.delete('0.0', 'end')
            output.insert('0.0',f'The discriminant is {D}\nx1 = {x1}\nx2 = {x2}')
        else:
            output.delete("0.0", "end")
            output.insert("0.0", f'The discriminant is {D}\nThe equation has no solutions.')
            messagebox.showinfo('Solution', f'The discriminant is {D}\nThe equation has no solutions.')
    except ValueError:
        output.delete("0.0", "end")
        output.insert("0.0", "Make sure you enter 3 numbers.")



# Создаю рамку
box1 = LabelFrame(text="Enter initial data", width=250, height=40)
box1.pack(pady=10)

entry_a = Entry(box1, width=4)
entry_a.grid(row=0,column=0,padx=5)


label1 = Label(box1, text='x**2+')
label1.grid(row=0, column=1, padx=5)

entry_b = Entry(box1, width=4)
entry_b.grid(row=0,column=3,padx=5)

label2 = Label(box1, text='x+')
label2.grid(row=0, column=4, padx=5)

entry_c = Entry(box1, width=4)
entry_c.grid(row=0,column=5,padx=5)

label2 = Label(box1, text='=0')
label2.grid(row=0, column=6,padx=5,pady=10)

box2 = LabelFrame(text='solution',width=225,height=120)
box2.pack(pady=10)

output = Text(box2, width=25, height=6)
output.pack(padx=10,pady=10)

button = Button(text='Solve the equation', width=15,command=equate)
button.pack(pady=10)

# Создаю окна информации
def entry_a_handler(event):
    message = "Enter the number a"
    messagebox.showinfo('Information', message)

def entry_b_handler(event):
    message = "Enter the number b"
    messagebox.showinfo('Information', message)

def entry_c_handler(event):
    message = "Enter the number c"
    messagebox.showinfo('Information', message)

def text_click_handler(event):
    message = "Field to display the answer"
    messagebox.showinfo("Information", message)

# Связываю функции событий с виджетами Entry
entry_a.bind("<Double-Button-1>", entry_a_handler)
entry_b.bind("<Double-Button-1>", entry_b_handler)
entry_c.bind("<Double-Button-1>", entry_c_handler)
# Связываю функции событий с виджетом Text
output.bind("<Double-Button-1>", text_click_handler)
# Связываю решение примера по кнопке Enter
entry_c.bind("<Return>", lambda event=None: equate())

mainloop()