from tkinter import *

# функция для переброса информации с первой строки во вторую
def show():
    outputbox.delete(0,END)
    password = inputbox.get()
    outputbox.insert(END,password)

# поле
window = Tk()
window.geometry('400x300')
window.resizable(False, False)
window.title('Password checking1.0')
# местоположение = центр
cenframe = Frame(window)
cenframe.pack(expand=True)

# Создание самой рамки
passwordbox = LabelFrame(cenframe, text="Password", width=180, height=45)
passwordbox.pack()


# 1.надписи для понимания,что вписывать в строку для пользователя=label-ы
label1 = Label(passwordbox, text='Enter password')
label1.pack(padx='35', pady='10')
# 1.строка для пользователя = input = Entry
inputbox = Entry(passwordbox,width='10',show='*',justify=CENTER,
                                    # insertbackground = курсор
                bg='black',fg='white',insertbackground='white')
inputbox.pack()

# 2.надписи для понимания,что вписывать в строку для пользователя=label-ы
label2 = Label(passwordbox, text='Your password')
label2.pack()
# 2.строка для пользователя = input = Entry
outputbox = Entry(passwordbox,width='10',justify=CENTER)
outputbox.pack()

# создание кнопки
showbutton = Button(passwordbox, text='Show', width='10',command=show)
showbutton.pack(pady='10')

mainloop()