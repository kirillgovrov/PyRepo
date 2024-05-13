from tkinter import*
import random
from tkinter import messagebox
import time

# field
window = Tk()
window.geometry('550x300')
window.title('Schulte')
window.resizable(False, False)


def click(event):
    # print(event.widget)
    if numbers_in_order[0]==event.widget['text']:
        numbers_in_order.pop(0)
        # random click
        event.widget.unbind('<Button-1>')
        event.widget['state'] = 'disabled'
        event.widget['bg']='green'
    else:
        messagebox.showerror('Ой', 'Вы ошиблись! Начинаем заново.')
        game_frame.destroy()
        restart()
    if numbers_in_order==[]:
        end_time = time.time()  
        messagebox.showinfo('Congratulations!', f'You are win! Starting over.\nYour time: {round(end_time-start_time, 3)}.')
        game_frame.destroy()
        greeting_frame.pack(expand=True)



def restart():
    global random_numbers, game_frame, numbers_in_order
    # Time
    global start_time
    if messagebox.askyesno('Are you ready?', 'After clicking "Да" the time will be counted down...'):
        start_time = time.time()
    greeting_frame.forget()
    random_numbers = [i for i in range(10)]
    numbers_in_order = [i for i in range(1, 10)]
    random_numbers = [i for i in range(1, 10)]
    random.shuffle(random_numbers)
    game_frame = Frame()
    game_frame.pack(expand=True)
    row = 0
    column = 0

    # function for create a button
    for number in random_numbers:
        button = Button(game_frame, text=number, font=('Arial', 15, 'bold'), width=8, height=3)
        button.grid(row=row, column=column)
        button.bind('<Button-1>', click) 
        column+=1
        if column==3:
            row+=1
            column=0



greeting_frame = Frame()
greeting_frame.pack(expand=True)

label = Label(greeting_frame, text='''Шульте — это простая игра, которая развивает
периферическое зрение, скорость чтения и
реакцию!
Правила игры:
1. Игрок должен быстрее всех выбрать все числа
по порядку от 1 до 9.
2. Если игрок ошибается – игра начинается заново.
3. Побеждает тот, кто быстрее всех справится с
задачей.''', font = ('Arial', 10), justify=LEFT)
label.pack(pady=25)

button = Button(greeting_frame, text="Start the game", command=restart)
button.pack()

def start(event):
    if messagebox.askquestion('Question', 'Are you sure, that you want break the game?'):
        game_frame.destroy()
        greeting_frame.pack(expand=True)
window.bind('<Escape>', start)
mainloop()