from tkinter import*
from tkinter import filedialog
# поле
window = Tk()
window.geometry('350x550')
window.resizable(False, False)
window.title('To-do list')

todos  = 0

def add():
    # автоматическая нумерация
    global todos
    todos+=1
    # ввод данных одной строки + другая
    text = str(todos)+ '. ' + what.get() + '\t'*3 + when.get() + '\n'
    todolist.insert(END, text)
    # автоматическое очищение
    what.delete(0,END)
    when.delete(0,END)

# очистка всего списка дел
def clear():
    todolist.delete(0.0, END)

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title='Save file',
                                    filetypes=(('txt files', '*.txt'),('*all files', '*.*')))
    if file:
        file.write(text)

def load():
    todolist.delete(0.0,END)
    file = filedialog.askopenfile(title='Select file',
        filetypes=(('txt files', '*.txt'),('all files', '*.*')))
    text = file.read()
    todolist.insert(END,text)

# Создание самой рамки
passwordbox = LabelFrame(text="Record of an important matter", width=300, height=120)
passwordbox.pack(pady=10)

# 1.надписи для понимания,что вписывать в строку для пользователя=label-ы
Label(passwordbox, text='What deal').grid(padx=10,pady=5,row=0,column=0)
what = Entry(passwordbox,width='20',justify=CENTER,
                                    # insertbackground = курсор
                bg='white',fg='black',insertbackground='black')
what.grid(padx=10,pady=5,row=1,column=0)


# 2.надписи для понимания,что вписывать в строку для пользователя=label-ы
Label(passwordbox, text='When to do').grid(padx=10,pady=5,row=0,column=1)
when = Entry(passwordbox,width='20',justify=CENTER,
                                    # insertbackground = курсор
                bg='white',fg='black',insertbackground='black')
when.grid(padx=10,pady=5,row=1,column=1)


# создание кнопки
button1 = Button(passwordbox, text='Add a new important deal', width='20',command=add)
button1.grid(pady=10,columnspan=2)

todolist = Text(height=17,width=36)
todolist.pack(pady=10)

button2 = Button(text='Delete all deals', width='18',command=clear)
button2.pack(pady=5)

button3 = Button(text='Save',width='10',command=save)
button3.pack(pady=5)

button4 = Button(text='Load',width='10',command=load)
button4.pack(pady=5)

mainloop()