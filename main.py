# TicTacToe game made on tkinter
from tkinter import Tk
from tkinter import Button as TkButton
from tkinter import messagebox as mb
from sys import exit as sysexit


### CONSTANTS
WIN_FIELDS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), # constant variable
              (0, 3, 6), (1, 4, 7), (2, 5, 8), # where we set
              (0, 4, 8), (2, 4, 6))            # win fields


class Button(TkButton):
    '''Button is a piece of game field'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
                         **kwargs,
                         master = root,
                         text = '',
                         font = (FONT, SIZE),
                         width = 2,
                         bd = 1,
                         bg = BACKGROUND,
                         activebackground = BACKGROUND
                         )

    def load_config(self):
        from json import load
        with open('config.json', 'r') as rf:
            data = load(rf)
        for i in data.items():
            exec('self.{} = "{}"'.format(i[0], i[1]))

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Tic-Tac-Toe')
        self.master.resizable(0, 0)
        self.master.config(bg = BACKGROUND)
        self.create_widgets()
        # GAME LOGIC
        self.move = 'x'
        # empty fields
        self.fields = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

    def create_widgets(self):
        self.field_0 = Button(command = self.cmd_f_0)
        self.field_1 = Button(command = self.cmd_f_1)
        self.field_2 = Button(command = self.cmd_f_2)
        self.field_3 = Button(command = self.cmd_f_3)
        self.field_4 = Button(command = self.cmd_f_4)
        self.field_5 = Button(command = self.cmd_f_5)
        self.field_6 = Button(command = self.cmd_f_6)
        self.field_7 = Button(command = self.cmd_f_7)
        self.field_8 = Button(command = self.cmd_f_8)
        self.field_0.grid()
        self.field_1.grid(row = 0, column = 1)
        self.field_2.grid(row = 0, column = 2)
        self.field_3.grid(row = 1)
        self.field_4.grid(row = 1, column = 1)
        self.field_5.grid(row = 1, column = 2)
        self.field_6.grid(row = 2)
        self.field_7.grid(row = 2, column = 1)
        self.field_8.grid(row = 2, column = 2)

    def mover(self, field_num):
        '''
        Function put the step to self.move list
        and get the number from commands self.cmd_f_{0..8}
        and call changing of step,
        call chek win
        '''
        self.fields[field_num] = self.move
        self.__change_move()


    def __change_move(self):
        '''
        Function change move
        '''
        if self.move == 'x':
            self.move = 'o'
        else:
            self.move = 'x'


    def __check_win(self):
        '''
        Function check the winner
        '''
        for i in range(len(WIN_FIELDS)):     # iterates through 8 win cases
            nums = WIN_FIELDS[i]             # tuple of 3 numbers
            signs = []                       # signs for next 2 lines
            for m in nums:
                # iterates 3 times where get the number from num
                signs.append(self.fields[m]) # and add value of the number

            # check if three symbols are equal
            if ((signs[0] == signs[1]) and (signs[1] == signs[2]) and
                (signs[0] == signs[2])):
                # throw away '*' symbol
                if signs[0] != '*':
                    self.__finish_game(signs[0])

    def __finish_game(self, sign):
        '''
        Close function where we get the sign from __chek_win
        '''
        print('\a') # make bip
        sign = sign.upper()                       # make the sign upper
        # our message after finish the game
        mes = 'The {} win\nRestart the game?\n'.format(sign)
        mes += 'Yes - restart. No - quit'
        restart = mb.askquestion(message = mes)   # messagebox with mes
        if restart == 'yes':
            self.__restart()
        else:
            sysexit()

    def __restart(self):
        '''
        Function which change the values of move and fiels
        to the our standart
        '''
        self.move = 'x'
        self.fields = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

        self.field_0['text'] = ''
        self.field_1['text'] = ''
        self.field_2['text'] = ''
        self.field_3['text'] = ''
        self.field_4['text'] = ''
        self.field_5['text'] = ''
        self.field_6['text'] = ''
        self.field_7['text'] = ''
        self.field_8['text'] = ''


    ### COMMANDS FOR FIELDS
    '''
    All this commands work in the same way
    if in the exact field we have '*' then we put it our move,
    then call function mover with argument,
    after if our step depending on our sign, we paint the field
    '''
    def cmd_f_0(self):
        if self.fields[0] == '*':
            self.field_0['text'] = self.move
            self.mover(0)
            if self.fields[0] == 'x':
                self.field_0['foreground'] = COLOR_X
                self.field_0['activeforeground'] = COLOR_X
            else:
                self.field_0['foreground'] = COLOR_O
                self.field_0['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_1(self):
        if self.fields[1] == '*':
            self.field_1['text'] = self.move
            self.mover(1)
            if self.fields[1] == 'x':
                self.field_1['foreground'] = COLOR_X
                self.field_1['activeforeground'] = COLOR_X
            else:
                self.field_1['foreground'] = COLOR_O
                self.field_1['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_2(self):
        if self.fields[2] == '*':
            self.field_2['text'] = self.move
            self.mover(2)
            if self.fields[2] == 'x':
                self.field_2['foreground'] = COLOR_X
                self.field_2['activeforeground'] = COLOR_X
            else:
                self.field_2['foreground'] = COLOR_O
                self.field_2['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_3(self):
        if self.fields[3] == '*':
            self.field_3['text'] = self.move
            self.mover(3)
            if self.fields[3] == 'x':
                self.field_3['foreground'] = COLOR_X
                self.field_3['activeforeground'] = COLOR_X
            else:
                self.field_3['foreground'] = COLOR_O
                self.field_3['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_4(self):
        if self.fields[4] == '*':
            self.field_4['text'] = self.move
            self.mover(4)
            if self.fields[4] == 'x':
                self.field_4['foreground'] = COLOR_X
                self.field_4['activeforeground'] = COLOR_X
            else:
                self.field_4['foreground'] = COLOR_O
                self.field_4['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_5(self):
        if self.fields[5] == '*':
            self.field_5['text'] = self.move
            self.mover(5)
            if self.fields[5] == 'x':
                self.field_5['foreground'] = COLOR_X
                self.field_5['activeforeground'] = COLOR_X
            else:
                self.field_5['foreground'] = COLOR_O
                self.field_5['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_6(self):
        if self.fields[6] == '*':
            self.field_6['text'] = self.move
            self.mover(6)
            if self.fields[6] == 'x':
                self.field_6['foreground'] = COLOR_X
                self.field_6['activeforeground'] = COLOR_X
            else:
                self.field_6['foreground'] = COLOR_O
                self.field_6['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_7(self):
        if self.fields[7] == '*':
            self.field_7['text'] = self.move
            self.mover(7)
            if self.fields[7] == 'x':
                self.field_7['foreground'] = COLOR_X
                self.field_7['activeforeground'] = COLOR_X
            else:
                self.field_7['foreground'] = COLOR_O
                self.field_7['activeforeground'] = COLOR_O
        self.__check_win()

    def cmd_f_8(self):
        if self.fields[8] == '*':
            self.field_8['text'] = self.move
            self.mover(8)
            if self.fields[8] == 'x':
                self.field_8['foreground'] = COLOR_X
                self.field_8['activeforeground'] = COLOR_X
            else:
                self.field_8['foreground'] = COLOR_O
                self.field_8['activeforeground'] = COLOR_O
        self.__check_win()


if __name__ == '__main__':
    # ---------------------------------------------- #
    # ---------  START INITIALIZE COLORS ----------- #
    from json import load
    with open('config.json', 'r') as rf:
        data = load(rf)
    for i in data.items():
        exec('{} = "{}"'.format(i[0], i[1]))
    # ----------- END INITIALIZE COLORS ------------ #
    # ---------------------------------------------- #
    root = Tk()
    mnw = MainWindow(root)
    root.mainloop()
