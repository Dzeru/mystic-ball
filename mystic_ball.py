from tkinter import *
import numpy as np
import os

answers = np.array(["Да", "Нет", "Наверное", "Возможно", "Шансы малы", "Шансы высоки", "50/50"])


def get_answer():
    answer = np.random.choice(answers)
    global ball_btn
    ball_btn.config(text=answer)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
root.iconbitmap(resource_path("mystic_ball_logo.ico"))
root.title(u"Mystic Ball (by Dzeru, 2020)")
root.resizable(False, False)
root.geometry("500x500")
ball_img = PhotoImage(file=resource_path("mystic_ball.png"))
ball_btn = Button(text="Задайте вопрос,\nнажмите на шар",
                  font=("Helvetica", 32),
                  fg="white",
                  compound="center",
                  image=ball_img,
                  border="0",
                  command=get_answer)
ball_btn.pack()

root.mainloop()
