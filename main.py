# TicTacToe game made on tkinter
import tkinter as tk
from tkinter import messagebox as mb
from sys import exit as sysexit


### CONSTANTS
WIN_FIELDS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), # constant variable
              (0, 3, 6), (1, 4, 7), (2, 5, 8), # where we set
              (0, 4, 8), (2, 4, 6))            # win fields
# colors of signs
COLOR_X = '#51CFC8'
COLOR_O = '#f5b849'
BACKGROUND = '#28313D'

### BUILDING WINDOW
root = tk.Tk()             # settings
root.title('Tic-Tac-Toe')  # of
root.resizable(0, 0)       # window
root.config(bg = BACKGROUND)


### for move
move = 'x'
fields = ['*', '*', '*', '*', '*', '*', '*', '*', '*'] # empty fields


### FUNCTIONS
def mover(field_num):
    '''
    Function put the step to self.move list
    and get the number from commands self.cmd_f_{0..8}
    and call changing of step,
    call chek win
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
    for i in range(len(WIN_FIELDS)):    # iterates through 8 win cases
        nums = WIN_FIELDS[i]            # tuple of 3 numbers
        signs = []                      # signs for next 2 lines
        for m in nums:
            # iterates 3 times where get the number from num
            signs.append(fields[m])     # and add value of the number
        
        # check if three symbols are equal
        if ((signs[0] == signs[1]) and (signs[1] == signs[2]) and
            (signs[0] == signs[2])):
            # throw away '*' symbol
            if signs[0] != '*':
                __finish_game(signs[0])


def __finish_game(sign):
    '''
    Close function where we get the sign from __chek_win
    '''
    sign = sign.upper()                       # make the sign upper
    # our message after finish the game
    mes = 'The {} win\nRestart the game?\n\
Yes - restart. No - quit'.format(sign)
    restart = mb.askquestion(message = mes)   # messagebox with mes
    if restart == 'yes':
        __restart()
    else:
        sysexit()

def __restart():
    '''
    Function which change the values of move and fiels
    to the our standart
    '''
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


### COMMANDS FOR FIELDS
'''
All this commands work in the same way
if in the exact field we have '*' then we put it our move,
then call function mover with argument,
after if our step depending on our sign, we paint the field
'''
def cmd_f_0():
    if fields[0] == '*':
        field_0['text'] = move
        mover(0)
        if fields[0] == 'x':
            field_0['foreground'] = COLOR_X
            field_0['activeforeground'] = COLOR_X
        else:
            field_0['foreground'] = COLOR_O
            field_0['activeforeground'] = COLOR_O

def cmd_f_1():
    if fields[1] == '*':
        field_1['text'] = move
        mover(1)
        if fields[1] == 'x':
            field_1['foreground'] = COLOR_X
            field_1['activeforeground'] = COLOR_X
        else:
            field_1['foreground'] = COLOR_O
            field_1['activeforeground'] = COLOR_O

def cmd_f_2():
    if fields[2] == '*':
        field_2['text'] = move
        mover(2)
        if fields[2] == 'x':
            field_2['foreground'] = COLOR_X
            field_2['activeforeground'] = COLOR_X
        else:
            field_2['foreground'] = COLOR_O
            field_2['activeforeground'] = COLOR_O

def cmd_f_3():
    if fields[3] == '*':
        field_3['text'] = move
        mover(3)
        if fields[3] == 'x':
            field_3['foreground'] = COLOR_X
            field_3['activeforeground'] = COLOR_X
        else:
            field_3['foreground'] = COLOR_O
            field_3['activeforeground'] = COLOR_O

def cmd_f_4():
    if fields[4] == '*':
        field_4['text'] = move
        mover(4)
        if fields[4] == 'x':
            field_4['foreground'] = COLOR_X
            field_4['activeforeground'] = COLOR_X
        else:
            field_4['foreground'] = COLOR_O
            field_4['activeforeground'] = COLOR_O

def cmd_f_5():
    if fields[5] == '*':
        field_5['text'] = move
        mover(5)
        if fields[5] == 'x':
            field_5['foreground'] = COLOR_X
            field_5['activeforeground'] = COLOR_X
        else:
            field_5['foreground'] = COLOR_O
            field_5['activeforeground'] = COLOR_O

def cmd_f_6():
    if fields[6] == '*':
        field_6['text'] = move
        mover(6)
        if fields[6] == 'x':
            field_6['foreground'] = COLOR_X
            field_6['activeforeground'] = COLOR_X
        else:
            field_6['foreground'] = COLOR_O
            field_6['activeforeground'] = COLOR_O

def cmd_f_7():
    if fields[7] == '*':
        field_7['text'] = move
        mover(7)
        if fields[7] == 'x':
            field_7['foreground'] = COLOR_X
            field_7['activeforeground'] = COLOR_X
        else:
            field_7['foreground'] = COLOR_O
            field_7['activeforeground'] = COLOR_O

def cmd_f_8():
    if fields[8] == '*':
        field_8['text'] = move
        mover(8)
        if fields[8] == 'x':
            field_8['foreground'] = COLOR_X
            field_8['activeforeground'] = COLOR_X
        else:
            field_8['foreground'] = COLOR_O
            field_8['activeforeground'] = COLOR_O


### buttons which is fields
field_0 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_0,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_0.grid()

field_1 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_1,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_1.grid(row = 0, column = 1)

field_2 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_2,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_2.grid(row = 0, column = 2)

field_3 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_3,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_3.grid(row = 1)

field_4 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_4,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_4.grid(row = 1, column = 1)

field_5 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_5,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_5.grid(row = 1, column = 2)

field_6 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_6,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_6.grid(row = 2)

field_7 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_7,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_7.grid(row = 2, column = 1)

field_8 = tk.Button(
                text = '',
                font = ('SourceCodePro-Bold', 50),
                width = 2,
                bd = 1,
                command = cmd_f_8,
                bg = BACKGROUND,
                activebackground = BACKGROUND
                )
field_8.grid(row = 2, column = 2)


root.mainloop()
