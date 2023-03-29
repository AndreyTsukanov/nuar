def mod_3():
    import random
    import copy
    import tkinter as tk
    import time
    window_ = tk.Tk()
    window_.attributes("-fullscreen", True)
    window_.geometry("1650x900")
    window_['bg'] = "#72F011"
    window_.title("НУАР без карт")
    window_.image = tk.PhotoImage(file="Background2.png")
    bg_logo = tk.Label(window_, image=window_.image)
    bg_logo.place(x=0, y=0)
    
    size = 5
    players = 2
    
    
    class DVST:
        def __init__(self):
            self.turn = tk.Label()
            self.History = []
            self.bg_ = "#7d6fb3"
            self.Buttons = []
            self.Clicked_Buttons = []
            self.hint_label = tk.Label()
            self.hint_topic= tk.Label()
            self.index_turn = -1
            self.k = 8 + 1 * (size==5) + 2 * (size==4) + 3 * (size==3) - 1 * (size == 7)
            self.Counts = []
            self.detective_cords = []
            self.player_number = 1
            self.Table = [[["", 0, "#ebc923"] for j in range(size)] for k in range(size)]
            self.NAMES = ["Ксавье", "Ирма", "Кэтрин", "Куинтон", "Саймон", "Франклин", "Горацио", "Касим", "Педро", "Джулиан", "Дарнелл", "Ивонн", "Ульбрехт", "Бэррин", "Улис", "Женева",
                      "Картрайт", "Таша", "Маркус", "Фиби", "Закари", "Грейс", "Ванда", "Дейдра", "Рамон", "Эвелин", "Изольда", "Сюзанна", "Райан", "Элисс", "Клайв", "Кристоф", 
                      "Линнетт", "Натан", "Эштон", "Брэнсон", "Мэрион", "Вильгельм", "Эрнест", "Дружок", "Нейл", "Джек", "Офелия", "Флоренс", "Хьюберт", "Владимир", "Винсан", 
                      "Тревор", "Лайнус", "Иван"]
            self.PLAYERS_NAMES = []
            for i in range(size ** 2):
                j = random.randint(0, len(self.NAMES) - 1)
                self.Table[i // size][i % size][0] = self.NAMES[j]
                self.PLAYERS_NAMES.append(self.NAMES[j])
                self.NAMES.pop(j)
            self.players = players
            self.size = size
            self.dict_name = {1: "вора", 2: "сыщика"}
            self.thief_cords = [-10, -10]
            self.rand_list = [i for i in range(size ** 2)]
            self.list_buttons = []
            self.list_ = []
            self.num = 1
            self.steal = tk.Button()
            self.question_ = tk.Button()
            self.change_ = tk.Button()
            self.change_officer = tk.Button()
            self.ok_button = tk.Button()
            self.begin_button = tk.Button()
            

    game = DVST()


    def left():
        help_clear()
        game.hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть влево...", font=('Arial, 15'),bg=game.bg_,fg='black')
        game.hint_topic = tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][0]
            for j in range(len(game.Table[0]) - 1):
                game.Table[n][j], game.Table[n][j + 1] = game.Table[n][j + 1], game.Table[n][j]
            help_for_player_turn()
            help_with_players_cords()
        game.Clicked_Buttons = []
        Show()
    
    
    def down():
        help_clear()
        game.hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкоторый надо сдвинуть вниз...", font=('Arial, 15'),bg=game.bg_,fg='black')
        game.hint_topic = tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][1]
            for i in range(-1, -len(game.Table), -1):
                game.Table[i][n], game.Table[i - 1][n] = game.Table[i - 1][n], game.Table[i][n]
            help_for_player_turn()
            help_with_players_cords()
        game.Clicked_Buttons = []
        Show()
    
    
    def up():
        help_clear()
        game.hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкотороый надо сдвинуть вверх...", font=('Arial, 15'),bg=game.bg_,fg='black')
        game.hint_topic = tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][1]
            for i in range(len(game.Table) - 1):
                game.Table[i][n], game.Table[i + 1][n] = game.Table[i + 1][n], game.Table[i][n]
            help_for_player_turn()
            help_with_players_cords()
        game.Clicked_Buttons = []
        Show()
    
    
    def right():
        help_clear()
        game.hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть вправо...", font=('Arial, 15'),bg=game.bg_,fg='black')
        game.hint_topic = tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][0]
            for j in range(-1, -len(game.Table[0]), - 1):
                game.Table[n][j], game.Table[n][j - 1] = game.Table[n][j - 1], game.Table[n][j]
            help_for_player_turn()
            help_with_players_cords()
        game.Clicked_Buttons = []
        Show()
    
    
    def help_for_player_turn():
        if game.index_turn != -1:
            for i in range(-1, game.index_turn, -1):
                game.History.pop(-1)
        game.index_turn = -1
        game.player_number = game.player_number % 2 + 1
        help_with_player()
        Table_ = copy.deepcopy(game.Table)
        player_number_ = game.player_number
        PLAYERS_NAMES_ = game.PLAYERS_NAMES[:]
        copy_ = [Table_, player_number_, PLAYERS_NAMES_]
        game.History.append(copy_)
    
    
    def Show():
        for i in range(len(game.Buttons)):
            for j in range(len(game.Buttons[0])):
                game.Buttons[i][j].destroy()   
        game.Buttons = []
        for i in range(len(game.Table)):
            game.Buttons.append([])
            for j in range(len(game.Table[0])):
                if game.Table[i][j][1] == 2:
                    but = tk.Button(text=game.Table[i][j][0], bd=15,font=('TimesNewRoman', 13,'underline'), fg="blue", bg = game.Table[i][j][2],width=10,height=4, command=lambda x=i, y=j:help_but_click(x, y))
                else:
                    but = tk.Button(text=game.Table[i][j][0], bd=15, font=('Arial', 13), bg = game.Table[i][j][2], fg='black',width=10,height=4, command=lambda x=i, y=j:help_but_click(x, y))
                but.grid(row=i+3, column=j+game.k, stick='wens', padx=5, pady=5)
                game.Buttons[-1].append(but)
    
    
    def help_but_click(x, y):
        if [x, y] not in game.Clicked_Buttons:
            if game.Table[x][y][1] == 2:
                but = tk.Button(text=game.Table[x][y][0], bd=15,width=10,height=4, font=('TimesNewRoman', 13,'underline'), bg='gray', fg='blue', command=lambda i=x, j=y:help_but_click(i, j))
            else:
                but = tk.Button(text=game.Table[x][y][0], bd=15,width=10, height=4, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
            game.Buttons[x][y].destroy()
            game.Buttons[x][y] = but
            but.grid(row=x + 3, column=y+game.k, stick='wens', padx=5, pady=5)
            game.Clicked_Buttons.append([x, y])
        else:
            if game.Table[x][y][1] == 2:
                but = tk.Button(text=game.Table[x][y][0], bd=15,width=10,height=4, font=('TimesNewRoman', 13,'underline'), bg=game.Table[x][y][2], fg='blue', command=lambda i=x, j=y:help_but_click(i, j))
            else:
                but = tk.Button(text=game.Table[x][y][0], bd=15,width=10,height=4, font=('Arial', 13), bg=game.Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
            game.Buttons[x][y].destroy()
            game.Buttons[x][y] = but
            but.grid(row=x + 3, column=y+game.k, stick='wens', padx=5, pady=5)
            game.Clicked_Buttons.pop(game.Clicked_Buttons.index([x, y]))
        
    
    def help_with_player():
        game.turn.destroy()
        game.turn = tk.Label(text="Ход " + game.dict_name[game.player_number] ,font=('Arial, 30'),bg=game.bg_)
        if game.player_number == 1:
            game.change_officer.destroy()
            game.question_.destroy()
            game.change_ = tk.Button(text="Сменить личность", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : CHANGE_THIEF())
            game.steal = tk.Button(text="Украсть золото", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : STEAL())
            game.change_.place(x=35,y=265)
            game.steal.place(x=230, y=265)
            game.turn.place(x=790, y=60)
        else:
            game.change_.destroy()
            game.steal.destroy()
            game.question_ = tk.Button(text="Опросить", bd=5, font=('Arial', 10), fg='red', bg='silver',width=20,height=2, command=lambda : QUESTION())
            game.change_officer = tk.Button(text="Сменить офицера", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : CHANGE_OFFICER())
            game.change_officer.place(x=35,y=265)
            game.question_.place(x=230, y=265)
            game.turn.place(x=760, y=60)
    
    
    def help_with_players_cords():
        game.hint_topic.destroy()
        game.detective_cords = []
        for i in range(len(game.Table)):
            for j in range(len(game.Table[0])):
                if game.Table[i][j][1] == 1:
                    game.thief_cords = [i, j][:]
                elif game.Table[i][j][1] == 2:
                    game.detective_cords.append([i, j])
    
    
    def cancel_turn():
        help_clear()
        game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        game.hint_label = tk.Label(text="Вы вернулись в начало игры!", 
        font=('Arial, 15'),bg=game.bg_,fg='black')
        if game.index_turn == -len(game.History) or len(game.History) == 1:
            game.hint_label.place(x=90,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            game.index_turn -= 1
            P_1 = copy.deepcopy(game.History[game.index_turn])
            game.Table = copy.deepcopy(P_1[0])
            game.player_number = P_1[1]
            game.PLAYERS_NAMES = P_1[2][:]
            help_with_player()
            help_with_players_cords()            
        Show()
    
    
    def forward_turn():
        help_clear()
        game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        game.hint_label = tk.Label(text="Вы вернулись в конец игры!", 
        font=('Arial, 15'),bg=game.bg_,fg='black')
        if game.index_turn == -1:
            game.hint_label.place(x=90,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            game.index_turn += 1
            P_1 = copy.deepcopy(game.History[game.index_turn])
            game.Table = copy.deepcopy(P_1[0])
            game.player_number = P_1[1]
            game.PLAYERS_NAMES = P_1[2][:]
            help_with_player()
            help_with_players_cords()  
        Show()
    
    
    def CHANGE_THIEF():
        help_clear()
        game.hint_label = tk.Label(text="ВОР! Это твои тайные личности.\nВыбери личность ТАК, ЧТОБЫ\nЭТОГО НИКТО НЕ ВИДЕЛ!",font=('Arial, 20'),bg=game.bg_)
        game.hint_label.place(x=20, y=450)
        for j in range(3):
            but = tk.Button(text=game.list_[j], bd=5, font=('Arial', 13), bg = "black", fg='white',width=10,height=4, command=lambda x=j:(change_thief(game.list_[x]), help_for_begin_3(), help_for_player_turn()))
            game.list_buttons.append(but)
            but.place(x = 20 + j*150, y = 600)
    
    
    def CHANGE_OFFICER():
        help_clear()
        game.hint_label.destroy()
        game.hint_topic.destroy()
        game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        game.hint_label = tk.Label(text="Укажите офицера, которого\n Вы хотите сменить.", 
        font=('Arial, 16'),bg=game.bg_,fg='black')
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if game.Table[i][j][1] != 2:
                game.hint_label.place(x=70,y = 590)
                game.hint_topic.place(x=120, y=510)
            elif game.PLAYERS_NAMES.count("") == game.size ** 2:
                game.hint_label = tk.Label(text="Свободных офицеров не осталось!", font=('Arial, 16'),bg=game.bg_,fg='black')
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120, y=510)
            else:
                game.Table[i][j][1] = 0
                game.detective_cords.pop(game.detective_cords.index([i, j]))
                i = random.choice(game.rand_list)
                while game.PLAYERS_NAMES[i] == "":
                    i = random.choice(game.rand_list)
                name = game.PLAYERS_NAMES[i]
                game.PLAYERS_NAMES[i] = ""
                for i in range(len(game.Table)):
                    for j in range(len(game.Table[0])):
                        if game.Table[i][j][0] == name:
                            game.Table[i][j][1] = 2
                            game.detective_cords.append([i, j])
                game.hint_label = game.hint_label = tk.Label(text=f"СЫЩИК! Ваш новый офицер - {name}", font=('Arial, 16'),bg=game.bg_,fg='black')
                game.hint_label.place(x=30, y=540)
                help_for_player_turn()
                help_with_players_cords()
        game.Clicked_Buttons = []
        Show()
    
    
    def QUESTION():
        help_clear()
        game.hint_label.destroy()
        game.hint_topic.destroy()
        game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        game.hint_label = tk.Label(text="Укажите персонажа (не офицера), \nнаходящегося рядом с Вашими офицерами,\n чтобы допросить его.", font=('Arial, 16'),bg=game.bg_,fg='black')
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            x_1, y_1 = game.detective_cords[0][0], game.detective_cords[0][1]
            x_2, y_2 = game.detective_cords[1][0], game.detective_cords[1][1]
            x_3, y_3 = game.detective_cords[2][0], game.detective_cords[2][1]
            if (abs(x_1 - i) > 1 or abs(y_1 - j) > 1) and (abs(x_2 - i) > 1 or abs(y_2 - j) > 1) and (abs(x_3 - i) > 1 or abs(y_3 - j) > 1):
                game.hint_label = tk.Label(text="Ваши офицеры находятся не рядом\n с выбранным Вами персонажем.", font=('Arial, 16'),bg=game.bg_,fg='black')
                game.hint_label.place(x=40,y = 590)
                game.hint_topic.place(x=120, y=510)
            elif game.Table[i][j][1] == 2:
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120, y=510)
            elif game.Table[i][j][1] == 0:
                game.hint_label = tk.Label(text=f"{game.Table[i][j][0].upper()} не является \nтекущей личностью вора.", font=('Arial, 20'),bg=game.bg_,fg='black')
                game.hint_label.place(x=70,y = 540)
                help_for_player_turn()
            else:
                game.hint_label = tk.Label(text="СЫЩИК ОБНАРУЖИЛ ВОРА!\nСЫЩИК ПОБЕДИЛ!!!", font=('Arial, 25'),bg=game.bg_,fg='black')
                game.hint_label.place(x=10, y=450)
                help_for_player_turn()
        game.Clicked_Buttons = []
        Show()
    
    
    def change_thief(name):
        for i in range(len(game.Table)):
            for j in range(len(game.Table[0])):
                if game.Table[i][j][1] != 2:
                    game.Table[i][j][1] = 0
                if game.Table[i][j][0] == name:
                    game.Table[i][j][1] = 1
                    game.thief_cords = [i, j][:]
    
    
    def help_clear():
        for elem in game.list_buttons:
            elem.destroy()
        game.hint_label.destroy()
        game.hint_topic.destroy()
    
    
    def STEAL():
        help_clear()
        game.hint_label.destroy()
        game.hint_topic.destroy()
        game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
        game.hint_label = tk.Label(text="Укажите ЗОЛОТУЮ ячейку персонажа,\n находящуюся рядом с Вашей тайной\n личностью, чтобы украсть золото.", 
        font=('Arial, 16'),bg=game.bg_,fg='black')
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if game.Table[i][j][2] != '#ebc923':
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120, y=510)
            else:
                x, y = game.thief_cords[0], game.thief_cords[1]
                if abs(x - i) > 1 or abs(y - j) > 1:
                    game.hint_label = tk.Label(text="Ваша тайная личность находится\n не рядом с выбранной золотой клеткой", font=('Arial, 16'),bg=game.bg_,fg='black')
                    game.hint_label.place(x=30,y = 590)
                    game.hint_topic.place(x=120, y=510)
                else:
                    game.Table[i][j][2] = "white"
                    count = 0
                    for i in range(len(game.Table)):
                        for j in range(len(game.Table[0])):
                           count += game.Table[i][j][2] == '#ebc923'
                    if count == 0:
                        game.hint_label = tk.Label(text="ИГРА ЗАВЕРШЕНА!\nВОР УКРАЛ ВСЁ ЗОЛОТО\n И ПОБЕДИЛ!", font=('Arial, 25'),bg=game.bg_,fg='black')
                        game.hint_label.place(x=10, y=450)
                    help_for_player_turn()
        game.Clicked_Buttons = []
        Show()
    
    
    # BEGINING
    ############################################################################
    window_.grid_columnconfigure(0, minsize=60)
    for i in range(1,11):
        window_.grid_columnconfigure(i, minsize=60)
        window_.grid_rowconfigure(i, minsize=70)
    Show()
    game.hint_label = tk.Label(text="СЫЩИК! Нажми на кнопку \n'УЗНАТЬ ДЕТЕКТИВОВ', чтобы\n узнать своих офицеров,\nа затем нажми кнопку 'ОК'",font=('Arial, 20'),bg=game.bg_)
    game.hint_label.place(x=40,y=350)
    game.begin_button = tk.Button(text="Узнать детективов", bd=5, font=('Arial', 13),fg='black', bg='silver',width=20,height=2,command=lambda :help_for_begin_1())
    game.begin_button.place(x=130,y=530)
    begin_topic = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg=game.bg_)
    begin_topic.place(x=550, y=30)
    
    
    def help_for_begin_1():
        game.begin_button.destroy()
        game.hint_label.destroy()
        game.list_ = []
        for k in range(3):
            i = random.choice(game.rand_list)
            while game.PLAYERS_NAMES[i] == "":
                i = random.choice(game.rand_list)
            name = game.PLAYERS_NAMES[i]
            game.Table[i // size][i % size][1] = 2
            game.PLAYERS_NAMES[i] = ""
            game.list_.append(name)
            for i in range(len(game.Table)):
                for j in range(len(game.Table[0])):
                    if game.Table[i][j][0] == name:
                        game.detective_cords.append([i, j])
        game.hint_label = tk.Label(text=f"СЫЩИК! Ваши офицеры - это \n {game.list_[0]}, {game.list_[1]} и {game.list_[2]}!",font=('Arial, 20'),bg=game.bg_)
        game.hint_label.place(x=50,y=350)
        game.ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13),fg='black', bg='silver',width=20,height=2,command=lambda :function_OK())
        game.ok_button.place(x=140,y=480)
        Show()
        game.Clicked_Buttons = []
    
    
    def help_for_begin_2():
        game.list_ = []
        for j in range(3):
            i = random.choice(game.rand_list)
            while game.PLAYERS_NAMES[i] == "":
                i = random.choice(game.rand_list)
            name = game.PLAYERS_NAMES[i]
            game.PLAYERS_NAMES[i] = ""
            game.list_.append(name)
        game.begin_button.destroy()
        game.hint_label.destroy()
        game.hint_label = tk.Label(text="ВОР! Это твои тайные личности.\nВыбери личность ТАК, ЧТОБЫ\nЭТОГО НИКТО НЕ ВИДЕЛ!",font=('Arial, 20'),bg=game.bg_)
        game.hint_label.place(x=50, y=320)
        game.list_buttons = []
        for j in range(3):
            but = tk.Button(text=game.list_[j], bd=5, font=('Arial', 13), bg = "black", fg='white',width=10,height=4, command=lambda x=j:(change_thief(game.list_[x]), help_for_begin_3()))
            game.list_buttons.append(but)
            but.place(x = 50 + j*150, y = 470)
    
    
    def help_for_begin_3():
        for elem in game.list_buttons:
            elem.destroy()
        game.begin_button.destroy()
        game.hint_label.destroy()
        game.ok_button.destroy()
        game.hint_label.destroy()
        begin()
    
    
    def function_OK():
        game.ok_button.destroy()
        game.hint_label.destroy()
        game.hint_label.destroy()
        game.hint_label = tk.Label(text="ВОР! Нажми на кнопку 'УЗНАТЬ\nТАЙНЫХ ЛИЧНОСТЕЙ', чтобы\n узнать своих тайных личностей, ТАК,\nЧТОБЫ ЭТОГО НИКТО НЕ ВИДЕЛ,\nзатем выбери действующую личность.",font=('Arial, 20'),bg=game.bg_)
        game.hint_label.place(x=20,y=330)
        game.begin_button = tk.Button(text="Узнать тайных личностей", bd=5, font=('Arial', 13),fg='black', bg='silver',width=30,height=2,command=lambda :help_for_begin_2())
        game.begin_button.place(x=120,y=530)
        game.Clicked_Buttons = []
        Show()
    
    
    def begin():
        game.Clicked_Buttons = []
        game.begin_button.destroy()
        game.hint_label.destroy()
        begin_topic.destroy()
        game.turn = tk.Label(text="Ход " + game.dict_name[game.player_number] ,font=('Arial, 30'),bg=game.bg_)
        game.turn.place(x=790, y=60)
        game.question_ = tk.Button(text="Опросить", bd=5, font=('Arial', 10), fg='red', bg='silver',width=20,height=2, command=lambda : STEAL())
        game.change_officer = tk.Button(text="Сменить офицера", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : CHANGE_OFFICER())
        game.change_ = tk.Button(text="Сменить личность", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : CHANGE_THIEF())
        game.steal = tk.Button(text="Украсть золото", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : STEAL())
        D = tk.Button(text="Вниз", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : down())
        U = tk.Button(text="Вверх", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : up())
        R = tk.Button(text="Вправо", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : right())
        L_ = tk.Button(text="Влево", bd=5, font=('Arial', 10), width=20,height=2,fg='red', bg='silver',command=lambda : left())
        C = tk.Button(text="Отменить", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : cancel_turn())
        F = tk.Button(text="Вперёд", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : forward_turn())
        end = tk.Button(text="В МЕНЮ", bd=5, font=('Arial', 10),width=20,height=2, bg='red',command=lambda : window_.destroy())
        command_topic = tk.Label(text="Команды:",font=('Arial, 40'),bg=game.bg_)
        command_topic.place(x=100,y=60)
        game.change_.place(x=35, y=265)
        game.steal.place(x=230,y=265)
        D.place(x=35,y=205)
        U.place(x=230,y=205)
        R.place(x=230, y=145)
        L_.place(x=35,y=145)
        C.place(x=35, y=325)
        F.place(x=230,y=325)
        end.place(x=1290,y=400 + 40 * (players - 4))
        Table_ = copy.deepcopy(game.Table)
        PLAYERS_NAMES_ = game.PLAYERS_NAMES[:]
        copy_ = [Table_, game.player_number, PLAYERS_NAMES_]
        game.History.append(copy_)
        Show()
    
    
    window_.mainloop()