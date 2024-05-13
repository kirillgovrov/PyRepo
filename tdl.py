from tkinter import *
from tkinter import filedialog

window = Tk()
# window.geometry('300x450')
window.title('Список дел')
#window.resizable(False, False)

padx = 10
pady = 10
todos = 0

def add():
    # <Автоматическая нумерация>
    global todos
    todos += 1
    # </Автоматическая нумерация>
    text = str(todos) + '. ' + what.get() + '\t'*3 + when.get() + '\n'
    todolist.insert(END, text)
    # <Автоматическое очищение>
    what.delete(0, END)
    when.delete(0, END)
    # </Автоматическое очищение>

def clear():
    todolist.delete(0.0, END)

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title="Save file",
                                    filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    if file:
        file.write(text)


def load():
    todolist.delete(0.0, END)
    file = filedialog.askopenfile(title="Select file",
        filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
    text = file.read()
    todolist.insert(END, text)


frame1 = LabelFrame(text='Записать важное дело')
frame1.pack(padx=padx, pady=pady)

Label(frame1, text='Какое дело').grid(row=0, column=0, padx=7, pady=5)
Label(frame1, text='Когда нужно сделать').grid(row=0, column=1, padx=7, pady=5)

what = Entry(frame1)
what.grid(row=1, column=0, padx=7, pady=5)

when = Entry(frame1)
when.grid(row=1, column=1, padx=7, pady=5)

button = Button(frame1, text='Добавить новое важное дело', command=add)
button.grid(row=2, column=0, columnspan=2, padx=7, pady=5)

todolist = Text(height=15, width=15, wrap=WORD)
todolist.pack(padx=padx, pady=pady, fill=X)

deletebutton = Button(text='Удалить все дела', command=clear)
deletebutton.pack(padx=padx, pady=pady)

Button(text='Сохранить', command=save).pack(padx=padx, pady=pady)
Button(text='Загрузить', command=load).pack(padx=padx, pady=pady)


window.mainloop()