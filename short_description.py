def description():
    import desc_strings
    import tkinter as tk

    window = tk.Tk()
    # print(window.winfo_screenwidth())
    # print(window.winfo_screenheight())
    window.attributes("-fullscreen", True)
    window.geometry("1650x900")
    window["bg"] = "#72F011"
    window.title("НУАР без карт")
    window.image = tk.PhotoImage(file="Background.png")
    bg_logo = tk.Label(window, image=window.image)
    bg_logo.place(x=0, y=0)

    class descriptions:
        def __init__(self):
            self.begin_topic = tk.Label(
                text="Описания режимов", font=("Arial, 60"), bg="green"
            )
            self.list_utils_for_description = []
            self.list_utils_modes = []

    game = descriptions()

    def start_description():
        while len(game.list_utils_modes) > 0:
            game.list_utils_modes[-1].destroy()
            game.list_utils_modes.pop(-1)
        game.begin_topic = tk.Label(
            text="Описания режимов", font=("Arial, 60"), bg="green"
        )
        game.begin_topic.place(x=430, y=100)
        m_1 = tk.Button(
            text="ОДИН ПРОТИВ ВСЕХ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#DAA520",
            command=lambda: description_1(),
        )
        m_2 = tk.Button(
            text="НУАР БЕЗ КАРТ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#DAA520",
            command=lambda: description_2(),
        )
        m_3 = tk.Button(
            text="СЫЩИК ПРОТИВ ВОРА",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#DAA520",
            command=lambda: description_3(),
        )
        m_4 = tk.Button(
            text="В МЕНЮ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#db5a32",
            command=lambda: window.destroy(),
        )
        m_1.place(x=400, y=280)
        m_2.place(x=900, y=280)
        m_3.place(x=400, y=530)
        m_4.place(x=900, y=530)
        game.list_utils_for_description = [m_1, m_2, m_3, m_4, game.begin_topic]

    def description_1():
        while len(game.list_utils_for_description) > 0:
            game.list_utils_for_description[-1].destroy()
            game.list_utils_for_description.pop(-1)
        game.begin_topic = tk.Label(
            text="Описание режима\n ОДИН ПРОТИВ ВСЕХ", font=("Arial, 40"), bg="green"
        )
        game.begin_topic.place(x=540, y=20)
        sense_topic = tk.Label(
            text="В чём суть режима?", font=("Arial, 35"), bg="#ad77e6", bd=15
        )
        sense_topic.place(x=20, y=240)
        sense_label = tk.Label(
            text=desc_strings.sense_1,
            width=40,
            font=("Arial, 15"),
            bg="#ad77e6",
            justify=tk.LEFT,
            bd=15,
        )
        sense_label.place(x=20, y=309)
        how_to_play_topic = tk.Label(
            text="Как ходить?", width=17, font=("Arial, 35"), bg="#DAA520", bd=15
        )
        how_to_play_topic.place(x=600, y=170)
        how_to_play_label = tk.Label(
            text=desc_strings.how_to_play_1,
            width=44,
            font=("Arial, 15"),
            bg="#DAA520",
            justify=tk.LEFT,
        )
        how_to_play_label.place(x=600, y=241)
        to_menu = tk.Button(
            text="В МЕНЮ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#db5a32",
            command=lambda: window.destroy(),
        )
        to_menu.place(x=1200, y=500)
        to_description = tk.Button(
            text="К ОПИСАНИЯМ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#1fc0ed",
            command=lambda: start_description(),
        )
        to_description.place(x=1200, y=300)
        game.list_utils_modes = [
            sense_topic,
            game.begin_topic,
            sense_label,
            how_to_play_topic,
            how_to_play_label,
            to_menu,
            to_description,
        ]

    def description_2():
        while len(game.list_utils_for_description) > 0:
            game.list_utils_for_description[-1].destroy()
            game.list_utils_for_description.pop(-1)
        game.begin_topic = tk.Label(
            text="Описание режима\n НУАР БЕЗ КАРТ",
            font=("Arial, 40"),
            bg="green",
            width=20,
        )
        game.begin_topic.place(x=520, y=20)
        sense_topic = tk.Label(
            text="В чём суть режима?", font=("Arial, 35"), bg="#ad77e6", bd=15
        )
        sense_topic.place(x=20, y=240)
        sense_label = tk.Label(
            text=desc_strings.sense_2,
            width=40,
            font=("Arial, 15"),
            bg="#ad77e6",
            justify=tk.LEFT,
            bd=15,
        )
        sense_label.place(x=20, y=309)
        how_to_play_topic = tk.Label(
            text="Как ходить?", width=17, font=("Arial, 35"), bg="#DAA520", bd=15
        )
        how_to_play_topic.place(x=600, y=170)
        how_to_play_label = tk.Label(
            text=desc_strings.how_to_play_2,
            width=44,
            font=("Arial, 15"),
            bg="#DAA520",
            justify=tk.LEFT,
        )
        how_to_play_label.place(x=600, y=241)
        to_menu = tk.Button(
            text="В МЕНЮ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#db5a32",
            command=lambda: window.destroy(),
        )
        to_menu.place(x=1200, y=500)
        to_description = tk.Button(
            text="К ОПИСАНИЯМ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#1fc0ed",
            command=lambda: start_description(),
        )
        to_description.place(x=1200, y=300)
        game.list_utils_modes = [
            sense_topic,
            game.begin_topic,
            sense_label,
            how_to_play_topic,
            how_to_play_label,
            to_menu,
            to_description,
        ]

    def description_3():
        while len(game.list_utils_for_description) > 0:
            game.list_utils_for_description[-1].destroy()
            game.list_utils_for_description.pop(-1)
        game.begin_topic = tk.Label(
            text="Описание режима\n СЫЩИК ПРОТИВ ВОРА", font=("Arial, 40"), bg="green"
        )
        game.begin_topic.place(x=520, y=20)
        sense_topic = tk.Label(
            text="В чём суть режима?", font=("Arial, 35"), bg="#ad77e6", bd=15
        )
        sense_topic.place(x=20, y=240)
        sense_label = tk.Label(
            text=desc_strings.sense_3,
            width=40,
            font=("Arial, 15"),
            bg="#ad77e6",
            justify=tk.LEFT,
            bd=15,
        )
        sense_label.place(x=20, y=309)
        how_to_play_topic = tk.Label(
            text="Как ходить?", width=17, font=("Arial, 35"), bg="#DAA520", bd=15
        )
        how_to_play_topic.place(x=600, y=220)
        how_to_play_label = tk.Label(
            text=desc_strings.how_to_play_3,
            width=44,
            font=("Arial, 15"),
            bg="#DAA520",
            justify=tk.LEFT,
        )
        how_to_play_label.place(x=600, y=291)
        to_menu = tk.Button(
            text="В МЕНЮ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#db5a32",
            command=lambda: window.destroy(),
        )
        to_menu.place(x=1200, y=500)
        to_description = tk.Button(
            text="К ОПИСАНИЯМ",
            font=("Arial, 15"),
            bd=20,
            width=22,
            height=4,
            bg="#1fc0ed",
            command=lambda: start_description(),
        )
        to_description.place(x=1200, y=300)
        game.list_utils_modes = [
            sense_topic,
            game.begin_topic,
            sense_label,
            how_to_play_topic,
            how_to_play_label,
            to_menu,
            to_description,
        ]

    start_description()

    window.mainloop()
