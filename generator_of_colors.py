from tkinter import *

# окно
window = Tk()
window.geometry()
window.resizable(False,False)
window.title('Colors generator')
window.minsize(550,300)

# функция
def color_generate(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f'#{red:02x}{green:02x}{blue:02x}'
    inverted_color = f'#{255-red:02x}{255-green:02x}{255-blue:02x}'
    label_color.config(bg=color,text=color,fg=inverted_color)

    entry.delete(0,END)
    entry.insert(END,color)


# фрэймы
frame_rgb = LabelFrame(text='Choose color',height=250, width=250)
frame_rgb.place(x='15',y='20')

frame1_rgb = LabelFrame(text='Received color',height=250, width=250)
frame1_rgb.place(x='285',y='20')

# виджеты
label_color = Label(frame1_rgb,font=('Arial',15,'bold'),height=8,width=16,bg='black',fg='white',text='#000000')
label_color.place(x=25,y=15)

red_scale = Scale(frame_rgb,from_=0,to=255,orient=HORIZONTAL,label='Red',
                length=220,width=20,fg='red',activebackground='red',command=color_generate)
red_scale.place(x=5,y=5)

green_scale = Scale(frame_rgb,from_=0,to=255,orient=HORIZONTAL,label='Green',
                    length=220,width=20,fg='green',activebackground='green',command=color_generate)
green_scale.place(x=5,y=70)

blue_scale = Scale(frame_rgb,from_=0,to=255,orient=HORIZONTAL,label='Blue',
                length=220,width=20,fg='blue',activebackground='blue',command=color_generate)
blue_scale.place(x=5,y=140)

# улучшение проги
entry = Entry(frame1_rgb,width=7,font=('Arial',15,'bold'),justify=CENTER)
entry.place(x=80,y=180)

# конец проги
window.mainloop()