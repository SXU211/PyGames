import tkinter

def set_tile(row, column):
    pass


playerX = 'X'
playerO = 'O'
curr_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]


color_black = '#171717'
color_blue = "#063EF7"
color_gray = '#808080'
color_light_gray = '#D3D3D3'


window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)



frame = tkinter.Frame(window)
label = tkinter.Label(frame, text= curr_player + "'s turn", font=('Arial', 20), background=color_black, 
                      foreground="white")

label.grid(row = 0, column = 0)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background= color_gray, foreground = color_blue, width = 4, height = 1,
                                            command = lambda row = row, column = column: set_tile(row, column))




frame.pack()


window.mainloop()



