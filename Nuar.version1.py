import time
import copy
import tkinter as tk
window = tk.Tk()
window.attributes("-fullscreen", True)
window['bg'] = "#72F011"
window.title("MetaCodeNuar For Noobs")


# POINT PLAYERS AND SIZE ON LINES 11, 12
########################################
players = 4
size = 6
########################################
# NEXT FUNCTIONS FOR GAME PROCESS:


def help_but_click(x, y):
    if [x, y] not in Clicked_Buttons:
        if killed_person == 0:
            but = tk.Button(text=help_to_show(Matrix[x][y][0]), bd=5,width=7, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=7, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        Clicked_Buttons.append([x, y])
    else:
        if killed_person == 0:
            but = tk.Button(text=help_to_show(Matrix[x][y][0]), bd=5,width=7,height=3, font=('Arial', 13), bg=Matrix[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=7,height=3, font=('Arial', 13), bg=Matrix[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        Buttons[x][y].destroy()
        Buttons[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        Clicked_Buttons.pop(Clicked_Buttons.index([x, y]))

        
def horizontal_clear():
    global Matrix
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="В каждой из " + str(len(Matrix)) + " строк выберите по одной\n чёрной ячейке для горизонтальной очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Matrix):
            hint_label.place(x=60,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            a = set()
            for j in range(len(Matrix)):
                if Matrix[Clicked_Buttons[-j-1][0]][Clicked_Buttons[-j-1][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j-1][0])
            if len(a) != len(Matrix):
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
            else:        
                for i in range(1, len(Matrix) + 1):
                    (Matrix[Clicked_Buttons[-i][0]]).pop(Clicked_Buttons[-i][1])
                help_for_player_turn()
                help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def vertical_clear():
    global Matrix
    global Clicked_Buttons
    global killed_person
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="В каждом из " + str(len(Matrix[0])) + " столбцов выберите по одной \nчёрной ячейке для вертикальной очистки очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != len(Matrix[0]):
            hint_label.place(x=50,y = 590)
            hint_topic.place(x=150,y = 510)
        else:
            a = set()
            for j in range(1, len(Matrix[0]) + 1):
                if Matrix[Clicked_Buttons[-j][0]][Clicked_Buttons[-j][1]][2] == 'black':
                    a.add(Clicked_Buttons[-j][1])
            if len(a) != len(Matrix[0]):
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
            else:
                P_1 = [[Matrix[i][j] for i in range(len(Matrix))] for j in range(len(Matrix[0]))]
                for i in range(1, len(Matrix[0]) + 1):
                    (P_1[Clicked_Buttons[-i][1]]).pop(Clicked_Buttons[-i][0])
                Matrix = [[P_1[i][j] for i in range(len(P_1))] for j in range(len(P_1[0]))]
                help_for_player_turn()
                help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def down():
    global Matrix
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
            for i in range(-1, -len(Matrix), -1):
                Matrix[i][n], Matrix[i - 1][n] = Matrix[i - 1][n], Matrix[i][n]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def up():
    global Matrix
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
            for i in range(len(Matrix) - 1):
                Matrix[i][n], Matrix[i + 1][n] = Matrix[i + 1][n], Matrix[i][n]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def left():
    global Matrix
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
            for j in range(len(Matrix[0]) - 1):
                Matrix[n][j], Matrix[n][j + 1] = Matrix[n][j + 1], Matrix[n][j]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def right():
    global Matrix
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
            for j in range(-1, -len(Matrix[0]), - 1):
                Matrix[n][j], Matrix[n][j - 1] = Matrix[n][j - 1], Matrix[n][j]
            help_for_player_turn()
            help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def kill():
    global Matrix, Clicked_Buttons, player_number, killed_person, cords, score, dead_label, dead_button, dead_topic
    global hint_topic, hint_label
    help_clear()
    hint_topic= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint_label = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed_person == 0:
        if len(Clicked_Buttons) != 1:
            hint_label.place(x=60,y = 590)
            hint_topic.place(x=150,y = 510)
            Show(Matrix)
        elif Matrix[Clicked_Buttons[-1][0]][Clicked_Buttons[-1][1]][2] == 'black':
            hint_label.place(x=75,y = 590)
            hint_topic.place(x=150,y = 510)
            Show(Matrix)
        else:
            i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
            if abs(cords[player_number - 1][0] - i) > 1 or abs(cords[player_number - 1][1] - j) > 1 or abs(cords[player_number - 1][0] - i) + abs(cords[player_number - 1][1] - j) == 0:
                hint_label.place(x=60,y = 590)
                hint_topic.place(x=150,y = 510)
                Show(Matrix)
            else:
                killed_person = Matrix[i][j][1]
                Matrix[i][j][2] = 'black'
                Matrix[i][j][0] = []
                Matrix[i][j][1] = 0
                score = Matrix[i][j][3]
                Matrix[i][j][3] = 0
                for a in range(len(Matrix)):
                    for b in range(len(Matrix[0])):
                        if abs(a - i) > 1 or abs(b - j) > 1:
                            if Matrix[a][b][2] != 'black':
                                Matrix[a][b][0][player_number - 1] = 0
                if killed_person != 0:
                    for x in range(len(Matrix)):
                        for y in range(len(Matrix[0])):
                            if Matrix[x][y][2] != 'black':
                                Matrix[x][y][0][killed_person - 1] = killed_person
                    Show_emty_pole(Matrix)
                    for a in range(len(Matrix)):
                        for b in range(len(Matrix[0])):
                            if Matrix[a][b][1] == player_number:
                                Matrix[a][b][3] += 1
                    Matrix[i][j][3], Matrix[i][j][1] = score, killed_person
                    help_with_kill_count()
                    Matrix[i][j][3], Matrix[i][j][1] = 0, 0
                    dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#72F011",fg='black')
                    dead_topic.place(x=80,y=530)
                    dead_label = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed_person) + ". \nИгрок номер " + str(killed_person) + ", укажите свое место возрождения так,\n чтобы это никто не видел, и нажмите кнопку 'ОК'.",font=('Arial, 15'),bg="#72F011",fg='black')
                    dead_label.place(x=40,y = 610)
                    dead_button= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                    dead_button.place(x=220,y=720)
                else:
                    Q_and_K()
                    help_for_player_turn()
                    help_with_players_cords()
                    Show(Matrix)
        Clicked_Buttons = []

        
def help_with_spawn():
    global cords
    global Clicked_Buttons
    global Matrix
    global killed_person
    global score
    global dead_button, dead_label, dead_topic
    if len(Clicked_Buttons) == 1:
        i, j = Clicked_Buttons[0][0], Clicked_Buttons[0][1]
        if Matrix[i][j][2] != 'black' and [i, j] not in cords:
            Matrix[i][j][1] = killed_person
            Matrix[i][j][3] = score
            Q_and_K()
            help_with_kill_count()
            help_with_players_cords()
            help_for_player_turn()
            killed_person = 0
            dead_button.destroy()
            dead_label.destroy()
            dead_topic.destroy()
    Clicked_Buttons = []
    Show_emty_pole(Matrix)
        

def question():
    global Matrix
    global Clicked_Buttons
    global cords
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
            if abs(cords[player_number - 1][0] - i) > 1 or abs(cords[player_number - 1][1] - j) > 1 or Matrix[i][j][2] == 'black':
                hint_label.place(x=40,y = 590)
                hint_topic.place(x=150,y = 510)
            else:
                s = []
                for k in range(len(Matrix)):
                    for y in range(len(Matrix[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and Matrix[k][y][1] != 0:
                            s.append(Matrix[k][y][1])
                for a in range(len(Matrix)):
                    for b in range(len(Matrix[0])):
                        if Matrix[a][b][2] != 'black':
                            for x in range(1, players + 1):
                                if (abs(a - i) > 1 or abs(b - j) > 1) and x in s:
                                    Matrix[a][b][0][x - 1] = 0
                                elif (abs(a - i) <= 1 and abs(b - j) <= 1) and x not in s:
                                    Matrix[a][b][0][x - 1] = 0
                Q_and_K()
                help_for_player_turn()
                help_with_players_cords()
        Clicked_Buttons = []
        Show(Matrix)

        
def Q_and_K():
    global Matrix
    global players
    for a in range(players):
        for player in range(1, players + 1):
            count = 0
            I, J = -1, -1
            for i in range(len(Matrix)):
                for j in range(len(Matrix[0])):
                    if player in Matrix[i][j][0]:
                        I, J = i, j
                        count += 1
            if count == 1 and I != -1:
                for k in range(len(Matrix[I][J][0])):
                    if k != player - 1:
                        Matrix[I][J][0][k] = 0

                        
def cancel_turn():
    global History
    global Matrix
    global index_turn
    global killed_person
    global hint_topic, hint_label
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
            Matrix = copy.deepcopy(P_1)
            help_with_player()
            help_with_players_cords()
            help_with_kill_count()
        Show(Matrix)

        
def forward_turn():
    global History
    global Matrix
    global index_turn
    global killed_person
    global hint_topic, hint_label
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
            Matrix = copy.deepcopy(P_1)
            help_with_player()
            help_with_players_cords()
            help_with_kill_count()
        Show(Matrix)

        
def help_for_player_turn():
    global History
    global Matrix
    global index_turn
    global player_number
    global turn
    if index_turn != -1:
        for i in range(-1, index_turn, -1):
            History.pop(-1)
    index_turn = -1
    player_number = player_number % players + 1
    turn.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    turn.place(x=720, y=60)
    X = copy.deepcopy(Matrix)
    History.append(X)

    
def help_with_player():
    global index_turn
    global player_number
    global turn
    global History
    player_number = (len(History) + index_turn) % players + 1
    turn.destroy()
    turn = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    turn.place(x=720, y=60)

    
def Show(Matrix):
    global Buttons
    global players
    for i in range(len(Buttons)):
        for j in range(len(Buttons[0])):            
            Buttons[i][j].destroy()   
    Buttons = []
    for i in range(len(Matrix)):
        Buttons.append([])
        for j in range(len(Matrix[0])):
            but = tk.Button(text=help_to_show(Matrix[i][j][0]), bd=5, font=('Arial', 13), bg =Matrix[i][j][2], fg='black',width=7,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
            Buttons[-1].append(but)

            
def Show_emty_pole(Matrix):
    global Buttons
    global players
    for i in range(len(Buttons)):
        for j in range(len(Buttons[0])):            
            Buttons[i][j].destroy()   
    Buttons = []
    for i in range(len(Matrix)):
        Buttons.append([])
        for j in range(len(Matrix[0])):
            but = tk.Button(text="", bd=5, font=('Arial', 13), bg =Matrix[i][j][2], fg='black',width=7,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
            Buttons[-1].append(but)


def help_with_kill_count():
    global Counts
    for elem in Counts:
        elem.destroy()
    for i in range(1, players + 1):
        for a in range(len(Matrix)):
            for b in range(len(Matrix[0])):
                if Matrix[a][b][1] == i:
                    text_ = tk.Label(text="Счёт игрока " + str(i) + " : " + str(Matrix[a][b][3]),font=('Arial, 15'),bg="#72F011")
                    Counts.append(text_)
                    Counts[-1].place(x=1300,y=200 + 40 * (i - 1))

                       
def help_with_players_cords():
    global Matrix
    global cords
    global hint_label, hint_topic
    help_clear()
    for i in range(len(Matrix)):
        for j in range(len(Matrix[0])):
            if Matrix[i][j][1] != 0:
                cords[Matrix[i][j][1] - 1] = [i, j]

                
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
cords = []
Matrix = [[[[i for i in range(1, players + 1)], 0, "white", 0] for j in range(size)] for k in range(size)]
hint_label = tk.Label()
hint_topic= tk.Label()
index_turn = -1
player_number = 1
killed_person = 1
num = 1
Counts = []
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
Show_emty_pole(Matrix)


def help_for_begin():
    global num, Clicked_Buttons, cords, Matrix, hint_label
    if num <= players:
        if len(Clicked_Buttons) == 1 and Clicked_Buttons[0] not in cords:
            hint_label.destroy()
            cords.append(Clicked_Buttons[0])
            Matrix[Clicked_Buttons[0][0]][Clicked_Buttons[0][1]][1] = num
            num += 1
            if num <= players:
                hint_label = tk.Label(text="Игрок номер " + str(num) + ", укажите своего \nперсонажа так, чтобы этого никто не \nвидел, и нажмте кнопку 'Продолжить'",font=('Arial, 20'),bg="#72F011")
                hint_label.place(x=70,y=350)
            else:
                hint_label = tk.Label(text="Да начнется игра!",font=('Arial, 40'),bg="#72F011")
                hint_label.place(x=70,y=350)
        Show_emty_pole(Matrix)
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
    global Matrix
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
    P_ = copy.deepcopy(Matrix)
    History = [P_]
    Show(Matrix)

    
window.mainloop()