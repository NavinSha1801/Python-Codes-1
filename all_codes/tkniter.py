from tkinter import *
import random

screen = Tk()

var_count = IntVar()
var_countcom = IntVar()
var_comp_choice = StringVar()
var_user_choice = StringVar()
choice_computer = 'Null'
choice_user = 'Null'
var_won = StringVar()
won = 'null'
count = 0
countcom = 0
choice = ['Rock','Paper','Scissor']

def counter(msg):
    global count,countcom,won
    if msg == 'Rock':
        choice_user = 'ROCK'
        rand_choice = random.choice(choice)
        if rand_choice == msg:
            count = 0
            countcom = 0
            choice_computer = 'ROCK'
            won = 'Draw'
        elif rand_choice == 'Paper':
            countcom += 1
            choice_computer = 'PAPER'
            won = 'Computer Won'
        elif rand_choice == 'Scissor':
            count += 1
            won = 'User Won'
            choice_computer = 'SCISSOR'
    elif msg == 'Paper':
        choice_user = 'PAPER'
        rand_choice = random.choice(choice)
        if rand_choice == msg:
            count = 0
            countcom = 0
            won = 'Draw'
            choice_computer = 'PAPER'
        elif rand_choice == 'Scissor':
            countcom += 1
            won = "Computer Won"
            choice_computer = 'SCISSOR'
        elif rand_choice == 'Rock':
            count += 1
            won = 'User Won'
            choice_computer = 'ROCK'
    else:
        choice_user = 'SCISSOR'
        rand_choice = random.choice(choice)
        if rand_choice == msg:
            count = 0
            won = 'Draw'
            countcom = 0
            choice_computer = 'SCISSOR'
        elif rand_choice == 'Rock':
            countcom += 1
            won = "Computer Won"
            choice_computer = 'ROCK'
        elif rand_choice == 'Paper':
            count += 1
            won = 'User Won'
            choice_computer = 'PAPER'
    var_count.set(count)
    var_countcom.set(countcom)
    var_won.set(won)
    var_comp_choice.set(choice_computer)
    var_user_choice.set(choice_user)

screen.title('Welcome to Game')
screen.geometry('1920x1080')

btn = Button(screen,text='Rock',command=lambda:counter('Rock'),font=('Arial',20,'bold'))
btn.place(x=0,y=20)

btn = Button(screen,text='Paper',command=lambda:counter('Paper'),font=('Arial',20,'bold'))
btn.place(x=560,y=20)

btn = Button(screen,text='Scissor',command=lambda:counter('Paper'),font=('Arial',20,'bold'))
btn.place(x=1220,y=20)

lbl = Label(screen,text = 'User: ',font=('Arial',20,'bold'))
lbl.place(x=0,y=100)

lbl = Label(screen,textvariable=var_user_choice,font=('Arial',20,'bold'))
lbl.place(x=560,y=100)

lbl = Label(screen,textvariable=var_count,font=('Arial',20,'bold'))
lbl.place(x=1220,y=100)

lbl = Label(screen,text = 'computer: ',font=('Arial',20,'bold'))
lbl.place(x=0,y=200)

lbl = Label(screen,textvariable=var_comp_choice,font=('Arial',20,'bold'))
lbl.place(x=560,y=200)

lbl = Label(screen,textvariable=var_countcom,font=('Arial',20,'bold'))
lbl.place(x=1220,y=200)

lbl = Label(screen,textvariable=var_won,font=('Arial',20,'bold'))
lbl.place(x=560,y=560)

screen.mainloop()