import time
import copy
import tkinter as tk
window = tk.Tk()
#window.attributes("-fullscreen", True)
window.geometry("1650x900")
window['bg'] = "#72F011"
window.title("Один против всех")
width = 1536
height = 864
width_ = window.winfo_screenwidth()
height_ = window.winfo_screenheight()


# POINT PLAYERS AND SIZE ON LINES 11, 12
########################################
players = 4
size = 6
########################################
# NEXT FUNCTIONS FOR GAME PROCESS:


def help_but_click(x, y):
    if [x, y] not in Clicked_Buttons:
        if killed_person == 0:
            but = tk.Button(text=help_to_show(Table[x][y][0]), bd=5,width=7+players-4, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=7+players-4, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        Clicked_Buttons.append([x, y])
    else:
        if killed_person == 0:
            but = tk.Button(text=help_to_show(Table[x][y][0]), bd=5,width=7+players-4,height=3, font=('Arial', 13), bg=Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=7+players-4,height=3, font=('Arial', 13), bg=Table[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        Clicked_Buttons.pop(Clicked_Buttons.index([x, y]))

        
def horizontal_clear():
    global Table
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="В каждой из " + str(len(Table)) + " строк выберите по одной\n чёрной ячейке для горизонтальной очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Table):
            hint_label.place(x=60,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            a = set()
            for j in range(len(Table)):
                if Table[Clicked_Buttons[-j-1][0]][Clicked_Buttons[-j-1][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j-1][0])
            if len(a) != len(Table):
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
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
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="В каждом из " + str(len(Table[0])) + " столбцов выберите по одной \nчёрной ячейке для вертикальной очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Table[0]):
            hint_label.place(x=50,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            a = set()
            for j in range(1, len(Table[0]) + 1):
                if Table[Clicked_Buttons[-j][0]][Clicked_Buttons[-j][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j][1])
            if len(a) != len(Table[0]):
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
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
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкоторый надо сдвинуть вниз...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=100,y = 590)
            hint_topic.place(x=150,y = 510)
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
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите любую ячейку столбца, \nкотороый надо сдвинуть вверх...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=100,y = 590)
            hint_topic.place(x=150,y = 510)
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
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть влево...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=100,y = 590)
            hint_topic.place(x=150,y = 510)
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
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть вправо...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=100,y = 590)
            hint_topic.place(x=150,y = 510)
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
    global hint_topic, hint_label, people_alive, player_trophy
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=60,y = 590)
            hint_topic.place(x=150,y = 510)
            Show(Table)
        elif Table[Clicked_Buttons[-1][0]][Clicked_Buttons[-1][1]][2] == 'black':
            hint_label.place(x=75,y = 590)
            hint_topic.place(x=150,y = 510)
            Show(Table)
        else:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if abs(player_cords[player_number - 1][0] - i) > 1 or abs(player_cords[player_number - 1][1] - j) > 1 or abs(player_cords[player_number - 1][0] - i) + abs(player_cords[player_number - 1][1] - j) == 0:
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
                Show(Table)
            else:
                people_alive -= 1
                killed_person = Table[i][j][1]
                Table[i][j][2] = 'black'
                Table[i][j][0] = []
                Table[i][j][1] = 0
                for a in range(len(Table)):
                    for b in range(len(Table[0])):
                        if abs(a - i) > 1 or abs(b - j) > 1:
                            if Table[a][b][2] != 'black':
                                Table[a][b][0][player_number - 1] = 0
                if killed_person != 0:
                    if people_alive >= players:
                        for x in range(len(Table)):
                            for y in range(len(Table[0])):
                                if Table[x][y][2] != 'black':
                                    Table[x][y][0][killed_person - 1] = killed_person
                        show_empty_table(Table)
                        player_trophy[player_number - 1] += 1
                        help_with_kill_count()
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#72F011",fg='black')
                        dead_topic.place(x=80,y=530)
                        dead_label = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed_person) + ". \nИгрок номер " + str(killed_person) + ", укажите свое место возрождения так,\n чтобы это никто не видел, и нажмите кнопку 'ОК'.",font=('Arial, 15'),bg="#72F011",fg='black')
                        dead_label.place(x=40,y = 610)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                        dead_button.place(x=220,y=720)
                    else:
                        for x in range(len(Table)):
                            for y in range(len(Table[0])):
                                if Table[x][y][2] != 'black':
                                    Table[x][y][0][killed_person - 1] = 0
                        show_empty_table(Table)
                        player_trophy[player_number - 1] += 1
                        help_with_kill_count()
                        player_cords[killed_person - 1] = [-10, -10]
                        player_turn.pop(player_turn.index(killed_person))
                        dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#72F011",fg='black')
                        dead_topic.place(x=80,y=530)
                        dead_label = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed_person) + ". \nИгрок номер " + str(killed_person) + ", Вы не можете больше возродиться, так как \nсвободных живых клеток не осталось. Нажмите кнопку 'ОК'.",font=('Arial, 15'),bg="#72F011",fg='black')
                        dead_label.place(x=10,y = 610)
                        dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                        dead_button.place(x=220,y=720)
                else:
                    Q_and_K()
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
    global dead_button, dead_label, dead_topic
    if people_alive < players:
        dead_button.destroy()
        dead_label.destroy()
        dead_topic.destroy()
        Q_and_K()
        help_for_player_turn()
        killed_person = 0
    else:
        if len(Clicked_Buttons) == 1:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if Table[i][j][2] != 'black' and [i, j] not in player_cords:
                Table[i][j][1] = killed_person
                Q_and_K()
                help_for_player_turn()
                help_with_players_cords()
                killed_person = 0
                dead_button.destroy()
                dead_label.destroy()
                dead_topic.destroy()
    Clicked_Buttons = []
    show_empty_table(Table)
        

def question():
    global Table
    global Clicked_Buttons
    global player_cords
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите ячейку персонажа, находящуюся рядом\n с Вашим пресонажем, чтобы опросить его...", 
    font=('Arial, 16'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=40,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if abs(player_cords[player_number - 1][0] - i) > 1 or abs(player_cords[player_number - 1][1] - j) > 1 or Table[i][j][2] == 'black':
                hint_label.place(x=40,y = 590)
                hint_topic.place(x=150,y = 510)
            else:
                s = []
                for k in range(len(Table)):
                    for y in range(len(Table[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and Table[k][y][1] != 0:
                            s.append(Table[k][y][1])
                for a in range(len(Table)):
                    for b in range(len(Table[0])):
                        if Table[a][b][2] != 'black':
                            for x in range(1, players + 1):
                                if (abs(a - i) > 1 or abs(b - j) > 1) and x in s:
                                    Table[a][b][0][x - 1] = 0
                                elif (abs(a - i) <= 1 and abs(b - j) <= 1) and x not in s:
                                    Table[a][b][0][x - 1] = 0
                Q_and_K()
                help_for_player_turn()
        Clicked_Buttons = []
        Show(Table)

        
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
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Вы вернулись в начало игры!", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if index_turn == -len(History) or len(History) == 1:
            hint_label.place(x=120,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            index_turn -= 1
            P_1 = copy.deepcopy(History[index_turn])
            Table = copy.deepcopy(P_1[0])
            player_cords = P_1[1][:]
            player_trophy = P_1[2][:]
            player_turn = P_1[3][:]
            player_number = P_1[4]
            people_alive = P_1[5]
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
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Вы вернулись в конец игры!", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if index_turn == -1:
            hint_label.place(x=120,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            index_turn += 1
            P_1 = copy.deepcopy(History[index_turn])
            Table = copy.deepcopy(P_1[0])
            player_cords = P_1[1][:]
            player_trophy = P_1[2][:]
            player_turn = P_1[3][:]
            player_number = P_1[4]
            people_alive = P_1[5]
            help_with_player()
            help_with_players_cords()
            help_with_kill_count()
        Show(Table)

        
def help_for_player_turn():
    global History
    global Table, player_cords, player_trophy, player_turn, player_number, people_alive
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
    copy_ = [Table_, player_cords_, player_trophy_, player_turn_, player_number, people_alive]
    History.append(copy_)

    
def help_with_player():
    global player_number
    global turn
    turn.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    turn.place(x=720, y=60)

    
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
            but = tk.Button(text=help_to_show(Table[i][j][0]), bd=5, font=('Arial', 13), bg =Table[i][j][2], fg='black',width=7+players-4,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
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
            but = tk.Button(text="", bd=5, font=('Arial', 13), bg =Table[i][j][2], fg='black',width=7+players-4,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
            Buttons[-1].append(but)


def help_with_kill_count():
    global Counts
    global player_trophy
    for elem in Counts:
        elem.destroy()
    for i in range(1, players + 1):
        text_ = tk.Label(text="Счёт игрока " + str(i) + " : " + str(player_trophy[i - 1]),font=('Arial, 15'),bg="#72F011")
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
            s += " "
    return s[:-1]


# GLOBAL VARIABLES
Buttons = []
Clicked_Buttons = []
Table = [[[[i for i in range(1, players + 1)], 0, "white"] for j in range(size)] for k in range(size)]
hint_label = tk.Label()
hint_topic= tk.Label()
index_turn = -1
killed_person = 1
num = 1
Counts = []
people_alive = size ** 2
player_cords = []
player_turn = [i for i in range(1, players + 1)]
player_trophy = [0 for i in range(players)]
player_number = 1
# POINT PLAYERS AND SIZE ON LiNES 11, 12
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
show_empty_table(Table)


def help_for_begin():
    global num, Clicked_Buttons, player_cords, Table, hint_label
    if num <= players:
        if len(Clicked_Buttons) == 1 and Clicked_Buttons[0] not in player_cords:
            hint_label.destroy()
            player_cords.append(Clicked_Buttons[0])
            Table[Clicked_Buttons[0][0]][Clicked_Buttons[0][1]][1] = num
            num += 1
            if num <= players:
                hint_label = tk.Label(text="Игрок номер " + str(num) + ", укажите своего \nперсонажа так, чтобы этого никто не \nвидел, и нажмте кнопку 'Продолжить'",font=('Arial, 20'),bg="#72F011")
                hint_label.place(x=70,y=350)
            else:
                hint_label = tk.Label(text="Да начнется игра!",font=('Arial, 40'),bg="#72F011")
                hint_label.place(x=70,y=350)
        show_empty_table(Table)
    else:
        begin()
    Clicked_Buttons = []

    
hint_label = tk.Label(text="Игрок номер " + str(num) + ", укажите своего \nперсонажа так, чтобы этого никто не \nвидел, и нажмте кнопку 'Продолжить'",font=('Arial, 20'),bg="#72F011")
hint_label.place(x=70,y=350)
begin_button = tk.Button(text="Продолжить", bd=5, font=('Arial', 13),fg='red',width=20,height=2,command=lambda :help_for_begin())
begin_button.place(x=200,y=500)
begin_topic = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg="#72F011")
begin_topic.place(x=500, y=30)


def begin():
    global turn
    global killed_person
    global Clicked_Buttons
    global Table
    global History
    Clicked_Buttons = []
    killed_person = 0
    begin_button.destroy()
    hint_label.destroy()
    begin_topic.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    turn.place(x=720, y=60)
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    turn.place(x=720, y=60)
    help_with_kill_count()
    K = tk.Button(text="Убить", bd=5, font=('Arial', 13),fg='red',width=20,height=2,command=lambda : kill())
    Q = tk.Button(text="Спросить", bd=5, font=('Arial', 13), fg='red',width=20,height=2, command=lambda : question())
    V = tk.Button(text="Вертикальная Чистка", bd=5, font=('Arial', 13),width=20, height=2, fg='red',command=lambda : vertical_clear())
    H = tk.Button(text="Горизонтальная Чистка", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : horizontal_clear())
    D = tk.Button(text="Вниз", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : down())
    U = tk.Button(text="Вверх", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : up())
    R = tk.Button(text="Вправо", bd=5, font=('Arial', 13),width=20, height=2, fg='red',command=lambda : right())
    L_ = tk.Button(text="Влево", bd=5, font=('Arial', 13), width=20,height=2,fg='red',command=lambda : left())
    C = tk.Button(text="Отменить", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : cancel_turn())
    F = tk.Button(text="Вперёд", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : forward_turn())
    end = tk.Button(text="Завершить Игру", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : window.destroy())
    command_topic = tk.Label(text="Команды:",font=('Arial, 40'),bg="#72F011")
    command_topic.place(x=150,y=60)
    count_hint = tk.Label(text="Счёт:",font=('Arial, 40'),bg="#72F011")
    count_hint.place(x=1300,y=100)
    K.place(x=65, y=145)
    Q.place(x=270,y=145)
    V.place(x=270,y=355)
    H.place(x=65, y=355)
    D.place(x=65,y=285)
    U.place(x=270,y=285)
    R.place(x=270, y=215)
    L_.place(x=65,y=215)
    C.place(x=65, y=425)
    F.place(x=270,y=425)
    end.place(x=1275,y=400 + 40 * (players - 4))
    Table_ = copy.deepcopy(Table)
    player_turn_ = player_turn[:]
    player_cords_ = player_cords[:]
    player_trophy_ = player_trophy[:]
    copy_ = [Table_, player_cords_, player_trophy_, player_turn_, player_number, people_alive]
    History = [copy_]
    Show(Table)

    
window.mainloop()