from tkinter import *
from random import randint

# окно
window = Tk()
window.geometry('400x310')
window.resizable(False,False)
window.title('Sticks')
sticks = 20

# функции
def player():
    global sticks
    remove_label_sticks = int(entry_sticks.get())
    if remove_label_sticks in [1,2,3] and remove_label_sticks<sticks:
        sticks-=remove_label_sticks
        label_sticks.config(text=sticks*'|')
        status.config(text=sticks)
        if sticks==1:
            status.config(text='You are winner',fg='green')
        else:
            label_move.config(text='Computer move, please wait')
            window.after(2000, computer)


def computer():
    global sticks
    rannum = randint(1,3)
    sticks-=rannum
    label_sticks.config(text=sticks*'|')
    status.config(text=sticks)
    if sticks==1:
        status.config(text='Computer are winner',fg='red')
    label_move.config(text='Enter a number from 1 to 3')


# виджеты
label_move = Label(text='Enter a number from 1 to 3', font=('Arial','15','bold'))
label_move.pack(pady=15)

entry_sticks = Entry(width=15,justify=CENTER,font=('Arial',15, 'bold'))
entry_sticks.pack(pady=5)

label_sticks = Label(text=sticks*'|', font=('Arial', 30, 'bold'))
label_sticks.pack(padx=10,pady=10)

status = Label(text=sticks, font=('Arial', 30, 'bold'))
status.pack(pady=7)

button = Button(text='Take sticks',font=('Arial', 15, 'bold'),command=player)
button.pack(pady=10)

# конец проги
window.mainloop()