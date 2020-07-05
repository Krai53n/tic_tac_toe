# TicTacToe game made on tkinter
import tkinter as tk
from tkinter import messagebox as mb
from sys import exit as sysexit


root = tk.Tk()
root.title('Tic-Tac-Toe')
root.resizable(0, 0)


### CONSTANTS
win_fields = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6))


### for move
move = 'x'
fields = ['*', '*', '*', '*', '*', '*', '*', '*', '*']


### FUNCTIONS
def mover(field_num):
    '''
    Function put the step to self.move list
    and get the number from commands self.cmd_f_{0..8}
    '''
    fields[field_num] = move
    __change_move()
    __check_win()


def __change_move():
    '''
    Function change move
    '''
    global move
    if move == 'x':
        move = 'o'
    else:
        move = 'x'


def __check_win():
    '''
    Function check the winner
    '''
    for i in range(len(win_fields)):
        nums = win_fields[i]
        signs = []
        for m in nums:
            signs.append(fields[m])

        if ((signs[0] == signs[1]) and (signs[1] == signs[2]) and
            (signs[0] == signs[2])):
            if signs[0] != '*':
                __finish_game(signs[0])


def __finish_game(sign):
    sign = sign.upper()
    mes = 'The {} win\nRestart the game?\n\
Yes - restart. No - quit'.format(sign)
    restart = mb.askquestion(message = mes)
    if restart == 'yes':
        __restart()
    else:
        sysexit()

def __restart():
    global move, fields
    move = 'x'
    fields = ['*', '*', '*', '*', '*', '*', '*', '*', '*']

    field_0['text'] = ''
    field_1['text'] = ''
    field_2['text'] = ''
    field_3['text'] = ''
    field_4['text'] = ''
    field_5['text'] = ''
    field_6['text'] = ''
    field_7['text'] = ''
    field_8['text'] = ''


### commands for fields
def cmd_f_0():
    if fields[0] == '*':
        field_0['text'] = move
        mover(0)
        if fields[0] == 'x':
            field_0['foreground'] = 'red'
            field_0['activeforeground'] = 'red'
        else:
            field_0['foreground'] = 'blue'
            field_0['activeforeground'] = 'blue'

def cmd_f_1():
    if fields[1] == '*':
        field_1['text'] = move
        mover(1)
        if fields[1] == 'x':
            field_1['foreground'] = 'red'
            field_1['activeforeground'] = 'red'
        else:
            field_1['foreground'] = 'blue'
            field_1['activeforeground'] = 'blue'

def cmd_f_2():
    if fields[2] == '*':
        field_2['text'] = move
        mover(2)
        if fields[2] == 'x':
            field_2['foreground'] = 'red'
            field_2['activeforeground'] = 'red'
        else:
            field_2['foreground'] = 'blue'
            field_2['activeforeground'] = 'blue'

def cmd_f_3():
    if fields[3] == '*':
        field_3['text'] = move
        mover(3)
        if fields[3] == 'x':
            field_3['foreground'] = 'red'
            field_3['activeforeground'] = 'red'
        else:
            field_3['foreground'] = 'blue'
            field_3['activeforeground'] = 'blue'

def cmd_f_4():
    if fields[4] == '*':
        field_4['text'] = move
        mover(4)
        if fields[4] == 'x':
            field_4['foreground'] = 'red'
            field_4['activeforeground'] = 'red'
        else:
            field_4['foreground'] = 'blue'
            field_4['activeforeground'] = 'blue'

def cmd_f_5():
    if fields[5] == '*':
        field_5['text'] = move
        mover(5)
        if fields[5] == 'x':
            field_5['foreground'] = 'red'
            field_5['activeforeground'] = 'red'
        else:
            field_5['foreground'] = 'blue'
            field_5['activeforeground'] = 'blue'

def cmd_f_6():
    if fields[6] == '*':
        field_6['text'] = move
        mover(6)
        if fields[6] == 'x':
            field_6['foreground'] = 'red'
            field_6['activeforeground'] = 'red'
        else:
            field_6['foreground'] = 'blue'
            field_6['activeforeground'] = 'blue'

def cmd_f_7():
    if fields[7] == '*':
        field_7['text'] = move
        mover(7)
        if fields[7] == 'x':
            field_7['foreground'] = 'red'
            field_7['activeforeground'] = 'red'
        else:
            field_7['foreground'] = 'blue'
            field_7['activeforeground'] = 'blue'

def cmd_f_8():
    if fields[8] == '*':
        field_8['text'] = move
        mover(8)
        if fields[8] == 'x':
            field_8['foreground'] = 'red'
            field_8['activeforeground'] = 'red'
        else:
            field_8['foreground'] = 'blue'
            field_8['activeforeground'] = 'blue'


### buttons which is fields
field_0 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_0
                )
field_0.grid()

field_1 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_1
                )
field_1.grid(row = 0, column = 1)

field_2 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_2
                )
field_2.grid(row = 0, column = 2)

field_3 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_3
                )
field_3.grid(row = 1)

field_4 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_4
                )
field_4.grid(row = 1, column = 1)

field_5 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_5
                )
field_5.grid(row = 1, column = 2)

field_6 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_6
                )
field_6.grid(row = 2)

field_7 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_7
                )
field_7.grid(row = 2, column = 1)

field_8 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_8
                )
field_8.grid(row = 2, column = 2)


root.mainloop()
