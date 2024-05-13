from tkinter import *
import random

# поле
window = Tk()
window.geometry()
window.resizable(True, True)
window.title('Alarm')
window.minsize(220,300)


# функция
def generate_alarms():
    alarms = []
    a = 0
    b = 5
    for i in range(10):
        alarmbox.delete(0,END)
        rt = random.randint(a,b)
        if len(str(rt))==1:
            alarms.append(f'07:0{rt}')
        else:
            alarms.append(f'07:{rt}')
    alarmbox.insert(END,*alarms)
    status.config(text=f'Total alarms: {alarmbox.size()}')

# функция
def delete_alarms():
    indexes = alarmbox.curselection()
    indexes = indexes[::-1]
    for indexes in indexes:
        alarmbox.delete(ACTIVE)
    status.config(text=f'Total alarms: {alarmbox.size()}')


# названия кнопок
label1 = Label(text='Alarm')
label1.pack(pady=5)

status = Label()
status.pack(pady=5)

alarmbox = Listbox(width=30,height=10,justify=CENTER,selectmode=EXTENDED)
alarmbox.pack(pady=5)


button1 = Button(text='Random alarm',width=12,command=generate_alarms)
button1.pack(pady=7)

button2 = Button(text='Delete alarm',width=10,command=delete_alarms)
button2.pack(pady=5)

# завершение
mainloop()