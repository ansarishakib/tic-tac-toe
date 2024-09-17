import tkinter #tk-interface (GUI library)

def set_title(row,column):
    global curr
    
    if(gameOver):
        return
    
    if board[row][column]["text"] != "":
        #alreadytaken spot
        return
    
    board[row][column]["text"]= curr

    if curr==playerO:
        curr=playerX
    else:
        curr=playerO

    label["text"]= curr+"'s turn"

    #check winner
    check_winner()

def check_winner():
    global turns,gameOver
    turns +=1

    #horizontal check
    for row in range(3):
        if (board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"] and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_gray)
            gameOver=True
            return
    #vertical check
    for column in range(3):
        if(board[0][column]["text"]==board[1][column]["text"]==board[2][column]["text"] and board[0][column]["text"]!=""):
            label.config(text=board[0][column]["text"]+" is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_gray)
            gameOver=True
            return
    #check diagonally
    if (board[0][0]["text"]==board[1][1]["text"]==board[2][2]["text"] and board[0][0]["text"]!=""):
        label.config(text=board[0][0]["text"]+" is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(foreground=color_yellow,background=color_light_gray)
        gameOver=True
        return
    #check anti-diagonal
    if (board[0][2]["text"]==board[1][1]["text"]==board[2][0]["text"] and board[0][2]["text"]!=""):
        label.config(text=board[0][2]["text"]+" is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        gameOver=True
        return
    if turns==9:
        gameOver=True
        label.config(text="Tie!!!",foreground=color_yellow)


def new_game():
    global turns,gameOver
    turns=0
    gameOver=False

    label.config(text=curr+"'s turn", foreground="white")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="",foreground=color_blue,background=color_gray)

    
#game setup
playerX= "X"
playerO= "O"
curr= playerX
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]

color_blue= "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray="#646464"

turns=0
gameOver=False

#window setup
window = tkinter.Tk() #create game window
window.title("Tic Tac Toe")
window.resizable(False,False)

frame= tkinter.Frame(window)
label = tkinter.Label(frame,text=curr+"'s turn", font=("Consolas",20),background=color_gray, foreground="white")

label.grid(row=0,column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] =  tkinter.Button(frame,text="",font=("Consolas",50,"bold"), background=color_gray, foreground= color_blue, width=4, height=1,command=lambda row=row, column=column : set_title(row,column))
        board[row][column].grid(row=row+1,column=column)


button = tkinter.Button(frame, text="Restart",font=("Consolas",20), background=color_gray,foreground="white", command=new_game)
button.grid(row=4,column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width = window.winfo_width()
window_height= window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height= window.winfo_screenheight()

window_x = int((screen_width/2)-(window_width/2))
window_y = int((screen_height/2)-(window_height/2))


#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()

