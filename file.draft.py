from tkinter import *

window = Tk()
window.geometry('450x400')
window.title('Centered Column')

# Создаем пустый Label для центрированного столбца
centered_column = Label(window, text="Centered Column")
centered_column.grid(row=1, column=0, columnspan=2)

# Создаем виджеты в столбцах 0 и 1
widget1 = Label(window, text="Widget 1")
widget2 = Label(window, text="Widget 2")

widget1.grid(row=0, column=0, sticky='w')
widget2.grid(row=0, column=1, sticky='w')



window.mainloop()
