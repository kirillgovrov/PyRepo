from tkinter import *

# функция для переброса информации с первой строки во вторую
def show():
    password = inputbox.get()
    lowercase = False
    uppercase = False
    digit = False
    for symbol in password:
        if symbol.isdigit():
            digit = True
        elif symbol.isalpha():
            if symbol.islower():
                lowercase = True
            elif symbol.isupper():
                uppercase = True
    # # два способа:
    # if lowercase and uppercase and digit:
    #     label2.config(text='Password is correct', fg='green')
    #     # label2['text'] = 'Password is correct'
    #     # label2['fg'] = 'green'
    # else:
    #     label2.config(text='The password is incorrect', fg='red')
    #     # label2['text'] = "The password is incorrect"
    #     # label2['fg'] = 'red'

    if lowercase and uppercase and digit:
        label2.config(text='Password is correct', fg='green')
    elif lowercase==False and uppercase and digit:
        label2.config(text='Not enough lowercase letter', fg='red')
    elif lowercase and uppercase==False and digit:
        label2.config(text='Not enough uppercase letter', fg='red')
    elif lowercase and uppercase and digit==False:
        label2.config(text='Not enough numbers', fg='red')
    else:
        label2.config(text='Password is incorrect', fg='red')



# настройки темной темы
def darkmode():
    window.config(bg='#353535')
    passwordbox.config(bg='#353535',fg='white')
    label1.config(bg='#353535',fg='white')
    label2.config(bg='#353535')
    showbutton1.config(bg='#535353',fg='white')
    showbutton2.config(bg='#535353',fg='white',state='disabled')


# поле
window = Tk()
window.geometry('400x300')
window.resizable(False, False)
window.title('Password checking2.0')
# местоположение = центр
cenframe = Frame(window)
cenframe.pack(expand=True)

# Создание самой рамки
passwordbox = LabelFrame(cenframe, text="Password", width=200, height=45)
passwordbox.pack()


# 1.надписи для понимания,что вписывать в строку для пользователя=label-ы
label1 = Label(passwordbox, text='Enter password')
label1.pack(padx='35', pady='10')
# 1.строка для пользователя = input = Entry
inputbox = Entry(passwordbox,width='13',show='*',justify=CENTER,
                                    # insertbackground = курсор
                bg='black',fg='white',insertbackground='white')
inputbox.pack()

# 2.надписи для понимания,что вписывать в строку для пользователя=label-ы
label2 = Label(passwordbox)
label2.pack()


# создание кнопки
showbutton1 = Button(passwordbox, text='Show', width='13',command=show)
showbutton1.pack(pady='7')

showbutton2 = Button(passwordbox, text='Night mode', width='13', command=darkmode)
showbutton2.pack(pady='5')

mainloop()