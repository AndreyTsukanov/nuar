def choose():
    global players, size, begin_topic
    import tkinter as tk
    window = tk.Tk()
    # print(window.winfo_screenwidth())
    # print(window.winfo_screenheight())
    window.attributes("-fullscreen", True)
    window.geometry("1650x900")
    window['bg'] = "#72F011"
    window.title("НУАР без карт")
    window.image = tk.PhotoImage(file="Background3.png")
    bg_logo = tk.Label(window, image=window.image)
    bg_logo.place(x=0, y=0)
    
    
    players = 0
    size = 0
    list_players = []
    list_size = []
    
    
    def choose_size(x):
        global size, begin_topic
        size = x
        begin_topic.destroy()
        for i in range(len(list_size)):
            list_size[i].destroy()
        begin_topic = tk.Label(text="Выберите число игроков",font=('Arial, 60'),bg="#DAA520")
        begin_topic.place(x=300, y=100)
        for i in range(2, 7):
            but = tk.Button(text=str(i), width=10,height=4,bg="#DAA520",font=('Arial, 15'),bd=10,command=lambda x=i: choose_players(x))
            but.place(x= -100 + 200*i , y = 400)
            list_players.append(but)
    

    def choose_players(x):
        global players
        players = x
        for i in range(len(list_players)):
            list_players[i].destroy()
        window.destroy()
    
    
    for i in range(3, 7):
        but = tk.Button(text=str(i), width=10,height=4,font=('Arial, 15'),bg = "#DAA520", bd=10,command=lambda x=i: choose_size(x))
        but.place(x=-180 + 200*i , y = 400)
        list_size.append(but)
    begin_topic = tk.Label(text="Выберите размер поля",font=('Arial, 60'),bg="#DAA520")
    begin_topic.place(x=350, y=100)
    

    window.mainloop()