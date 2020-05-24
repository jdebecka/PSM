import tkinter as tk
from tkinter import *
from Service.Game_Of_life import Game_Of_life
import numpy as np


class UserInterface(Frame):

    def __init__(self):
        super().__init__(master=None)

        # Default params
        self.isPlaying = True
        self.gol = None
        self.rule_1 = '2'
        self.rule_2 = '2'
        self.rule_3 = '3'
        self.number_of_cells = 40

        # rules
        self.rule = 'Rules'
        self.rule_1_txt = f"Any live cell with fewer than {self.rule_1} live neighbours dies, as if by underpopulation."
        self.rule_2_txt = f"Any live cell with more than {self.rule_2} ive neighbours dies, as if by overpopulation."
        self.rule_3_txt = f"Any dead cell with exactly {self.rule_3} live neighbours becomes a live cell, as if by " \
                          f"reproduction. "

        self.dict = dict()
        # Containers
        self.canvas = Canvas(root, bg='black', width=605, height=605)
        self.control_panel = Frame(root, bg='#fcba03')

        # Components

        # Buttons
        self.button = Button(root, text='Start Game', command=self.start_game)
        self.button_stop = Button(root, text='Stop Game', command=self.stop_game)

        # Spin boxes
        self.rule_1_spin_box = Spinbox(self.control_panel, from_=1, to=8, width=10)
        self.rule_2_spin_box = Spinbox(self.control_panel, from_=1, to=8, width=10)
        self.rule_3_spin_box = Spinbox(self.control_panel, from_=1, to=8, width=10)

        self.button_1_spin_box = Button(self.control_panel, text='Change rule', command=self.change_rule_1, bg='yellow', fg='#fcba03', state=DISABLED)
        self.button_2_spin_box = Button(self.control_panel, text='Change rule', command=self.change_rule_2, bg='black', fg='#fcba03', state=DISABLED)
        self.button_3_spin_box = Button(self.control_panel, text='Change rule', command=self.change_rule_3, bg='black', fg='#fcba03', state=DISABLED)

        self.self_rule_1_lbl = Label(self.control_panel, text=self.rule_1_txt, bg="#fcba03")
        self.self_rule_1_lbl = Label(self.control_panel, text=self.rule_1_txt, bg="#fcba03")
        self.self_rule_2_lbl = Label(self.control_panel, text=self.rule_2_txt, bg="#fcba03")
        self.self_rule_3_lbl = Label(self.control_panel, text=self.rule_3_txt, bg="#fcba03")

        # Pack labels
        self.self_rule_1_lbl.place(relx=.3, rely=.1, anchor="center")
        self.self_rule_2_lbl.place(relx=.3, rely=.3, anchor="center")
        self.self_rule_3_lbl.place(relx=.3, rely=.5, anchor="center")

        self.rule_1_spin_box.place(relx=.7, rely=.1, anchor="center")
        self.rule_2_spin_box.place(relx=.7, rely=.3, anchor="center")
        self.rule_3_spin_box.place(relx=.7, rely=.5, anchor="center")

        self.button_1_spin_box.place(relx=.9, rely=.1, anchor="center")
        self.button_2_spin_box.place(relx=.9, rely=.3, anchor="center")
        self.button_3_spin_box.place(relx=.9, rely=.5, anchor="center")

        # Put on the window
        self.canvas.place(relx=.5, rely=.35, anchor="center")
        self.button.place(relx=.4, rely=.72, anchor="center")
        self.button_stop.place(relx=.6, rely=.72, anchor="center")
        self.control_panel.place(relx=.5, rely=.9, relwidth=1.0, relheight=0.3, anchor="center")

        self.init_board(self.number_of_cells)

    def change_rule_1(self):
        new_rule = self.rule_1_spin_box.get()
        self.rule_1 = new_rule
        self.rule_1_txt = f"Any live cell with fewer than {self.rule_1} live neighbours dies, as if by underpopulation."
        self.self_rule_1_lbl["text"] = self.rule_1_txt
        new_rule = int(new_rule)

        self.gol.rule_1 = new_rule

    def change_rule_2(self):
        new_rule = self.rule_2_spin_box.get()
        self.rule_2 = new_rule
        self.rule_2_txt = f"Any live cell with more than {self.rule_2} live neighbours dies, as if by overpopulation."
        self.self_rule_2_lbl["text"] = self.rule_2_txt
        new_rule = int(new_rule)

        self.gol.rule_2 = new_rule

    def change_rule_3(self):
        new_rule = self.rule_3_spin_box.get()
        self.rule_3 = new_rule
        self.rule_3_txt = f"Any dead cell with exactly {self.rule_3} live neighbours becomes a live cell, as if by " \
                          f"reproduction. "
        self.self_rule_3_lbl["text"] = self.rule_3_txt
        new_rule = int(new_rule)

        self.gol.rule_3 = new_rule

    def init_board(self, num):
        y = 5

        self.master.title("Colours")
        self.pack(fill=BOTH, expand=1)
        dx = 600 / num
        for i in range(num):
            x = 5
            for j in range(num):
                self.dict[(i, j)] = self.canvas.create_rectangle(x, y, x + dx, y + dx, outline="#fcba03", fill="white")
                x += dx
            y += dx

    def stop_game(self):
        self.isPlaying = False

    def start_game(self):
        self.button_1_spin_box.configure(state=NORMAL)
        self.button_2_spin_box.configure(state=NORMAL)
        self.button_3_spin_box.configure(state=NORMAL)
        self.isPlaying = True
        if self.gol is None:
            self.gol = Game_Of_life(self.number_of_cells, int(self.rule_1), int(self.rule_2), int(self.rule_3))
            self.gol.start_game()
        self.play()

    def play(self):
        index = 0

        while self.isPlaying:
            if index == 0:
                self.update_board(self.gol.game_arr, True)
            else:
                self.update_board(self.gol.game_arr)
            index += 1

    def update_board(self, game_list: list, just_started=False):
        for i in range(len(game_list)):
            i_check = i + 1

            if i_check == len(game_list):
                i_check = 0

            if not self.gol.game_arr[i].__contains__(1) and self.gol.game_arr[i - 1].__contains__(1) and \
                    self.gol.game_arr[i_check].__contains__(1):
                continue
            if not self.isPlaying:
                break

            for j in range(len(game_list)):
                # Calling update on game board
                if not just_started:
                    self.gol.play_game(i, j)

                # Adjusting interface
                if game_list[i][j] == 1:
                    self.canvas.itemconfig(self.dict[(i, j)], fill='#fcba03')
                    self.canvas.update()
                else:
                    self.canvas.itemconfig(self.dict[(i, j)], fill='white')
                    self.canvas.update()


root = Tk()
ex = UserInterface()
root.geometry("950x950+300+300")
root.bind("<Return>", )
root.mainloop()
