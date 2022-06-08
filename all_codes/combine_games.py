from games.games import *

choice = int(input('''
        Hello Everyone 
        Which game do you want to play today 
        Here's the menu 
        1-> Sasta IPL 0_0
        2-> Number Guessing Game
        3-> Rock Paper Scissor: '''))
while True:
        if choice == 1:
                ipl()
        elif choice == 2:
                guess_game()
        elif choice == 3:
                rock_paper_scissor()
        else:
                print('Nothing')
        again = input("Do you Want to Play Again Enter in Y/N: ").upper()
        if again == 'Y':
                continue
        elif again == 'N':
                break
        else:
                print("Invalid input")
                print("Thank You for Playing with us")
