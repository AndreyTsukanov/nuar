#import one_against_all
import time
import random
import copy
import tkinter as tk
from tkinter import*
window = tk.Tk()
window.attributes("-fullscreen", True)
window.image = PhotoImage(file="Background.png")
bg_logo = Label(window, image=window.image)
bg_logo.place(x=0, y=0)
#window.geometry("1650x900")
window['bg'] = "#72F011"
window.title("НУАР без карт")
width = 1536
height = 864
#width = window.winfo_screenwidth()
#height = window.winfo_screenheight()


# POINT PLAYERS AND SIZE ON LINES 23, 24
########################################
players = 3
size = 6
########################################
# NEXT FUNCTIONS FOR GAME PROCESS:

        
def horizontal_clear():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="В каждой из " + str(len(Table)) + " строк выберите по одной\n чёрной ячейке для горизонтальной очистки...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Table):
            hint_label.place(x=30,y = 590)
            hint_topic.place(x=120, y=510)
        else:
            a = set()
            for j in range(len(Table)):
                if Table[Clicked_Buttons[-j-1][0]][Clicked_Buttons[-j-1][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j-1][0])
            if len(a) != len(Table):
                hint_label.place(x=30,y = 590)
                hint_topic.place(x=120, y=510)
            else:        
                for i in range(1, len(Table) + 1):
                    (Table[Clicked_Buttons[-i][0]]).pop(Clicked_Buttons[-i][1])
                help_for_player_turn()
                help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def vertical_clear():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="В каждом из " + str(len(Table[0])) + " столбцов выберите по одной \nчёрной ячейке для вертикальной очистки...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Table[0]):
            hint_label.place(x=30,y = 590)
            hint_topic.place(x=120, y=510)
        else:
            a = set()
            for j in range(1, len(Table[0]) + 1):
                if Table[Clicked_Buttons[-j][0]][Clicked_Buttons[-j][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j][1])
            if len(a) != len(Table[0]):
                hint_label.place(x=30,y = 590)
                hint_topic.place(x=120, y=510)
            else:
                P_1 = [[Table[i][j] for i in range(len(Table))] for j in range(len(Table[0]))]
                for i in range(1, len(Table[0]) + 1):
                    (P_1[Clicked_Buttons[-i][1]]).pop(Clicked_Buttons[-i][0])
                Table = [[P_1[i][j] for i in range(len(P_1))] for j in range(len(P_1[0]))]
                help_for_player_turn()
                help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def down():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкоторый надо сдвинуть вниз...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=70, y=590)
            hint_topic.place(x=120, y=510)
        else:
            n = Clicked_Buttons[-1][1]
            for i in range(-1, -len(Table), -1):
                Table[i][n], Table[i - 1][n] = Table[i - 1][n], Table[i][n]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def up():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкотороый надо сдвинуть вверх...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=70, y=590)
            hint_topic.place(x=120, y=510)
        else:
            n = Clicked_Buttons[-1][1]
            for i in range(len(Table) - 1):
                Table[i][n], Table[i + 1][n] = Table[i + 1][n], Table[i][n]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def left():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть влево...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=70, y=590)
            hint_topic.place(x=120, y=510)
        else:
            n = Clicked_Buttons[-1][0]
            for j in range(len(Table[0]) - 1):
                Table[n][j], Table[n][j + 1] = Table[n][j + 1], Table[n][j]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def right():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть вправо...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=70, y=590)
            hint_topic.place(x=120, y=510)
        else:
            n = Clicked_Buttons[-1][0]
            for j in range(-1, -len(Table[0]), - 1):
                Table[n][j], Table[n][j - 1] = Table[n][j - 1], Table[n][j]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Table)

        
def kill():
    global Table, Clicked_Buttons, player_number, killed_person, player_cords, dead_label, dead_button, dead_topic
    global hint_topic, hint_label, people_alive, player_trophy, PLAYERS_NAMES
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=30,y = 590)
            hint_topic.place(x=120, y=510)
            Show(Table)
        elif Table[Clicked_Buttons[-1][0]][Clicked_Buttons[-1][1]][2] == 'black':
            hint_label.place(x=30,y = 590)
            hint_topic.place(x=120, y=510)
            Show(Table)
        else:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if abs(player_cords[player_number - 1][0] - i) > 1 or abs(player_cords[player_number - 1][1] - j) > 1 or abs(player_cords[player_number - 1][0] - i) + abs(player_cords[player_number - 1][1] - j) == 0:
                hint_label.place(x=30,y = 590)
                hint_topic.place(x=120, y=510)
                Show(Table)
            else:
                people_alive -= 1
                killed_person = Table[i][j][1]
                Table[i][j][2] = 'black'
                Table[i][j][1] = 0
                if killed_person != 0:
                    if people_alive >= players:
                        Show(Table)
                        player_trophy[player_number - 1] += 1
                        help_with_kill_count()
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#DAA520",fg='black')
                        dead_topic.place(x=20,y=488)
                        dead_label = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed_person) + ".\nИгрок номер " + str(killed_person) + ", нажмите на кнопку\n'УЗНАТЬ НОВОГО ПЕРСОНАЖА' так,\nчтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'.",width=37,font=('Arial, 15'),bg="#DAA520",fg='black')
                        dead_label.place(x=20,y = 535)
                        dead_button= tk.Button(text="Узнать нового персонажа", height=2, font=('Arial, 15'), bg='silver' ,command=lambda: help_with_spawn())
                        dead_button.place(x=90,y=680)
                    else:
                        Show(Table)
                        player_trophy[player_number - 1] += 1
                        help_with_kill_count()
                        player_cords[killed_person - 1] = [-10, -10]
                        player_turn.pop(player_turn.index(killed_person))
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#DAA520",fg='black')
                        dead_topic.place(x=25,y=478)
                        dead_label = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed_person) + ". \nИгрок номер " + str(killed_person) + ", Вы не можете\nбольше возродиться, так как\n свободных живых клеток не\nосталось. Нажмите кнопку 'ОК'.",width=37,font=('Arial, 15'),bg="#DAA520",fg='black')
                        dead_label.place(x=25,y = 528)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'), bg='silver',command=lambda: help_with_spawn())
                        dead_button.place(x=170,y=680)
                else:
                    #Q_and_K()
                    PLAYERS_NAMES[PLAYERS_NAMES.index(Table[i][j][0])] = ""
                    help_for_player_turn()
                    help_with_players_cords()
                    Show(Table)
        Clicked_Buttons = []

        
def help_with_spawn():
    global player_cords
    global people_alive
    global Clicked_Buttons
    global Table
    global killed_person
    global dead_button, dead_label, dead_topic, ok_button, name_label
    global PLAYERS_NAMES
    dead_button.destroy()
    dead_label.destroy()
    dead_topic.destroy()
    if people_alive < players:
        help_for_player_turn()
        killed_person = 0
    else:
        i = random.randint(0, len(PLAYERS_NAMES) - 1)
        while PLAYERS_NAMES[i] == "":
            i = random.randint(0, len(PLAYERS_NAMES) - 1)
        for x in range(len(Table)):
            for y in range(len(Table[0])):
                if Table[x][y][0] == PLAYERS_NAMES[i]:
                    player_cords[killed_person - 1] = [x, y]
                    Table[x][y][1] = killed_person
        name = PLAYERS_NAMES[i]
        PLAYERS_NAMES[i] = ""
        name_label = tk.Label(text="Игрок номер " + str(killed_person) + ", Вы играете\n за персонажа " + str(name) + "!\nХорошенько запомните его!",font=('Arial, 20'),bg="#DAA520")
        name_label.place(x=40,y=480)
        ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13), bg='silver',width=20,height=2,command=lambda :func_OK())
        ok_button.place(x=120,y=610)
    Clicked_Buttons = []
    Show(Table)


def func_OK():
    global ok_button, name_label, Table, killed_person
    ok_button.destroy()
    name_label.destroy()
    help_for_player_turn()
    help_with_players_cords()
    killed_person = 0
    Show(Table)


def question():
    global Table
    global Clicked_Buttons
    global player_cords
    global killed_person
    global hint_topic, hint_label, dead_button, dead_label, dead_topic
    global name
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Укажите ячейку персонажа, находящуюся рядом\n с Вашим пресонажем, чтобы опросить его...", 
    font=('Arial, 16'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=5,y = 590)
            hint_topic.place(x=120, y=510)
        else:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if abs(player_cords[player_number - 1][0] - i) > 1 or abs(player_cords[player_number - 1][1] - j) > 1 or Table[i][j][2] == 'black':
                hint_label.place(x=5,y = 590)
                hint_topic.place(x=120, y=510)
            else:
                name = Table[i][j][0]
                s = []
                for k in range(len(Table)):
                    for y in range(len(Table[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and Table[k][y][1] != 0:
                            s.append(str(Table[k][y][1]))
                s.sort()
                dead_topic= tk.Label(text="Вы успешно опросили\n игроков!",font=('Arial, 30'),bg="#DAA520")
                dead_label = tk.Label(text="Рядом с персонажем "+ str(name) + "\nоказались игроки: " + " ".join(s),width=34, font=('Arial, 16'),bg="#DAA520",fg='black')        
                dead_label.place(x=10,y = 600)
                dead_topic.place(x=10,y = 510)
                dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'), bg="silver",command=lambda: help_with_Q())
                dead_button.place(x=180,y=670)
                killed_person = 1
        Clicked_Buttons = []
        Show(Table)


def help_with_Q():
    global dead_button, killed_person, dead_label, dead_topic, Clicked_Buttons
    dead_label.destroy()
    dead_topic.destroy()
    help_for_player_turn()
    dead_button.destroy()
    Clicked_Buttons = []
    Show(Table)
    killed_person = 0


def Q_and_K():
    global Table
    global players
    for a in range(players):
        for player in range(1, players + 1):
            count = 0
            I, J = -1, -1
            for i in range(len(Table)):
                for j in range(len(Table[0])):
                    if player in Table[i][j][0]:
                        I, J = i, j
                        count += 1
            if count == 1 and I != -1:
                for k in range(len(Table[I][J][0])):
                    if k != player - 1:
                        Table[I][J][0][k] = 0

                        
def cancel_turn():
    global History
    global Table
    global index_turn
    global killed_person
    global hint_topic, hint_label
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive, PLAYERS_NAMES
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Вы вернулись в начало игры!", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if index_turn == -len(History) or len(History) == 1:
            hint_label.place(x=90,y = 590)
            hint_topic.place(x=120, y=510)
        else:
            index_turn -= 1
            P_1 = copy.deepcopy(History[index_turn])
            Table = copy.deepcopy(P_1[0])
            player_cords = P_1[1][:]
            player_trophy = P_1[2][:]
            player_turn = P_1[3][:]
            player_number = P_1[4]
            people_alive = P_1[5]
            PLAYERS_NAMES = P_1[6][:]
            help_with_player()
            help_with_players_cords()
            help_with_kill_count()
        Show(Table)

        
def forward_turn():
    global History
    global Table
    global index_turn
    global killed_person
    global hint_topic, hint_label
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive, PLAYERS_NAMES
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#DAA520")
    hint_label = tk.Label(text="Вы вернулись в конец игры!", 
    font=('Arial, 15'),bg="#DAA520",fg='black')
    if killed_person == 0:
        if index_turn == -1:
            hint_label.place(x=90,y = 590)
            hint_topic.place(x=120, y=510)
        else:
            index_turn += 1
            P_1 = copy.deepcopy(History[index_turn])
            Table = copy.deepcopy(P_1[0])
            player_cords = P_1[1][:]
            player_trophy = P_1[2][:]
            player_turn = P_1[3][:]
            player_number = P_1[4]
            people_alive = P_1[5]
            PLAYERS_NAMES = P_1[6]
            help_with_player()
            help_with_players_cords()
            help_with_kill_count()
        Show(Table)

        
def help_for_player_turn():
    global History
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive, PLAYERS_NAMES
    global index_turn
    global turn
    if index_turn != -1:
        for i in range(-1, index_turn, -1):
            History.pop(-1)
    index_turn = -1
    player_number = player_turn[(player_turn.index(player_number) + 1) % len(player_turn)]
    help_with_player()
    Table_ = copy.deepcopy(Table)
    player_turn_ = player_turn[:]
    player_cords_ = player_cords[:]
    player_trophy_ = player_trophy[:]
    PLAYERS_NAMES_ = PLAYERS_NAMES[:]
    copy_ = [Table_, player_cords_, player_trophy_, player_turn_, player_number, people_alive, PLAYERS_NAMES_]
    History.append(copy_)

    
def help_with_player():
    global player_number
    global turn
    turn.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#DAA520")
    turn.place(x=720, y=60)


def help_but_click(x, y):
    if [x, y] not in Clicked_Buttons:
        but = tk.Button(text=help_to_show(Table[x][y][0]), bd=5,width=10, height=4, font=('Arial', 12), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+k, stick='wens', padx=5, pady=5)
        Clicked_Buttons.append([x, y])
    else:
        if Table[x][y][2] == 'black':
            but = tk.Button(text=help_to_show(Table[x][y][0]), bd=5,width=10,height=4, font=('Arial', 12), bg=Table[x][y][2], fg='white', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text=help_to_show(Table[x][y][0]), bd=5,width=10,height=4, font=('Arial', 12), bg=Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+k, stick='wens', padx=5, pady=5)
        Clicked_Buttons.pop(Clicked_Buttons.index([x, y]))

    
def Show(Table):
    global Buttons
    global players
    for i in range(len(Buttons)):
        for j in range(len(Buttons[0])):
            Buttons[i][j].destroy()   
    Buttons = []
    for i in range(len(Table)):
        Buttons.append([])
        for j in range(len(Table[0])):
            if Table[i][j][2] == "black":
                but = tk.Button(text=help_to_show(Table[i][j][0]), bd=5, font=('Arial', 12), bg =Table[i][j][2], fg='white',width=10,height=4, command=lambda x=i, y=j:help_but_click(x, y))
            else:
                but = tk.Button(text=help_to_show(Table[i][j][0]), bd=5, font=('Arial', 12), bg =Table[i][j][2], fg='black',width=10,height=4, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+k, stick='wens', padx=5, pady=5)
            Buttons[-1].append(but)

          
def show_empty_table(Table):
    global Buttons
    global players
    for i in range(len(Buttons)):
        for j in range(len(Buttons[0])):            
            Buttons[i][j].destroy()   
    Buttons = []
    for i in range(len(Table)):
        Buttons.append([])
        for j in range(len(Table[0])):
            but = tk.Button(text="", bd=5, font=('Arial', 10), bg =Table[i][j][2], fg='black',width=9,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+k, stick='wens', padx=5, pady=5)
            Buttons[-1].append(but)


def help_with_kill_count():
    global Counts
    global player_trophy
    for elem in Counts:
        elem.destroy()
    for i in range(1, players + 1):
        text_ = tk.Label(text="Счёт игрока " + str(i) + " : " + str(player_trophy[i - 1]),font=('Arial, 15'),bg="#DAA520")
        Counts.append(text_)
        Counts[-1].place(x=1300,y=200 + 40 * (i - 1))

                       
def help_with_players_cords():
    global Table
    global player_cords
    global hint_label, hint_topic
    help_clear()
    for i in range(len(Table)):
        for j in range(len(Table[0])):
            if Table[i][j][1] != 0:
                player_cords[Table[i][j][1] - 1] = [i, j]

                
def help_clear():
    global hint_label, hint_topic
    hint_label.destroy()
    hint_topic.destroy()

    
def help_to_show(Buttons):
    s = ""
    for elem in Buttons:
        if elem != 0:
            s += str(elem)
            s += ""
    return s


# GLOBAL VARIABLES
Buttons = []
Clicked_Buttons = []
hint_label = tk.Label()
hint_topic= tk.Label()
index_turn = -1
killed_person = 1
num = 1
k = 8 + 1 * (size==5) + 2 * (size==4) + 3 * (size==3)
Counts = []
people_alive = size ** 2
player_cords = []
player_turn = [i for i in range(1, players + 1)]
player_trophy = [0 for i in range(players)]
player_number = 1
NAMES = ["Ксавье", "Ирма", "Кэтрин", "Куинтон", "Саймон", "Франклин", "Горацио", "Касим", "Педро", "Джулиан", "Дарнелл", "Ивонн", "Ульбрехт", "Бэррин", "Улис", "Женева",
          "Картрайт", "Таша", "Маркус", "Фиби", "Закари", "Грейс", "Ванда", "Дейдра", "Рамон", "Эвелин", "Изольда", "Сюзанна", "Райан", "Элисс", "Клайв", "Кристоф", 
          "Линнетт", "Натан", "Эштон", "Брэнсон", "Мэрион", "Вильгельм", "Эрнест", "Дружок", "Нейл", "Джек", "Офелия", "Флоренс", "Хьюберт", "Владимир", "Винсан", 
          "Тревор", "Лайнус", "Иван"]
PLAYERS_NAMES = []
Table = [[["", 0, "white"] for j in range(size)] for k in range(size)]
############################################################################
for i in range(size ** 2):
    j = random.randint(0, len(NAMES) - 1)
    Table[i // size][i % size][0] = NAMES[j]
    PLAYERS_NAMES.append(NAMES[j])
    NAMES.pop(j)
# POINT PLAYERS AND SIZE ON LiNES 23, 24
# NEXT FUNCTIONS FOR BEGINING GAME:
window.grid_columnconfigure(0, minsize=60)
window.grid_columnconfigure(1, minsize=60)
window.grid_columnconfigure(2, minsize=60)
window.grid_columnconfigure(3, minsize=60)
window.grid_columnconfigure(4, minsize=60)
window.grid_columnconfigure(5, minsize=60)
window.grid_columnconfigure(6, minsize=60)
window.grid_columnconfigure(7, minsize=60)
window.grid_columnconfigure(8, minsize=60)
window.grid_columnconfigure(9, minsize=60)
window.grid_columnconfigure(10, minsize=60)

window.grid_rowconfigure(1, minsize=70)
window.grid_rowconfigure(2, minsize=70)
window.grid_rowconfigure(3, minsize=70)
window.grid_rowconfigure(4, minsize=70)
window.grid_rowconfigure(5, minsize=70)
window.grid_rowconfigure(6, minsize=70)
window.grid_rowconfigure(7, minsize=70)
window.grid_rowconfigure(8, minsize=70)
window.grid_rowconfigure(9, minsize=70)
window.grid_rowconfigure(10, minsize=70)
Show(Table)


def help_for_begin():
    global num, Clicked_Buttons, player_cords, Table, hint_label, ok_button, name, name_label, begin_button
    begin_button.destroy()
    hint_label.destroy()
    i = random.randint(0, len(PLAYERS_NAMES) - 1)
    while PLAYERS_NAMES[i] == "":
        i = random.randint(0, len(PLAYERS_NAMES) - 1)
    player_cords.append([i // size, i % size])
    name = PLAYERS_NAMES[i]
    Table[i // size][i % size][1] = num
    PLAYERS_NAMES[i] = ""
    name_label = tk.Label(text="Игрок номер " + str(num) +", Вы играете\n за персонажа " + str(name) + "!\nХорошенько запомните его!",font=('Arial, 20'),bg="#DAA520")
    name_label.place(x=40,y=350)
    ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :function_OK())
    ok_button.place(x=120,y=510)
    Show(Table)
    Clicked_Buttons = []

    
hint_label = tk.Label(text="Игрок номер " + str(1) + ", нажмите на \nкнопку 'УЗНАТЬ ПЕРСОНАЖА',\n чтобы узнать своего персонажа,\n так, чтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'",font=('Arial, 20'),bg="#DAA520")
hint_label.place(x=20,y=350)
begin_button = tk.Button(text="Узнать персонажа", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :help_for_begin())
begin_button.place(x=130,y=530)
begin_topic = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg="#DAA520")
begin_topic.place(x=500, y=30)


def function_OK():
    global num, ok_button, hint_label, begin_button, name_label, Clicked_Buttons
    if num < players:
        ok_button.destroy()
        hint_label.destroy()
        name_label.destroy()
        num += 1
        hint_label = tk.Label(text="Игрок номер " + str(num) + ", нажмите на \nкнопку 'УЗНАТЬ ПЕРСОНАЖА',\n чтобы узнать своего персонажа,\n так, чтобы этого никто не видел,\n а затем нажмите кнопку 'ОК'",font=('Arial, 20'),bg="#DAA520")
        hint_label.place(x=20,y=350)
        begin_button = tk.Button(text="Узнать персонажа", bd=5, font=('Arial', 13),fg='red', bg='silver',width=20,height=2,command=lambda :help_for_begin())
        begin_button.place(x=130,y=530)
    else:
        begin_button.destroy()
        name_label.destroy()
        ok_button.destroy()
        begin()
    Clicked_Buttons = []
    Show(Table)


def help_but_function():
    global HELP_BUTTON, name, ok_button, killed_person
    if killed_person == 0:
        HELP_BUTTON.destroy()
        x, y = player_cords[player_number - 1][0], player_cords[player_number - 1][1]
        name = Table[x][y][0]
        hint_label = tk.Label(text="Игрок номер " + str(player_number) + ",\n Вы " + str(name) + "!",font=('Arial, 20'),bg="#DAA520")
        hint_label.place(x=1280,y=470 + 40 * (players - 4))
        HELP_BUTTON = tk.Button(text="Забыли персонажа?", bd=5, font=('Arial', 10),width=20,height=2,bg="green",command=lambda : help_but_function())
        ok_button = tk.Button(text="ОК", bd=5, font=('Arial', 13), bg='silver',width=10,height=2,command=lambda : (ok_button.destroy(), hint_label.destroy(), HELP_BUTTON.place(x=1290,y=400 + 40 * (players - 4) + 60)))
        ok_button.place(x=1330,y=550 + 40 * (players - 4))


def begin():
    global turn
    global killed_person
    global Clicked_Buttons
    global History
    global PLAYERS_NAMES
    global HELP_BUTTON
    Clicked_Buttons = []
    killed_person = 0
    begin_button.destroy()
    hint_label.destroy()
    begin_topic.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#DAA520")
    turn.place(x=720, y=60)
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#DAA520")
    turn.place(x=720, y=60)
    help_with_kill_count()
    K = tk.Button(text="Убить", bd=5, font=('Arial', 10),fg='red', bg='silver',width=20,height=2,command=lambda : kill())
    Q = tk.Button(text="Спросить", bd=5, font=('Arial', 10), fg='red', bg='silver',width=20,height=2, command=lambda : question())
    V = tk.Button(text="Вертикальная Чистка", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : vertical_clear())
    H = tk.Button(text="Горизонтальная Чистка", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : horizontal_clear())
    D = tk.Button(text="Вниз", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : down())
    U = tk.Button(text="Вверх", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : up())
    R = tk.Button(text="Вправо", bd=5, font=('Arial', 10),width=20, height=2, fg='red', bg='silver',command=lambda : right())
    L_ = tk.Button(text="Влево", bd=5, font=('Arial', 10), width=20,height=2,fg='red', bg='silver',command=lambda : left())
    C = tk.Button(text="Отменить", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : cancel_turn())
    F = tk.Button(text="Вперёд", bd=5, font=('Arial', 10),width=20,height=2, fg='red', bg='silver',command=lambda : forward_turn())
    end = tk.Button(text="Завершить Игру", bd=5, font=('Arial', 10),width=20,height=2, bg='red',command=lambda : window.destroy())
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
    #end.place(x=1290,y=400 + 40 * (players - 4))
    Table_ = copy.deepcopy(Table)
    player_turn_ = player_turn[:]
    player_cords_ = player_cords[:]
    player_trophy_ = player_trophy[:]
    PLAYERS_NAMES_ = PLAYERS_NAMES[:]
    copy_ = [Table_, player_cords_, player_trophy_, player_turn_, player_number, people_alive, PLAYERS_NAMES_]
    History = [copy_]
    Show(Table)


window.mainloop()