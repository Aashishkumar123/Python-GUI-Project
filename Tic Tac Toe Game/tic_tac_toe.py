from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe Game')

# Player 1 [X] starts first, Player 2 [O] continues
clicked = True
count = 0

# To disable all the buttons when someone has won the game
def disableButtons():
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)

    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)

    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

# To check whether did anyone won the game and restart the game when someone won the game 
def checkWinner():
    global winner
    winner = False

    # Player 1 [X] winning patterns
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg="#80ffaa")                                        #[X][X][X]
        button2.config(bg="#80ffaa")                                        #[O][O][ ]
        button3.config(bg="#80ffaa")                                        #[ ][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.config(bg="#80ffaa")                                        #[O][O][ ]
        button5.config(bg="#80ffaa")                                        #[X][X][X]
        button6.config(bg="#80ffaa")                                        #[ ][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.config(bg="#80ffaa")                                        #[ ][ ][ ]
        button8.config(bg="#80ffaa")                                        #[O][O][ ]
        button9.config(bg="#80ffaa")                                        #[X][X][X]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.config(bg="#80ffaa")                                        #[X][O][ ]
        button4.config(bg="#80ffaa")                                        #[X][O][ ]
        button7.config(bg="#80ffaa")                                        #[X][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.config(bg="#80ffaa")                                        #[O][X][ ]
        button5.config(bg="#80ffaa")                                        #[O][X][ ]
        button8.config(bg="#80ffaa")                                        #[ ][X][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.config(bg="#80ffaa")                                        #[ ][O][X]
        button6.config(bg="#80ffaa")                                        #[ ][O][X]
        button9.config(bg="#80ffaa")                                        #[ ][ ][X]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.config(bg="#80ffaa")                                        #[X][O][ ]
        button5.config(bg="#80ffaa")                                        #[ ][X][ ]
        button9.config(bg="#80ffaa")                                        #[ ][O][X]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.config(bg="#80ffaa")                                        #[ ][O][X]
        button5.config(bg="#80ffaa")                                        #[ ][X][ ]
        button7.config(bg="#80ffaa")                                        #[X][O][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 1 is the Winner!")
        disableButtons
        start()

    # Player 2 [O] winning patterns
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg="#80ffaa")                                        #[O][O][O]
        button2.config(bg="#80ffaa")                                        #[X][X][ ]
        button3.config(bg="#80ffaa")                                        #[X][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.config(bg="#80ffaa")                                        #[X][X][ ]
        button5.config(bg="#80ffaa")                                        #[O][O][O]
        button6.config(bg="#80ffaa")                                        #[X][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.config(bg="#80ffaa")                                        #[X][ ][ ]
        button8.config(bg="#80ffaa")                                        #[X][X][ ]
        button9.config(bg="#80ffaa")                                        #[O][O][O]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.config(bg="#80ffaa")                                        #[O][X][X]
        button4.config(bg="#80ffaa")                                        #[O][X][ ]
        button7.config(bg="#80ffaa")                                        #[O][ ][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.config(bg="#80ffaa")                                        #[X][O][X]
        button5.config(bg="#80ffaa")                                        #[X][O][ ]
        button8.config(bg="#80ffaa")                                        #[ ][O][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.config(bg="#80ffaa")                                        #[X][X][O]
        button6.config(bg="#80ffaa")                                        #[ ][X][O]
        button9.config(bg="#80ffaa")                                        #[ ][ ][O]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.config(bg="#80ffaa")                                        #[O][X][X]
        button5.config(bg="#80ffaa")                                        #[ ][O][ ]
        button9.config(bg="#80ffaa")                                        #[ ][X][O]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.config(bg="#80ffaa")                                        #[X][X][O]
        button5.config(bg="#80ffaa")                                        #[ ][O][ ]
        button7.config(bg="#80ffaa")                                        #[O][X][ ]
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Player 2 is the Winner!")
        disableButtons
        start()

# To check whether the game is a draw
def checkDraw():
    global count, winner

    if count == 9 and winner == False:
        messagebox.showerror("Tic Tac Toe", "Draw, play again!")
        start()

# To determine the buttons that Player 1 or Player 2 has clicked on
def buttonClicked(button):
    global clicked, count

    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("Tic Tac Toe", "Please select another box.")

# To start or restart the game
def start():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, count
    clicked = True
    count = 0

    # Building the buttons for the game
    button1 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button3))

    button4 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button5))
    button6 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button6))

    button7 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica, 20"), height=3, width=7, bg="SystemButtonFace", command=lambda: buttonClicked(button9))

    # Arranging the buttons on the screen for the game
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)

    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)

    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)

# Create game menu
gameMenu = Menu(root)
root.config(menu = gameMenu)

# Create game options menu
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)


start()
root.mainloop()