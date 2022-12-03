import time
import copy
import tkinter as tk
win = tk.Tk()
win.geometry(f"2100x2100")
win['bg'] = "#72F011"
win.title("MetaCodeNuar For Noobs")

# POINT PLAYERS AND SIZE ON LiNES 11, 12
########################################
players = 2
size = 5
########################################
# NEXT FUNCTIONS FOR GAME PROCESS:

def help_but_click(x, y):
    global S
    global killed
    if [x, y] not in S:
        if killed == 0:
            but = tk.Button(text=help_to_show(P[x][y][0]), bd=5,width=6, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=6, height=3, font=('Arial', 13), bg='gray', fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        L[x][y].destroy()
        L[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        S.append([x, y])
    else:
        if killed == 0:
            but = tk.Button(text=help_to_show(P[x][y][0]), bd=5,width=6,height=3, font=('Arial', 13), bg=P[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        else:
            but = tk.Button(text="", bd=5,width=6,height=3, font=('Arial', 13), bg=P[x][y][2], fg='black', command=lambda i=x, j=y:help_but_click(i, j))
        L[x][y].destroy()
        L[x][y] = but
        but.grid(row=x + 3, column=y+10, stick='wens', padx=5, pady=5)
        S.pop(S.index([x, y]))

def horizontal_clear():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="В каждой из " + str(len(P)) + " строк выберите по одной\n черной ячейке для горизонтальной очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != len(P):
            hint.place(x=60,y = 520)
            hint_.place(x=150,y = 440)
        else:
            a = set()
            for j in range(len(P)):
                if P[S[-j-1][0]][S[-j-1][1]][2] == 'black':
                    a.add(S[-j-1][0])
            if len(a) != len(P):
                hint.place(x=60,y = 520)
                hint_.place(x=150,y = 440)
            else:        
                for i in range(1, len(P) + 1):
                    (P[S[-i][0]]).pop(S[-i][1])
                help_for_functions()
                help_for_all_functions()
        S = []
        Show(P)

def vertical_clear():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="В каждом из " + str(len(P[0])) + " столбцов выберите по одной \nчерной ячейке для вертикальной очистки очистки...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != len(P[0]):
            hint.place(x=50,y = 520)
            hint_.place(x=150,y = 440)
        else:
            a = set()
            for j in range(1, len(P[0]) + 1):
                if P[S[-j][0]][S[-j][1]][2] == 'black':
                    a.add(S[-j][1])
            if len(a) != len(P[0]):
                hint.place(x=60,y = 520)
                hint_.place(x=150,y = 440)
            else:
                P_1 = [[P[i][j] for i in range(len(P))] for j in range(len(P[0]))]
                for i in range(1, len(P[0]) + 1):
                    (P_1[S[-i][1]]).pop(S[-i][0])
                P = [[P_1[i][j] for i in range(len(P_1))] for j in range(len(P_1[0]))]
                help_for_functions()
                help_for_all_functions()
        S = []
        Show(P)

def down():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите любую ячейку столбца, \nкоторый надо сдвинуть вниз...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=100,y = 520)
            hint_.place(x=150,y = 440)
        else:
            n = S[-1][1]
            for i in range(-1, -len(P), -1):
                P[i][n], P[i - 1][n] = P[i - 1][n], P[i][n]
            help_for_functions()
            help_for_all_functions()
        S = []
        Show(P)

def up():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите любую ячейку столбца, \nкотороый надо сдвинуть вверх...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=100,y = 520)
            hint_.place(x=150,y = 440)
        else:
            n = S[-1][1]
            for i in range(len(P) - 1):
                P[i][n], P[i + 1][n] = P[i + 1][n], P[i][n]
            help_for_functions()
            help_for_all_functions()
        S = []
        Show(P)

def left():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть влево...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=100,y = 520)
            hint_.place(x=150,y = 440)
        else:
            n = S[-1][0]
            for j in range(len(P[0]) - 1):
                P[n][j], P[n][j + 1] = P[n][j + 1], P[n][j]
            help_for_functions()
            help_for_all_functions()
        S = []
        Show(P)

def right():
    global P
    global S
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите любую ячейку строки, \nкоторую надо сдвинуть вправо...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=100,y = 520)
            hint_.place(x=150,y = 440)
        else:
            n = S[-1][0]
            for j in range(-1, -len(P[0]), - 1):
                P[n][j], P[n][j - 1] = P[n][j - 1], P[n][j]
            help_for_functions()
            help_for_all_functions()
        S = []
        Show(P)

def kill():
    global P, S, player_number, killed, cords, score, dead, dead_, dead_topic
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите живого персонажа, находящегося\n рядом с Вами, которого Вы хотите убить...", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=60,y = 520)
            hint_.place(x=150,y = 440)
            Show(P)
        elif P[S[-1][0]][S[-1][1]][2] == 'black':
            hint.place(x=75,y = 520)
            hint_.place(x=150,y = 440)
            Show(P)
        else:
            i, j = S[0][0], S[0][1]
            if abs(cords[player_number - 1][0] - i) > 1 or abs(cords[player_number - 1][1] - j) > 1 or abs(cords[player_number - 1][0] - i) + abs(cords[player_number - 1][1] - j) == 0:
                hint.place(x=60,y = 520)
                hint_.place(x=150,y = 440)
                Show(P)
            else:
                killed = P[i][j][1]
                P[i][j][2] = 'black'
                P[i][j][0] = []
                P[i][j][1] = 0
                score = P[i][j][3]
                P[i][j][3] = 0
                for a in range(len(P)):
                    for b in range(len(P[0])):
                        if abs(a - i) > 1 or abs(b - j) > 1:
                            if P[a][b][2] != 'black':
                                P[a][b][0][player_number - 1] = 0
                if killed != 0:
                    for x in range(len(P)):
                        for y in range(len(P[0])):
                            if P[x][y][2] != 'black':
                                P[x][y][0][killed - 1] = killed
                    show(P)
                    for a in range(len(P)):
                        for b in range(len(P[0])):
                            if P[a][b][1] == player_number:
                                P[a][b][3] += 1
                    P[i][j][3], P[i][j][1] = score, killed
                    help_with_kill_count()
                    P[i][j][3], P[i][j][1] = 0, 0
                    dead_topic = tk.Label(text="Произошло Убийство!",font=('Arial, 30'),bg="#72F011",fg='black')
                    dead_topic.place(x=80,y=460)
                    dead = tk.Label(text="Игрок номер " + str(player_number) + " убил игрока номер " + str(killed) + ". \nИгрок номер " + str(killed) + ", укажите свое место возрождения так,\n чтобы это никто не видел, и нажмите кнопку 'ОК'.",font=('Arial, 15'),bg="#72F011",fg='black')
                    dead.place(x=40,y = 540)
                    dead_= tk.Button(text="ОК", width=7,height=2,font=('Arial, 15'),command=lambda: help_with_spawn())
                    dead_.place(x=220,y=650)
                else:
                    Q_and_K()
                    help_for_functions()
                    help_for_all_functions()
                    Show(P)
        S = []

def help_with_spawn():
    global cords
    global S
    global P
    global killed
    global score
    global dead_, dead, dead_topic
    if len(S) == 1:
        i, j = S[0][0], S[0][1]
        if P[i][j][2] != 'black' and [i, j] not in cords:
            P[i][j][1] = killed
            P[i][j][3] = score
            Q_and_K()
            help_with_kill_count()
            help_for_all_functions()
            help_for_functions()
            killed = 0
            dead_.destroy()
            dead.destroy()
            dead_topic.destroy()
    S = []
    show(P)
        

def question():
    global P
    global S
    global cords
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Укажите ячейку персонажа, находящуюся рядом\n с Вашим пресонажем, чтобы опросить его...", 
    font=('Arial, 16'),bg="#72F011",fg='black')
    if killed == 0:
        if len(S) != 1:
            hint.place(x=40,y = 520)
            hint_.place(x=150,y = 440)
        else:
            i, j = S[0][0], S[0][1]
            if abs(cords[player_number - 1][0] - i) > 1 or abs(cords[player_number - 1][1] - j) > 1 or P[i][j][2] == 'black':
                hint.place(x=40,y = 520)
                hint_.place(x=150,y = 440)
            else:
                s = []
                for k in range(len(P)):
                    for y in range(len(P[0])):
                        if abs(i - k) < 2 and abs(j - y) < 2 and P[k][y][1] != 0:
                            s.append(P[k][y][1])
                for a in range(len(P)):
                    for b in range(len(P[0])):
                        if P[a][b][2] != 'black':
                            for x in range(1, players + 1):
                                if (abs(a - i) > 1 or abs(b - j) > 1) and x in s:
                                    P[a][b][0][x - 1] = 0
                                elif (abs(a - i) <= 1 and abs(b - j) <= 1) and x not in s:
                                    P[a][b][0][x - 1] = 0
                Q_and_K()
                help_for_functions()
                help_for_all_functions()
        S = []
        Show(P)

def Q_and_K():
    global P
    global players
    for a in range(players):
        for player in range(1, players + 1):
            count = 0
            I, J = -1, -1
            for i in range(len(P)):
                for j in range(len(P[0])):
                    if player in P[i][j][0]:
                        I, J = i, j
                        count += 1
            if count == 1 and I != -1:
                for k in range(len(P[I][J][0])):
                    if k != player - 1:
                        P[I][J][0][k] = 0

def cancel():
    global All_P
    global P
    global index
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Вы вернулись в начало игры!", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if index == -len(ALL_P) or len(ALL_P) == 1:
            hint.place(x=120,y = 520)
            hint_.place(x=150,y = 440)
        else:
            index -= 1
            P_1 = copy.deepcopy(ALL_P[index])
            P = copy.deepcopy(P_1)
            help_with_player()
            help_for_all_functions()
            help_with_kill_count()
        Show(P)

def forward():
    global All_P
    global P
    global index
    global killed
    global hint_, hint
    help_clear()
    hint_= tk.Label(text="Подсказка:",font=('Arial, 30'),bg="#72F011")
    hint = tk.Label(text="Вы вернулись в конец игры!", 
    font=('Arial, 15'),bg="#72F011",fg='black')
    if killed == 0:
        if index == -1:
            hint.place(x=120,y = 520)
            hint_.place(x=150,y = 440)
        else:
            index += 1
            P_1 = copy.deepcopy(ALL_P[index])
            P = copy.deepcopy(P_1)
            help_with_player()
            help_for_all_functions()
            help_with_kill_count()
        Show(P)

def help_for_functions():
    global ALL_P
    global P
    global index
    global player_number
    global aboba
    if index != -1:
        for i in range(-1, index, -1):
            ALL_P.pop(-1)
    index = -1
    player_number = player_number % players + 1
    aboba.destroy()
    aboba = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    aboba.place(x=720, y=60)
    X = copy.deepcopy(P)
    ALL_P.append(X)

def help_with_player():
    global index
    global player_number
    global aboba
    global P
    global ALL_P
    player_number = (len(ALL_P) + index) % players + 1
    aboba.destroy()
    aboba = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    aboba.place(x=720, y=60)

def Show(P):
    global L
    global players
    for i in range(len(L)):
        for j in range(len(L[0])):            
            L[i][j].destroy()   
    L = []
    for i in range(len(P)):
        L.append([])
        for j in range(len(P[0])):
            but = tk.Button(text=help_to_show(P[i][j][0]), bd=5, font=('Arial', 13), bg =P[i][j][2], fg='black',width=6,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
            L[-1].append(but)

def show(P):
    global L
    global players
    for i in range(len(L)):
        for j in range(len(L[0])):            
            L[i][j].destroy()   
    L = []
    for i in range(len(P)):
        L.append([])
        for j in range(len(P[0])):
            but = tk.Button(text="", bd=5, font=('Arial', 13), bg =P[i][j][2], fg='black',width=6,height=3, command=lambda x=i, y=j:help_but_click(x, y))
            but.grid(row=i+3, column=j+10, stick='wens', padx=5, pady=5)
            L[-1].append(but)

Counts = []
def help_with_kill_count():
    global Counts
    for elem in Counts:
        elem.destroy()
    for i in range(1, players + 1):
        for a in range(len(P)):
            for b in range(len(P[0])):
                if P[a][b][1] == i:
                    text_ = tk.Label(text="Счёт игрока " + str(i) + " : " + str(P[a][b][3]),font=('Arial, 15'),bg="#72F011")
                    Counts.append(text_)
                    Counts[-1].place(x=1300,y=200 + 40 * (i - 1))
   
def help_for_all_functions():
    global P
    global cords
    global hint, hint_
    help_clear()
    for i in range(len(P)):
        for j in range(len(P[0])):
            if P[i][j][1] != 0:
                cords[P[i][j][1] - 1] = [i, j]

def help_clear():
    global hint, hint_
    hint.destroy()
    hint_.destroy()

def help_to_show(L):
    s = ""
    for elem in L:
        if elem != 0:
            s += str(elem)
            s += " "
    return s[:-1]


# GLOBAL VARIABLES
L = []
S = []
cords = []
P = [[[[i for i in range(1, players + 1)], 0, "white", 0] for j in range(size)] for k in range(size)]
hint=tk.Label()
hint_= tk.Label()
index = -1
player_number = 1
killed = 1
num = 1
# POINT PLAYERS AND SIZE ON LiNES 11, 12
# NEXT FUNCTIONS FOR BEGINING GAME:

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)
win.grid_columnconfigure(6, minsize=60)
win.grid_columnconfigure(7, minsize=60)
win.grid_columnconfigure(8, minsize=60)
win.grid_columnconfigure(9, minsize=60)
win.grid_columnconfigure(10, minsize=60)

win.grid_rowconfigure(1, minsize=70)
win.grid_rowconfigure(2, minsize=70)
win.grid_rowconfigure(3, minsize=70)
win.grid_rowconfigure(4, minsize=70)
win.grid_rowconfigure(5, minsize=70)
win.grid_rowconfigure(6, minsize=70)
win.grid_rowconfigure(7, minsize=70)
win.grid_rowconfigure(8, minsize=70)
win.grid_rowconfigure(9, minsize=70)
win.grid_rowconfigure(10, minsize=70)
show(P)


def help_for_begin():
    global num, S, cords, P, hint
    if num <= players:
        if len(S) == 1 and S[0] not in cords:
            hint.destroy()
            cords.append(S[0])
            P[S[0][0]][S[0][1]][1] = num
            num += 1
            if num <= players:
                hint = tk.Label(text="Игрок номер " + str(num) + " укажите своего \nперсонажа так, чтобы этого никто не \nвидел и нажмте кнопку 'Продолжить'",font=('Arial, 20'),bg="#72F011")
                hint.place(x=70,y=350)
            else:
                hint = tk.Label(text="Да начнется игра!",font=('Arial, 40'),bg="#72F011")
                hint.place(x=70,y=350)
        show(P)
    else:
        begin()
    S = []

    
hint = tk.Label(text="Игрок номер " + str(num) + " укажите своего \nперсонажа так, чтобы этого никто не\n видел и нажмте кнопку 'Продолжить'",font=('Arial, 20'),bg="#72F011")
hint.place(x=80,y=350)
begin_ = tk.Button(text="Продолжить", bd=5, font=('Arial', 13),fg='red',width=20,height=2,command=lambda :help_for_begin())
begin_.place(x=200,y=500)
_begin_ = tk.Label(text="Подготовка к игре",font=('Arial, 60'),bg="#72F011")
_begin_.place(x=500, y=30)


def begin():
    global aboba
    global killed
    global S
    global P
    global ALL_P
    S = []
    killed = 0
    begin_.destroy()
    hint.destroy()
    _begin_.destroy()
    aboba = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    aboba.place(x=720, y=60)
    aboba = tk.Label(text="Ход игрока " + str(player_number),font=('Arial, 30'),bg="#72F011")
    aboba.place(x=720, y=60)
    help_with_kill_count()
    K = tk.Button(text="Убить", bd=5, font=('Arial', 13),fg='red',width=20,height=2,command=lambda : kill())
    Q = tk.Button(text="Спросить", bd=5, font=('Arial', 13), fg='red',width=20,height=2, command=lambda : question())
    V = tk.Button(text="Вертикальная чистка", bd=5, font=('Arial', 13),width=20, height=2, fg='red',command=lambda : vertical_clear())
    H = tk.Button(text="Горизонтальная чистка", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : horizontal_clear())
    D = tk.Button(text="Вниз", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : down())
    U = tk.Button(text="Вверх", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : up())
    R = tk.Button(text="Вправо", bd=5, font=('Arial', 13),width=20, height=2, fg='red',command=lambda : right())
    L_ = tk.Button(text="Влево", bd=5, font=('Arial', 13), width=20,height=2,fg='red',command=lambda : left())
    C = tk.Button(text="Отменить", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : cancel())
    F = tk.Button(text="Вперёд", bd=5, font=('Arial', 13),width=20,height=2, fg='red',command=lambda : forward())
    K.place(x=65, y=75)
    Q.place(x=270,y=75)
    V.place(x=270,y=285)
    H.place(x=65, y=285)
    D.place(x=65,y=215)
    U.place(x=270,y=215)
    R.place(x=270, y=145)
    L_.place(x=65,y=145)
    C.place(x=65, y=355)
    F.place(x=270,y=355)
    P_ = copy.deepcopy(P)
    ALL_P = [P_]
    Show(P)
win.mainloop()