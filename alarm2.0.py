from tkinter import *
import random

# поле
window = Tk()
window.geometry()
window.resizable(True, True)
window.title('Alarm')
window.minsize(220,330)


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

def delete_alarms():
    indexes = alarmbox.curselection()
    indexes = indexes[::-1]
    for indexes in indexes:
        alarmbox.delete(ACTIVE)
    status.config(text=f'Total alarms: {alarmbox.size()}')

def open_change_window():
    global newalarm, change_window
    change_window = Toplevel()
    change_window.title('Change')
    change_window.geometry('300x125')
    change_window.resizable(False,False)
    chlabel = Label(change_window,text='Enter a new alarm value')
    chlabel.pack(pady=10)
    newalarm = Entry(change_window,width='15',justify=CENTER)
    newalarm.pack(pady=7)
    chbutton = Button(change_window,text="Save",width=10,command=change_alarm)
    chbutton.pack(pady=10)
    newalarm.insert(END, alarmbox.get(ACTIVE))

def change_alarm():
    alarmbox.delete(ACTIVE)
    alarmbox.insert(ACTIVE, newalarm.get())
    change_window.destroy()

label1 = Label(text='Alarm')
label1.pack()

status = Label()
status.pack(pady=5)

alarmbox = Listbox(width=30,height=10,justify=CENTER,selectmode=EXTENDED)
alarmbox.pack()


button1 = Button(text='Random alarm',width=12,command=generate_alarms)
button1.pack(pady=7)

button2 = Button(text='Delete alarm',width=10,command=delete_alarms)
button2.pack(pady=5)

button3 = Button(text='Change the alarm',width=14,command=open_change_window)
button3.pack(pady=5)

mainloop()