'''
TicTacToe game made on tkinter
'''


import tkinter as tk


### CONSTANTS


class Application(tk.Frame):
    '''
    Application class which draw all that we can see
    '''
    def __init__(self, master):
        '''
        Draw all of tictactoe
        '''
        super().__init__(master)
        self.grid()
        self.create_widgets()
    

    def create_widgets(self):
        '''
        Built buttons as fields
        '''
        field_0 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_0.grid()

        field_1 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_1.grid(row = 0, column = 1)

        field_2 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_2.grid(row = 0, column = 2)

        field_3 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_3.grid(row = 1)

        field_4 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_4.grid(row = 1, column = 1)

        field_5 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_5.grid(row = 1, column = 2)

        field_6 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_6.grid(row = 2)

        field_7 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_7.grid(row = 2, column = 1)

        field_8 = tk.Button(
                        self,
                        text = '',
                        font = ('SourceCodePro-Bold', 50),
                        width = 2,
                        bd = 1
                        )
        field_8.grid(row = 2, column = 2)


if __name__ == '__main__':
    '''
    Launch our application
    call his
    and make loop
    '''
    root = tk.Tk()
    root.resizable(0, 0)
    root.title('TicTacToe')
    app = Application(root)
    app.mainloop()
