from tkinter import *
import random as rdm

class Main(Frame):
    def __init__(self,root):
        super(Main,self).__init__(root)
        self.startUI()

    def startUI(self):
        btn = Button(root, text="Rock", font=("Times New Roman", 15), command=lambda x=1: self.btn_click(x))
        btn.place(x=50, y=135, width=120, height=50)
        btn2 = Button(root, text="Scissors", font=("Times New Roman", 15), command=lambda x=2: self.btn_click(x))
        btn2.place(x=190, y=135, width=120, height=50)
        btn3 = Button(root, text="Paper", font=("Times New Roman", 15), command=lambda x=3: self.btn_click(x))
        btn3.place(x=330, y=135, width=120, height=50)

        self.lbl = Label(root, text="Start game!", bg="#FFF", font=("Times New Roman", 21, "bold"))
        self.lbl.place(x=5, y=70)
        self.win = self.drow = self.lose = 0
        self.lbl2 = Label(root, justify="left", font=("Times New Roman", 13), 
                          text=f"Wins: {self.win}\nLosses:"f" {self.lose}\nDraws: {self.drow}",bg="#FFF")
        self.lbl2.place(x=5, y=5)


    def btn_click(self, choise):
        comp_choise = rdm.randint(1, 3)
        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="Draw")
        elif choise == 1 and comp_choise == 2 \
            or choise == 2 and comp_choise == 3 \
            or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text="Win")
        else:
            self.lose += 1
            self.lbl.configure(text="Loss")
        self.lbl2.configure(text=f"Wins: {self.win}\nLosses:"f" {self.lose}\nDraws: {self.drow}")
        del comp_choise

if __name__ == '__main__':
    root = Tk()
    root.geometry("500x200")
    root.title("Rock, Scissors, Paper")
    root.resizable(False, False)
    root["bg"] = "#FFF"
    app = Main(root)
    app.pack()
    root.mainloop()