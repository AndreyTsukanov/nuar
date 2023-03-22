import tkinter as tk
import copy
import global_class_file_
from global_class_file_ import window_, players, size


game = global_class_file_.ONE_AGAINST_ALL()
game.change_table()

     
def kill():
    global dead_label, dead_button, dead_topic
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
    game.hint_label = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", font=('Arial, 15'),bg=game.bg_,fg='black')
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120,y = 510)
            global_class_file_.Show(game)
        elif game.Table[game.Clicked_Buttons[-1][0]][game.Clicked_Buttons[-1][1]][2] == 'black':
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120,y = 510)
            global_class_file_.Show(game)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if abs(game.player_cords[game.player_number - 1][0] - i) > 1 or abs(game.player_cords[game.player_number - 1][1] - j) > 1 or abs(game.player_cords[game.player_number - 1][0] - i) + abs(game.player_cords[game.player_number - 1][1] - j) == 0:
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120,y = 510)
                global_class_file_.Show(game)
            else:
                game.people_alive -= 1
                game.killed_person = game.Table[i][j][1]
                game.Table[i][j][2] = 'black'
                game.Table[i][j][0] = []
                game.Table[i][j][1] = 0
                for a in range(len(game.Table)):
                    for b in range(len(game.Table[0])):
                        if abs(a - i) > 1 or abs(b - j) > 1:
                            if game.Table[a][b][2] != 'black':
                                game.Table[a][b][0][game.player_number - 1] = 0
                if game.killed_person != 0:
                    if game.people_alive >= players:
                        for x in range(len(game.Table)):
                            for y in range(len(game.Table[0])):
                                if game.Table[x][y][2] != 'black':
                                    game.Table[x][y][0][game.killed_person - 1] = game.killed_person
                        show_empty_table()
                        game.player_trophy[game.player_number - 1] += 1
                        global_class_file_.help_with_kill_count(game)
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg=game.bg_,fg='black')
                        dead_topic.place(x=30,y=500)
                        dead_label = tk.Label(text="Игрок номер " + str(game.player_number) + " убил игрока номер " + str(game.killed_person) + ". \nИгрок номер " + str(game.killed_person) + ", укажите свое \nместо возрождения так, чтобы это никто \nне видел, и нажмите кнопку 'ОК'.",font=('Arial, 15'),bg=game.bg_,fg='black')
                        dead_label.place(x=40,y = 560)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                        dead_button.place(x=180,y=690)
                    else:
                        for x in range(len(game.Table)):
                            for y in range(len(game.Table[0])):
                                if game.Table[x][y][2] != 'black':
                                    game.Table[x][y][0][game.killed_person - 1] = 0
                        show_empty_table()
                        game.player_trophy[game.player_number - 1] += 1
                        global_class_file_.help_with_kill_count(game)
                        game.player_cords[game.killed_person - 1] = [-10, -10]
                        game.player_turn.pop(game.player_turn.index(game.killed_person))
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg=game.bg_,fg='black')
                        dead_topic.place(x=30,y=500)
                        dead_label = tk.Label(text="Игрок номер " + str(game.player_number) + " убил игрока номер " + str(game.killed_person) + ". \nИгрок номер " + str(game.killed_person) + ", Вы не можете больше\n возродиться, так как свободных живых\n клеток не осталось. Нажмите кнопку 'ОК'.",font=('Arial, 15'),bg=game.bg_,fg='black')
                        dead_label.place(x=40,y = 560)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                        dead_button.place(x=180,y=690)
                else:
                    Q_and_K()
                    global_class_file_.help_for_player_turn(game)
                    global_class_file_.help_with_players_cords(game)
                    global_class_file_.Show(game)
        game.Clicked_Buttons = []


def help_with_spawn():
    global dead_button, dead_label, dead_topic
    if game.people_alive < players:
        dead_button.destroy()
        dead_label.destroy()
        dead_topic.destroy()
        Q_and_K()
        global_class_file_.help_for_player_turn(game)
        game.killed_person = 0
    else:
        if len(game.Clicked_Buttons) == 1:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if game.Table[i][j][2] != 'black' and [i, j] not in game.player_cords:
                game.Table[i][j][1] = game.killed_person
                Q_and_K()
                global_class_file_.help_for_player_turn(game)
                global_class_file_.help_with_players_cords(game)
                game.killed_person = 0
                dead_button.destroy()
                dead_label.destroy()
                dead_topic.destroy()
    game.Clicked_Buttons = []
    show_empty_table()
        

def question():
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg=game.bg_)
    game.hint_label = tk.Label(text="Укажите ячейку персонажа, находящуюся\n рядом с Вашим пресонажем,\n чтобы опросить его...", font=('Arial, 16'),bg=game.bg_,fg='black')
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120,y = 510)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if abs(game.player_cords[game.player_number - 1][0] - i) > 1 or abs(game.player_cords[game.player_number - 1][1] - j) > 1 or game.Table[i][j][2] == 'black':
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120,y = 510)
            else:
                s = []
                for k in range(len(game.Table)):
                    for y in range(len(game.Table[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and game.Table[k][y][1] != 0:
                            s.append(game.Table[k][y][1])
                for a in range(len(game.Table)):
                    for b in range(len(game.Table[0])):
                        if game.Table[a][b][2] != 'black':
                            for x in range(1, players + 1):
                                if (abs(a - i) > 1 or abs(b - j) > 1) and x in s:
                                    game.Table[a][b][0][x - 1] = 0
                                elif (abs(a - i) <= 1 and abs(b - j) <= 1) and x not in s:
                                    game.Table[a][b][0][x - 1] = 0
                Q_and_K()
                global_class_file_.help_for_player_turn(game)
        game.Clicked_Buttons = []
        global_class_file_.Show(game)

        
def Q_and_K():
    global players
    for a in range(players):
        for player in range(1, players + 1):
            count = 0
            I, J = -1, -1
            for i in range(len(game.Table)):
                for j in range(len(game.Table[0])):
                    if player in game.Table[i][j][0]:
                        I, J = i, j
                        count += 1
            if count == 1 and I != -1:
                for k in range(len(game.Table[I][J][0])):
                    if k != player - 1:
                        game.Table[I][J][0][k] = 0


def help_but_click(x, y):
    if [x, y] not in game.Clicked_Buttons:
        if game.killed_person == 0:
            but = tk.Button(text=global_class_file_.help_to_show(game.Table[x][y][0]), bd=5,width=7+players-4, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=10, height=4, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        game.Buttons[x][y].destroy()
        game.Buttons[x][y] = but
        but.grid(row=x + 3, column=y+game.k, stick='wens', padx=5, pady=5)
        game.Clicked_Buttons.append([x, y])
    else:
        if game.killed_person == 0:
            but = tk.Button(text=global_class_file_.help_to_show(game.Table[x][y][0]), bd=5,width=10,height=4, font=('Arial', 13), bg=game.Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=10,height=4, font=('Arial', 13), bg=game.Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        game.Buttons[x][y].destroy()
        game.Buttons[x][y] = but
        but.grid(row=x + 3, column=y+game.k, stick='wens', padx=5, pady=5)
        game.Clicked_Buttons.pop(game.Clicked_Buttons.index([x, y]))

            
def show_empty_table():
    global players
    for i in range(len(game.Buttons)):
        for j in range(len(game.Buttons[0])):            
            game.Buttons[i][j].destroy()   
    game.Buttons = []
    for i in range(len(game.Table)):
        game.Buttons.append([])
        for j in range(len(game.Table[0])):
            but = tk.Button(text="", bd=5, font=('Arial', 13), bg =game.Table[i][j][2], fg='black',width=10,height=4, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+game.k, stick='wens', padx=5, pady=5)
            game.Buttons[-1].append(but)

#BEGINING
#####################################################
num = 1
window_.grid_columnconfigure(0, minsize=60)
for i in range(1, 11):
   window_.grid_columnconfigure(i, minsize=60)
   window_.grid_rowconfigure(i, minsize=70)
show_empty_table()


def help_for_begin():
    global num
    if num <= players:
        if len(game.Clicked_Buttons) == 1 and game.Clicked_Buttons[0] not in game.player_cords:
            game.hint_label.destroy()
            game.player_cords.append(game.Clicked_Buttons[0])
            game.Table[game.Clicked_Buttons[0][0]][game.Clicked_Buttons[0][1]][1] = num
            num += 1
            if num <= players:
                game.hint_label = tk.Label(text="Игрок номер " + str(num) + ", укажите \nсвоего персонажа так, чтобы этого \nникто не видел, и нажмте \nкнопку 'Продолжить'",font=('Arial, 20'),bg=game.bg_)
                game.hint_label.place(x=10,y=350)
            else:
                game.hint_label = tk.Label(text="Да начнется игра!",font=('Arial, 40'),bg=game.bg_)
                game.hint_label.place(x=10,y=350)
        show_empty_table()
    else:
        begin()
    game.Clicked_Buttons = []

    
game.hint_label = tk.Label(text="Игрок номер " + str(num) + ", укажите \nсвоего персонажа так, чтобы этого \nникто не видел, и нажмте \nкнопку 'Продолжить'",font=('Arial, 20'),bg=game.bg_)
game.hint_label.place(x=10,y=350)
begin_button = tk.Button(text="Продолжить", bd=5, font=('Arial', 13),fg='red',width=20,height=2,command=lambda :help_for_begin())
begin_button.place(x=140,y=500)
begin_topic = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg=game.bg_)
begin_topic.place(x=500, y=30)


def begin():
    game.Clicked_Buttons = []
    game.killed_person = 0
    begin_button.destroy()
    game.hint_label.destroy()
    begin_topic.destroy()
    game.turn = tk.Label(text="Ход игрока " + str(game.player_number),font=('Arial, 30'),bg=game.bg_)
    game.turn.place(x=720, y=60)
    game.turn = tk.Label(text="Ход игрока " + str(game.player_number),font=('Arial, 30'),bg=game.bg_)
    game.turn.place(x=720, y=60)
    global_class_file_.help_with_kill_count(game)
    K = tk.Button(text="Убить", bd=5, font=('Arial', 10),fg='red', bg='silver',width=20,height=2,command=lambda : kill())
    Q = tk.Button(text="Спросить", bd=5, font=('Arial', 10), fg='red', bg='silver',width=20,height=2, command=lambda : question())
    V = tk.Button(text="Вертикальная Чистка", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : global_class_file_.vertical_clear(game))
    H = tk.Button(text="Горизонтальная Чистка", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : global_class_file_.horizontal_clear(game))
    D = tk.Button(text="Вниз", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : global_class_file_.down(game))
    U = tk.Button(text="Вверх", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : global_class_file_.up(game))
    R = tk.Button(text="Вправо", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : global_class_file_.right(game))
    L_ = tk.Button(text="Влево", bd=5, font=('Arial', 10), width=20,height=2,fg='red', bg='silver',command=lambda : global_class_file_.left(game))
    C = tk.Button(text="Отменить", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : global_class_file_.cancel_turn(game))
    F = tk.Button(text="Вперёд", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : global_class_file_.forward_turn(game))
    end = tk.Button(text="Завершить Игру", bd=5, font=('Arial', 10),width=20,height=2, bg='red',command=lambda : window_.destroy())
    command_topic = tk.Label(text="Команды:",font=('Arial, 40'),bg=game.bg_)
    command_topic.place(x=100,y=60)
    count_hint = tk.Label(text="Счёт:",font=('Arial, 40'),bg=game.bg_)
    count_hint.place(x=1300,y=100)
    K.place(x=35, y=145)
    Q.place(x=230,y=145)
    V.place(x=230,y=325)
    H.place(x=35, y=325)
    D.place(x=35,y=265)
    U.place(x=230,y=265)
    R.place(x=230, y=205)
    L_.place(x=35,y=205)
    C.place(x=35, y=385)
    F.place(x=230,y=385)
    end.place(x=1290,y=400 + 40 * (players - 4))
    Table_ = copy.deepcopy(game.Table)
    player_turn_ = game.player_turn[:]
    player_cords_ = game.player_cords[:]
    player_trophy_ = game.player_trophy[:]
    PLAYERS_NAMES_ = game.PLAYERS_NAMES[:]
    copy_ = [Table_, player_cords_, player_trophy_, player_turn_, game.player_number, game.people_alive, PLAYERS_NAMES_]
    game.History.append(copy_)
    global_class_file_.Show(game)

    
window_.mainloop()