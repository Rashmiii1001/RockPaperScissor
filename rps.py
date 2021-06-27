from tkinter import *
import random

root = Tk()
root.title("ROCK PAPER SCISSOR GAME")
width = 690
height = 690
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2)- (width/2)
y = (screen_height / 2)- (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="violet")


blank_image = PhotoImage(file="blank.png") #used to add user friendly images in the app
rock_player = PhotoImage(file="rock_player.png")
rock_player_ado = rock_player.subsample(3, 3)
paper_player = PhotoImage(file="paper_player.png")
paper_player_ado = paper_player.subsample(3, 3)
scissor_player = PhotoImage(file="scissor_player.png")
scissor_player_ado = scissor_player.subsample(3, 3)
rock_computer = PhotoImage(file="rock_computer.png")
paper_computer = PhotoImage(file="paper_computer.png")
scissor_computer = PhotoImage(file="scissor_computer.png")
global score
score = 0

def Rock():
    global player_option
    player_option = 1
    player_image.configure(image=rock_player)
    MatchProcess()


def Paper():
    global player_option
    player_option = 2
    player_image.configure(image=paper_player)
    MatchProcess()


def Scissor():
    global player_option
    player_option = 3
    player_image.configure(image=scissor_player)
    MatchProcess()


def MatchProcess():
    computer_option = random.randint(1, 3)
    if computer_option == 1:
        computer_image.configure(image=rock_computer)
        RockCom()
    elif computer_option == 2:
        computer_image.configure(image=paper_computer)
        PaperCom()
    elif computer_option == 3:
        computer_image.configure(image=scissor_computer)
        ScissorCom()


def RockCom():
    global score
    if player_option == 1:
        status_label.config(text="Game Tie", bg="black")
    elif player_option == 2:
        status_label.config(text="Player Win", bg="black")
        score += 1
        score_label.config(text=score)
    elif player_option == 3:
        status_label.config(text="Computer Win", bg="black")
        score -= 1
        score_label.config(text=score)

def PaperCom():
    global score
    if player_option == 1:
        status_label.config(text="Computer Win", bg="black")
        score -= 1
        score_label.config(text=score)
    elif player_option == 2:
        status_label.config(text="Game Tie", bg="black")
    elif player_option == 3:
        status_label.config(text="Player Win", bg="black")
        score += 1
        score_label.config(text=score)



def ScissorCom():
    global score
    if player_option == 1:
        status_label.config(text="Player Win", bg="black")
        score += 1
        score_label.config(text=score)
    elif player_option == 2:
        status_label.config(text="Computer Win", bg="black")
        score -= 1
        score_label.config(text=score)
    elif player_option == 3:
        status_label.config(text="Game Tie", bg="black")


def ExitApplication():
    root.destroy()
    exit()



player_image = Label(root, image=blank_image)
player_image.grid(row=3, column=1, padx=30, pady=20)
computer_image = Label(root, image=blank_image)
computer_image.grid(row=3, column=3, pady=20)
player_label = Label(root, text="PLAYER")
player_label.grid(row=2, column=1)
player_label.config(bg="black", fg="white", font=('Times New Roman', 18, 'bold'))
computer_label = Label(root, text="COMPUTER")
computer_label.grid(row=2, column=3)
computer_label.config(bg="black", fg="white", font=('Times New Roman', 18, 'bold'))
status_label = Label(root, text="", font=('Times New Roman', 12))
status_label.grid(row=4, column=2)
status_label.config(bg="violet", fg="white", font=('Times New Roman', 20, 'bold'))

score_label = Label(root, text=score, font=('Times New Roman', 12))
score_label.grid(row=5, column=2, pady=10)
score_label.config(bg="black", fg="white", font=('Times New Roman', 20, 'bold'))

rock = Button(root, image=rock_player_ado, command=Rock)
paper = Button(root, image=paper_player_ado, command=Paper)
scissor = Button(root, image=scissor_player_ado, command=Scissor)
button_quit = Button(root, text="Quit", bg="blue", fg="black", font=('Times New Roman', 22, 'bold'), command=ExitApplication)
rock.grid(row=6, column=1, pady=30)
paper.grid(row=6, column=2, pady=30)
scissor.grid(row=6, column=3, pady=30)
button_quit.grid(row=7, column=2)


if __name__ == '__main__':
    root.mainloop()
