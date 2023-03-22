import tkinter as tk
import random
import copy
import global_class_file_


game = global_class_file_.Game_without_cards()
from global_class_file_ import window_, players, size

        
def kill():
    global dead_label, dead_button, dead_topic
    game.hint_topic.destroy()
    game.hint_label.destroy()
    game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    game.hint_label = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120, y=510)
            global_class_file_.Show(game)
        elif game.Table[game.Clicked_Buttons[-1][0]][game.Clicked_Buttons[-1][1]][2] == 'black':
            game.hint_label.place(x=30,y = 590)
            game.hint_topic.place(x=120, y=510)
            global_class_file_.Show(game)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if abs(game.player_cords[game.player_number - 1][0] - i) > 1 or abs(game.player_cords[game.player_number - 1][1] - j) > 1 or abs(game.player_cords[game.player_number - 1][0] - i) + abs(game.player_cords[game.player_number - 1][1] - j) == 0:
                game.hint_label.place(x=30,y = 590)
                game.hint_topic.place(x=120, y=510)
                global_class_file_.Show(game)
            else:
                game.hint_topic.destroy()
                game.hint_label.destroy()
                game.people_alive -= 1
                game.killed_person = game.Table[i][j][1]
                game.Table[i][j][2] = 'black'
                game.Table[i][j][1] = 0
                if game.killed_person != 0:
                    if game.people_alive >= players:
                        global_class_file_.Show(game)
                        game.player_trophy[game.player_number - 1] += 1
                        global_class_file_.help_with_kill_count(game)
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#DAA520",fg='black')
                        dead_topic.place(x=20,y=488)
                        dead_label = tk.Label(text="Игрок номер " + str(game.player_number) + " убил игрока номер " + str(game.killed_person) + ".\nИгрок номер " + str(game.killed_person) + ", нажмите на кнопку\n'УЗНАТЬ НОВОГО ПЕРСОНАЖА' так,\nчтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'.",width=37,font=('Arial, 15'),bg="#DAA520",fg='black')
                        dead_label.place(x=20,y = 535)
                        dead_button= tk.Button(text="Узнать нового персонажа", height=2, font=('Arial, 15'), bg='silver' ,command=lambda: help_with_spawn())
                        dead_button.place(x=90,y=680)
                    else:
                        global_class_file_.Show(game)
                        game.player_trophy[game.player_number - 1] += 1
                        global_class_file_.help_with_kill_count(game)
                        game.player_cords[game.killed_person - 1] = [-10, -10]
                        game.player_turn.pop(game.player_turn.index(game.killed_person))
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#DAA520",fg='black')
                        dead_topic.place(x=25,y=478)
                        dead_label = tk.Label(text="Игрок номер " + str(game.player_number) + " убил игрока номер " + str(game.killed_person) + ". \nИгрок номер " + str(game.killed_person) + ", Вы не можете\nбольше возродиться, так как\n свободных живых клеток не\nосталось. Нажмите кнопку 'ОК'.",width=37,font=('Arial, 15'),bg="#DAA520",fg='black')
                        dead_label.place(x=25,y = 528)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'), bg='silver',command=lambda: help_with_spawn())
                        dead_button.place(x=170,y=680)
                else:
                    #Q_and_K()
                    game.PLAYERS_NAMES[game.PLAYERS_NAMES.index(game.Table[i][j][0])] = ""
                    global_class_file_.help_for_player_turn(game)
                    global_class_file_.help_with_players_cords(game)
                    global_class_file_.Show(game)
        game.Clicked_Buttons = []

        
def help_with_spawn():
    global dead_button, dead_label, dead_topic, ok_button, name_label
    dead_button.destroy()
    dead_label.destroy()
    dead_topic.destroy()
    if game.people_alive < players:
        global_class_file_.help_for_player_turn(game)
        game.killed_person = 0
    else:
        i = random.randint(0, len(game.PLAYERS_NAMES) - 1)
        while game.PLAYERS_NAMES[i] == "":
            i = random.randint(0, len(game.PLAYERS_NAMES) - 1)
        for x in range(len(game.Table)):
            for y in range(len(game.Table[0])):
                if game.Table[x][y][0] == game.PLAYERS_NAMES[i]:
                    game.player_cords[game.killed_person - 1] = [x, y]
                    game.Table[x][y][1] = game.killed_person
        name = game.PLAYERS_NAMES[i]
        game.PLAYERS_NAMES[i] = ""
        name_label = tk.Label(text="Игрок номер " + str(game.killed_person) + ", Вы играете\n за персонажа " + str(name) + "!\nХорошенько запомните его!",font=('Arial, 20'),bg="#DAA520")
        name_label.place(x=40,y=480)
        ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13), bg='silver',width=20,height=2,command=lambda :func_OK())
        ok_button.place(x=120,y=610)
    game.Clicked_Buttons = []
    global_class_file_.Show(game)


def func_OK():
    global ok_button, name_label
    ok_button.destroy()
    name_label.destroy()
    global_class_file_.help_for_player_turn(game)
    global_class_file_.help_with_players_cords(game)
    game.killed_person = 0
    global_class_file_.Show(game)


def question():
    global dead_button, dead_label, dead_topic
    global name
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    game.hint_label = tk.Label(text="Укажите ячейку персонажа, находящуюся рядом\n с Вашим пресонажем, чтобы опросить его...", 
    font=('Arial, 16'),bg="#DAA520",fg='black')
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=5,y = 590)
            game.hint_topic.place(x=120, y=510)
        else:
            i, j = game.Clicked_Buttons[0][0], game.Clicked_Buttons[0][1]
            if abs(game.player_cords[game.player_number - 1][0] - i) > 1 or abs(game.player_cords[game.player_number - 1][1] - j) > 1 or game.Table[i][j][2] == 'black':
                game.hint_label.place(x=5,y = 590)
                game.hint_topic.place(x=120, y=510)
            else:
                game.hint_topic.destroy()
                game.hint_label.destroy()
                name = game.Table[i][j][0]
                s = []
                for k in range(len(game.Table)):
                    for y in range(len(game.Table[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and game.Table[k][y][1] != 0:
                            s.append(str(game.Table[k][y][1]))
                s.sort()
                dead_topic= tk.Label(text="Вы успешно опросили\n игроков!",font=('Arial, 30'),bg="#DAA520")
                dead_label = tk.Label(text="Рядом с персонажем "+ str(name) + "\nоказались игроки: " + " ".join(s),width=34, font=('Arial, 16'),bg="#DAA520",fg='black')        
                dead_label.place(x=10,y = 600)
                dead_topic.place(x=10,y = 510)
                dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'), bg="silver",command=lambda: help_with_Q())
                dead_button.place(x=180,y=670)
                game.killed_person = 1
        game.Clicked_Buttons = []
        global_class_file_.Show(game)


def help_with_Q():
    global dead_button, dead_label, dead_topic
    dead_label.destroy()
    dead_topic.destroy()
    global_class_file_.help_for_player_turn(game)
    dead_button.destroy()
    game.Clicked_Buttons = []
    global_class_file_.Show(game)
    game.killed_person = 0


# BEGINING
############################################################################
window_.grid_columnconfigure(0, minsize=60)
for i in range(1,11):
    window_.grid_columnconfigure(i, minsize=60)
    window_.grid_rowconfigure(i, minsize=70)
global_class_file_.Show(game)

num = 1
def help_for_begin():
    global num, ok_button, name, name_label, begin_button
    begin_button.destroy()
    game.hint_label.destroy()
    i = random.randint(0, len(game.PLAYERS_NAMES) - 1)
    while game.PLAYERS_NAMES[i] == "":
        i = random.randint(0, len(game.PLAYERS_NAMES) - 1)
    game.player_cords.append([i // size, i % size])
    name = game.PLAYERS_NAMES[i]
    game.Table[i // size][i % size][1] = num
    game.PLAYERS_NAMES[i] = ""
    name_label = tk.Label(text="Игрок номер " + str(num) +", Вы играете\n за персонажа " + str(name) + "!\nХорошенько запомните его!",font=('Arial, 20'),bg="#DAA520")
    name_label.place(x=40,y=350)
    ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :function_OK())
    ok_button.place(x=120,y=510)
    global_class_file_.Show(game)
    game.Clicked_Buttons = []


game.hint_label = tk.Label(text="Игрок номер " + str(1) + ", нажмите на \nкнопку 'УЗНАТЬ ПЕРСОНАЖА',\n чтобы узнать своего персонажа,\n так, чтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'",font=('Arial, 20'),bg="#DAA520")
game.hint_label.place(x=20,y=350)
begin_button = tk.Button(text="Узнать персонажа", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :help_for_begin())
begin_button.place(x=130,y=530)
begin_topic = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg="#DAA520")
begin_topic.place(x=500, y=30)


def function_OK():
    global num, ok_button, begin_button, name_label
    if num < players:
        ok_button.destroy()
        game.hint_label.destroy()
        name_label.destroy()
        num += 1
        game.hint_label = tk.Label(text="Игрок номер " + str(num) + ", нажмите на \nкнопку 'УЗНАТЬ ПЕРСОНАЖА',\n чтобы узнать своего персонажа,\n так, чтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'",font=('Arial, 20'),bg="#DAA520")
        game.hint_label.place(x=20,y=350)
        begin_button = tk.Button(text="Узнать персонажа", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :help_for_begin())
        begin_button.place(x=130,y=530)
    else:
        begin_button.destroy()
        name_label.destroy()
        ok_button.destroy()
        begin()
    game.Clicked_Buttons = []
    global_class_file_.Show(game)


def help_but_function():
    global HELP_BUTTON, name, ok_button
    if game.killed_person == 0:
        HELP_BUTTON.destroy()
        game.hint_label.destroy()
        game.hint_topic.destroy()
        x, y = game.player_cords[game.player_number - 1][0], game.player_cords[game.player_number - 1][1]
        name = game.Table[x][y][0]
        game.hint_label = tk.Label(text="Игрок номер " + str(game.player_number) + ",\n Вы " + str(name) + "!",font=('Arial, 20'),bg="#DAA520")
        game.hint_label.place(x=1280,y=470 + 40 * (players - 4))
        HELP_BUTTON = tk.Button(text="Забыли персонажа?", bd=5, font=('Arial', 10),width=20,height=2,bg="green",command=lambda : help_but_function())
        ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13), bg='silver',width=10,height=2,command=lambda : (ok_button.destroy(), game.hint_label.destroy(), HELP_BUTTON.place(x=1290,y=400 + 40 * (players - 4) + 60)))
        ok_button.place(x=1330,y=550 + 40 * (players - 4))


def begin():
    global HELP_BUTTON
    game.Clicked_Buttons = []
    game.killed_person = 0
    begin_button.destroy()
    game.hint_label.destroy()
    begin_topic.destroy()
    game.turn = tk.Label(text="Ход игрока " + str(game.player_number),font=('Arial, 30'),bg="#DAA520")
    game.turn.place(x=720, y=60)
    game.turn = tk.Label(text="Ход игрока " + str(game.player_number),font=('Arial, 30'),bg="#DAA520")
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
    HELP_BUTTON = tk.Button(text="Забыли персонажа?", bd=5, font=('Arial', 10),width=20,height=2,bg="green",command=lambda : help_but_function())
    HELP_BUTTON.place(x=1290,y=400 + 40 * (players - 4) + 60)
    command_topic = tk.Label(text="Команды:",font=('Arial, 40'),bg="#DAA520")
    command_topic.place(x=100,y=60)
    count_hint = tk.Label(text="Счёт:",font=('Arial, 40'),bg="#DAA520")
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