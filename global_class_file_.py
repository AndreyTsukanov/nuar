import tkinter as tk
import random
import copy


class Game_without_cards:
    def update(self, players, size):
        self.turn = tk.Label()
        self.History = []
        self.bg_ = "#DAA520"
        self.Buttons = []
        self.Clicked_Buttons = []
        self.hint_label = tk.Label()
        self.hint_topic = tk.Label()
        self.index_turn = -1
        self.killed_person = 1
        self.num = 1
        self.k = (
            8 + 1 * (size == 5) + 2 * (size == 4) + 3 * (size == 3) - 1 * (size == 7)
        )
        self.Counts = []
        self.people_alive = size**2
        self.player_cords = []
        self.player_turn = [i for i in range(1, players + 1)]
        self.player_trophy = [0 for i in range(players)]
        self.player_number = 1
        self.ok_button_ = tk.Button()
        self.Table = [[["", 0, "white"] for j in range(size)] for k in range(size)]
        self.NAMES = [
            "Ксавье",
            "Ирма",
            "Кэтрин",
            "Куинтон",
            "Саймон",
            "Франклин",
            "Горацио",
            "Касим",
            "Педро",
            "Джулиан",
            "Дарнелл",
            "Ивонн",
            "Ульбрехт",
            "Бэррин",
            "Улис",
            "Женева",
            "Картрайт",
            "Таша",
            "Маркус",
            "Фиби",
            "Закари",
            "Грейс",
            "Ванда",
            "Дейдра",
            "Рамон",
            "Эвелин",
            "Изольда",
            "Сюзанна",
            "Райан",
            "Элисс",
            "Клайв",
            "Кристоф",
            "Линнетт",
            "Натан",
            "Эштон",
            "Брэнсон",
            "Мэрион",
            "Вильгельм",
            "Эрнест",
            "Дружок",
            "Нейл",
            "Джек",
            "Офелия",
            "Флоренс",
            "Хьюберт",
            "Владимир",
            "Винсан",
            "Тревор",
            "Лайнус",
            "Иван",
        ]
        self.PLAYERS_NAMES = []
        for i in range(size**2):
            j = random.randint(0, len(self.NAMES) - 1)
            self.Table[i // size][i % size][0] = self.NAMES[j]
            self.PLAYERS_NAMES.append(self.NAMES[j])
            self.NAMES.pop(j)
        self.players = players
        self.size = size
        self.dead_label = tk.Label()
        self.dead_topic = tk.Label()
        self.dead_button = tk.Button()
        self.name = ""
        self.ok_button = tk.Button()
        self.name_label = tk.Button()
        self.HELP_BUTTON = tk.Button()
        self.begin_button = tk.Button()

    def change_table(self):
        self.Table = [
            [
                [[i for i in range(1, self.players + 1)], 0, "white"]
                for j in range(self.size)
            ]
            for k in range(self.size)
        ]


def left(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="Укажите любую ячейку строки, \nкоторую надо сдвинуть влево...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][0]
            for j in range(len(game.Table[0]) - 1):
                game.Table[n][j], game.Table[n][j + 1] = (
                    game.Table[n][j + 1],
                    game.Table[n][j],
                )
            help_for_player_turn(game)
            help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def down(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="Укажите любую ячейку столбца, \nкоторый надо сдвинуть вниз...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][1]
            for i in range(-1, -len(game.Table), -1):
                game.Table[i][n], game.Table[i - 1][n] = (
                    game.Table[i - 1][n],
                    game.Table[i][n],
                )
            help_for_player_turn(game)
            help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def up(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="Укажите любую ячейку столбца, \nкотороый надо сдвинуть вверх...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][1]
            for i in range(len(game.Table) - 1):
                game.Table[i][n], game.Table[i + 1][n] = (
                    game.Table[i + 1][n],
                    game.Table[i][n],
                )
            help_for_player_turn(game)
            help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def right(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="Укажите любую ячейку строки, \nкоторую надо сдвинуть вправо...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != 1:
            game.hint_label.place(x=70, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            n = game.Clicked_Buttons[-1][0]
            for j in range(-1, -len(game.Table[0]), -1):
                game.Table[n][j], game.Table[n][j - 1] = (
                    game.Table[n][j - 1],
                    game.Table[n][j],
                )
            help_for_player_turn(game)
            help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def Show(game:Game_without_cards):
    for i in range(len(game.Buttons)):
        for j in range(len(game.Buttons[0])):
            game.Buttons[i][j].destroy()
    game.Buttons = []
    for i in range(len(game.Table)):
        game.Buttons.append([])
        for j in range(len(game.Table[0])):
            if game.Table[i][j][2] == "black":
                but = tk.Button(
                    text=help_to_show(game.Table[i][j][0]),
                    bd=5,
                    font=("Arial", 13),
                    bg=game.Table[i][j][2],
                    fg="white",
                    width=10,
                    height=4,
                    command=lambda x=i, y=j: help_but_click(game, x, y),
                )
            else:
                but = tk.Button(
                    text=help_to_show(game.Table[i][j][0]),
                    bd=5,
                    font=("Arial", 13),
                    bg=game.Table[i][j][2],
                    fg="black",
                    width=10,
                    height=4,
                    command=lambda x=i, y=j: help_but_click(game, x, y),
                )
            but.grid(row=i + 3, column=j + game.k, stick="wens", padx=5, pady=5)
            game.Buttons[-1].append(but)


def help_to_show(list_):
    s = ""
    if type(list_) == str:
        return list_
    for elem in list_:
        if elem != 0:
            s += str(elem)
            s += " "
    s = s[:-1]
    return s


def help_for_player_turn(game:Game_without_cards):
    if game.index_turn != -1:
        for i in range(-1, game.index_turn, -1):
            game.History.pop(-1)
    game.index_turn = -1
    game.player_number = game.player_turn[
        (game.player_turn.index(game.player_number) + 1) % len(game.player_turn)
    ]
    help_with_player(game)
    Table_ = copy.deepcopy(game.Table)
    player_turn_ = game.player_turn[:]
    player_cords_ = game.player_cords[:]
    player_trophy_ = game.player_trophy[:]
    PLAYERS_NAMES_ = game.PLAYERS_NAMES[:]
    copy_ = [
        Table_,
        player_cords_,
        player_trophy_,
        player_turn_,
        game.player_number,
        game.people_alive,
        PLAYERS_NAMES_,
    ]
    game.History.append(copy_)


def help_but_click(game:Game_without_cards, x, y):
    if [x, y] not in game.Clicked_Buttons:
        but = tk.Button(
            text=help_to_show(game.Table[x][y][0]),
            bd=5,
            width=10,
            height=4,
            font=("Arial", 13),
            bg="gray",
            fg="black",
            command=lambda i=x, j=y: help_but_click(game, i, j),
        )
        game.Buttons[x][y].destroy()
        game.Buttons[x][y] = but
        but.grid(row=x + 3, column=y + game.k, stick="wens", padx=5, pady=5)
        game.Clicked_Buttons.append([x, y])
    else:
        if game.Table[x][y][2] == "black":
            but = tk.Button(
                text=help_to_show(game.Table[x][y][0]),
                bd=5,
                width=10,
                height=4,
                font=("Arial", 13),
                bg=game.Table[x][y][2],
                fg="white",
                command=lambda i=x, j=y: help_but_click(game, i, j),
            )
        else:
            but = tk.Button(
                text=help_to_show(game.Table[x][y][0]),
                bd=5,
                width=10,
                height=4,
                font=("Arial", 13),
                bg=game.Table[x][y][2],
                fg="black",
                command=lambda i=x, j=y: help_but_click(game, i, j),
            )
        game.Buttons[x][y].destroy()
        game.Buttons[x][y] = but
        but.grid(row=x + 3, column=y + game.k, stick="wens", padx=5, pady=5)
        game.Clicked_Buttons.pop(game.Clicked_Buttons.index([x, y]))


def help_with_player(game:Game_without_cards):
    game.turn.destroy()
    game.turn = tk.Label(
        text="Ход игрока " + str(game.player_number), font=("Arial, 30"), bg=game.bg_
    )
    game.turn.place(x=720, y=60)


def help_with_players_cords(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    for i in range(len(game.Table)):
        for j in range(len(game.Table[0])):
            if game.Table[i][j][1] != 0:
                game.player_cords[game.Table[i][j][1] - 1] = [i, j]


def horizontal_clear(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="В каждой из "
        + str(len(game.Table))
        + " строк выберите по одной\n чёрной ячейке для горизонтальной очистки...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != len(game.Table):
            game.hint_label.place(x=30, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            a = set()
            for j in range(len(game.Table)):
                if (
                    game.Table[game.Clicked_Buttons[-j - 1][0]][
                        game.Clicked_Buttons[-j - 1][1]
                    ][2]
                    == "black"
                ):
                    a.add(game.Clicked_Buttons[-j - 1][0])
            if len(a) != len(game.Table):
                game.hint_label.place(x=30, y=590)
                game.hint_topic.place(x=120, y=510)
            else:
                for i in range(1, len(game.Table) + 1):
                    (game.Table[game.Clicked_Buttons[-i][0]]).pop(
                        game.Clicked_Buttons[-i][1]
                    )
                help_for_player_turn(game)
                help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def vertical_clear(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_label = tk.Label(
        text="В каждом из "
        + str(len(game.Table[0]))
        + " столбцов выберите по одной \nчёрной ячейке для вертикальной очистки...",
        font=("Arial, 15"),
        bg=game.bg_,
        fg="black",
    )
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    if game.killed_person == 0:
        if len(game.Clicked_Buttons) != len(game.Table[0]):
            game.hint_label.place(x=30, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            a = set()
            for j in range(1, len(game.Table[0]) + 1):
                if (
                    game.Table[game.Clicked_Buttons[-j][0]][
                        game.Clicked_Buttons[-j][1]
                    ][2]
                    == "black"
                ):
                    a.add(game.Clicked_Buttons[-j][1])
            if len(a) != len(game.Table[0]):
                game.hint_label.place(x=30, y=590)
                game.hint_topic.place(x=120, y=510)
            else:
                P_1 = [
                    [game.Table[i][j] for i in range(len(game.Table))]
                    for j in range(len(game.Table[0]))
                ]
                for i in range(1, len(game.Table[0]) + 1):
                    (P_1[game.Clicked_Buttons[-i][1]]).pop(game.Clicked_Buttons[-i][0])
                game.Table = [
                    [P_1[i][j] for i in range(len(P_1))] for j in range(len(P_1[0]))
                ]
                help_for_player_turn(game)
                help_with_players_cords(game)
        game.Clicked_Buttons = []
        Show(game)


def help_with_kill_count(game:Game_without_cards):
    for elem in game.Counts:
        elem.destroy()
    for i in range(1, game.players + 1):
        text_ = tk.Label(
            text="Счёт игрока " + str(i) + " : " + str(game.player_trophy[i - 1]),
            font=("Arial, 15"),
            bg=game.bg_,
        )
        game.Counts.append(text_)
        game.Counts[-1].place(x=1300, y=200 + 40 * (i - 1))


def cancel_turn(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    game.hint_label = tk.Label(
        text="Вы вернулись в начало игры!", font=("Arial, 15"), bg=game.bg_, fg="black"
    )
    if game.killed_person == 0:
        if game.index_turn == -len(game.History) or len(game.History) == 1:
            game.hint_label.place(x=90, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            game.index_turn -= 1
            P_1 = copy.deepcopy(game.History[game.index_turn])
            game.Table = copy.deepcopy(P_1[0])
            game.player_cords = P_1[1][:]
            game.player_trophy = P_1[2][:]
            game.player_turn = P_1[3][:]
            game.player_number = P_1[4]
            game.people_alive = P_1[5]
            game.PLAYERS_NAMES = P_1[6][:]
            help_with_player(game)
            help_with_players_cords(game)
            help_with_kill_count(game)
        Show(game)


def forward_turn(game:Game_without_cards):
    game.hint_label.destroy()
    game.hint_topic.destroy()
    game.hint_topic = tk.Label(text="Подсказка:", font=("Arial, 30"), bg=game.bg_)
    game.hint_label = tk.Label(
        text="Вы вернулись в конец игры!", font=("Arial, 15"), bg=game.bg_, fg="black"
    )
    if game.killed_person == 0:
        if game.index_turn == -1:
            game.hint_label.place(x=90, y=590)
            game.hint_topic.place(x=120, y=510)
        else:
            game.index_turn += 1
            P_1 = copy.deepcopy(game.History[game.index_turn])
            game.Table = copy.deepcopy(P_1[0])
            game.player_cords = P_1[1][:]
            game.player_trophy = P_1[2][:]
            game.player_turn = P_1[3][:]
            game.player_number = P_1[4]
            game.people_alive = P_1[5]
            game.PLAYERS_NAMES = P_1[6]
            help_with_player(game)
            help_with_players_cords(game)
            help_with_kill_count(game)
        Show(game)
