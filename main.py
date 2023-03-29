from ONE__AGAINST__ALL import mod_1
from NUAR__WITHOUT__CARDS import mod_2
from DETECTIVE__AGAINST__THIEF import mod_3


def change_n(i):
    global n, window
    n = i
    window.destroy()


while True:
    import tkinter as tk
    window = tk.Tk()
    n = 0
    # print(window.winfo_screenwidth())
    # print(window.winfo_screenheight())
    window.attributes("-fullscreen", True)
    window.geometry("1650x900")
    window['bg'] = "#72F011"
    window.title("НУАР без карт")
    window.image = tk.PhotoImage(file="Background3.png")
    bg_logo = tk.Label(window, image=window.image)
    bg_logo.place(x=0, y=0)
    begin_topic = tk.Label(text="ДОБРО ПОЖАЛОВАТЬ В МЕНЮ!",font=('Arial, 50'),bg="#DAA520")
    begin_topic.place(x=250, y=50)
    m_1 = tk.Button(text="ОДИН ПРОТИВ ВСЕХ",font=('Arial, 15'),bd=20,width=22,height=4,bg = "#DAA520",command=lambda: change_n(1))
    m_2 = tk.Button(text="НУАР БЕЗ КАРТ",font=('Arial, 15'),bd=20,width=22,height=4,bg = "#DAA520",command=lambda: change_n(2))
    m_3 = tk.Button(text="СЫЩИК ПРОТИВ ВОРА",font=('Arial, 15'),bd=20,width=22,height=4,bg = "#DAA520",command=lambda: change_n(3))
    m_4 = tk.Button(text="КРАТКОЕ ОПИСАНИЕ",font=('Arial, 15'),bd=20,width = 22,height=4,bg = "green")
    m_5 = tk.Button(text="ВЫЙТИ ИЗ МЕНЮ",font=('Arial, 15'),bd=20,width = 22,height=4,bg = "#db5a32",command=lambda: window.destroy())
    m_1.place(x=200,y=280)
    m_2.place(x=600,y=280)
    m_3.place(x=1000,y=280)
    m_4.place(x=400, y=530)
    m_5.place(x=800,y=530)
    window.mainloop()
    if n == 1:
        mod_1()
    elif n == 2:
        mod_2()
    elif n == 3:
        mod_3()
    else:
        break