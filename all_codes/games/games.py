import random

from pyparsing import originalTextFor

#sasta ipl game goes here.
def ipl():
    print('''
            Hello and welcome to IPL 
        ''')
    total_teams = ['CSK','RCB','KXIP','KKR','DC','SHR','LSR','RR','GT','MI']
    for team in total_teams:
        print(team,end=' ')
    choose_team = input("\nEnter your Team: ").upper()
    while True:
        if choose_team in total_teams:
            break
        else:
            print("\n",total_teams)
            choose_team = input("\nEnter your Team from given list only: \n").upper()
    opp_team = random.choice(total_teams)
    while True:
        if opp_team == choose_team:
           opp_team = random.choice(total_teams)
        else:
            break
    print(f"\n\t\t\tMy Team: {choose_team}")
    print(f"\n\t\t\tOpponent Team: {opp_team}")
    print("Now its time for toss")
    possible_toss = ['H','T']
    rand_toss = random.choice(possible_toss)
    given_toss = input("Enter your toss in \'H/T\': ").upper()
    while True:
        if given_toss == 'H' or given_toss == 'T':
            break
        else:
            given_toss = input("Enter your toss in \'H/t\': ").upper()
    if rand_toss == given_toss:
        print(f"{choose_team} got the toss")
        toss = int(input('''
            Choose 1-> Batting
                   2-> Balling: '''))
        if toss == 1:
            batting_first = choose_team
            print(f"{batting_first} got batting")
        else:
            batting_first = opp_team
            print(f"{batting_first} got batting")
    else:
        print(f"{opp_team} got the toss")
        toss = random.choice(possible_toss)
        if toss == 'H':
            batting_first = opp_team
            print(f"{batting_first} got batting")
        else:
            batting_first = choose_team
            print(f"{batting_first} got batting")
    ball_no = 1
    temp0 = 0
    sum0 = 0
    sum1 = 0
    possible_no = [0,1,2,3,4,6,'out','runout','lbw','wb']
    if batting_first == choose_team:
        while ball_no<=10:
            input()
            random_run = random.choice(possible_no)
            print(f"{choose_team}-{sum0}/{temp0} Ball-{ball_no} : {random_run}")
            ball_no += 1
            if type(random_run) == int:
                sum0 += random_run
            elif random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
                temp0 += 1
            elif random_run == 'wb':
                ball_no -= 1
            else:
                continue
            if temp0 == 2:
                break
        ball_no = 1
        temp0 = 0
        print(f"Team {opp_team} got batting and requiered {sum0+1} to win the match")     
        #print(f"Team {opp_team} got balling and {team} requiered {sum0+1} to win this match")
        while ball_no<=10:
            input()
            random_run = random.choice(possible_no)
            print(f"\n{opp_team}-{sum1}/{temp0} Ball-{ball_no} : {random_run}")
            ball_no += 1
            if type(random_run)==int:
                sum1 += random_run
            if random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
                temp0 += 1
            elif random_run == 'wb':
                ball_no -= 1
            else:
                continue
            if temp0 == 2:
                break
            if (sum0+1)<sum1:
                break
    if batting_first == opp_team:
        while ball_no<=10:
            input()
            random_run = random.choice(possible_no)
            print(f"{opp_team}-{sum0}/{temp0} Ball-{ball_no} : {random_run}")
            ball_no += 1
            if type(random_run) == int:
                sum0 += random_run
            elif random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
                temp0 += 1
            elif random_run == 'wb':
                ball_no -= 1
            else:
                continue
            if temp0 == 2:
                break
        ball_no = 1
        temp0 = 0
        #print(f"Team {opp_team} got batting and requiered {sum0+1} to win the match")     
        print(f"Team {opp_team} got balling and {choose_team} requiered {sum0+1} to win this match")
        while ball_no<=10:
            input()
            random_run = random.choice(possible_no)
            print(f"\n{opp_team}-{sum1}/{temp0} Ball-{ball_no} : {random_run}")
            ball_no += 1
            if type(random_run)==int:
                sum1 += random_run
            if random_run == 'out' or random_run == 'runout' or random_run == 'lbw':
                temp0 += 1
            elif random_run == 'wb':
                ball_no -= 1
            else:
                continue
            if temp0 == 2:
                break
            if (sum0+1)<sum1:
                break
    if sum0 > sum1:
        if toss == 'H':
            print(f"\nTeam {team} wins with {sum0-sum1} runs")
        else:
            print(f'\nTeam {opp_team} wins with {sum0-sum1} runs')
    elif sum0< sum1:
        if toss == 'H':
            print(f"\nTeam {opp_team} wins with {sum1-sum0} runs")
        else:
            print(f'\nTeam {team} wins with {sum1-sum0} runs')
    else:
        print("\nMatch Tied")
#Number gurssing game goes here
def guess_game():
    print("Lets Play number guessing Game")
    random_no = random.randint(0,100)
    Guessings = 1
    total_lst = []
    print('''\n \'\'\'If you want some help then type hint/h so that you can get range of number 
    and if you want to quit game type exit/e to quit game\'\'\' \n''')
    choosen_number = input("Enter the your first choice: ")
    while True:
        if choosen_number.isdigit():
            choosen_number = int(choosen_number)
            break
        else:
            print("Kindly Enter Number only")
            choosen_number = input("Enter the number again: ")
    while True: 
        if choosen_number>(random_no+10):
            print("Hmm too high low your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number<(random_no+10) and choosen_number>random_no:
            print("Hmm Little high low your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number<(random_no-10):
            print("Hmm too low high your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number == 'h' or choosen_number =='H' or choosen_number == 'HINT' or choosen_number == 'Hint' or choosen_number == 'hint':
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        elif choosen_number>(random_no-10) and choosen_number<random_no:
            print("Hmm little low high your choice bit")
            choosen_number = input("Enter the number: ")
            while True:
                if choosen_number.isdigit():
                    choosen_number = int(choosen_number)
                    break
                elif choosen_number.startswith("h") or choosen_number.startswith("H"):
                    print(f"Hint:- The number lies in range of {random_no-11} and {random_no+12}")
                    choosen_number = input("Enter the number: ")
                elif choosen_number == 'e' or choosen_number =='E' or choosen_number == 'EXIT' or choosen_number == 'Exit' or choosen_number == 'exit':
                    print("Thank you for playing with us")
                    exit()
                else:
                    print("Kindly Enter Number only")
                    choosen_number = input("Enter the number: ")
            Guessings += 1
        else:
            print(f"You got that number and your total number of guess is {Guessings}")
            if Guessings>=15:
                print(f"Your average Guessing Rate is Low")
            elif Guessings<15 and Guessings>=10:
                print("Your Average Guessing Rate is moderate")
            elif Guessings<10 and Guessings>=5:
                print("your Average Guessing Rate is medium")
            else:
                print("Your Average Guessing Rate is awsome")
            total_lst.append(Guessings)
            break
def rock_paper_scissor():
    my_score = []
    comp_score = []
    available_choice = ['ROCK','PAPER','SCISSOR']
    hits = 1
    while hits <= 5:
        hits += 1
        my_choice  = input("Enter your choice in Rock/Paper/Scissor: ").upper()
        comp_choice = random.choice(available_choice)
        if my_choice == comp_choice:
            print("Round Tied")
            print("No one got the point This round")
            my_score.append(0)
            comp_score.append(0)
            hits -= 1
        elif my_choice == 'ROCK':
            if comp_choice == 'PAPER':
                print(f'{comp_choice}')
                print("you lost this round")
                print("Computer Got 1 Point")
                comp_score.append(1)
            elif comp_choice == 'SCISSOR':
                print(f'{comp_choice}')
                print("You Won this round")
                print("You Got 1 Point")
                my_score.append(1)
        elif my_choice == 'PAPER':
            if comp_choice == 'ROCK':
                print(f'{comp_choice}')
                print("You Won this round")
                print("You Got 1 Point")
                my_score.append(1)
            elif comp_choice == 'SCISSOR':
                print(f'{comp_choice}')
                print("you lost this round")
                print("Computer Got 1 Point")
                comp_score.append(1)
        elif my_choice == 'SCISSOR':
            if comp_choice == 'ROCK':
                print(f'{comp_choice}')
                print("you lost this round")
                print("Computer Got 1 Point")
                comp_score.append(1)
            elif comp_choice == 'PAPER':
                print(f'{comp_choice}')
                print("You Won this round")
                print("You Got 1 Point")
                my_score.append(1)
        else:
            pass
        my_total = my_score.count(1)
        comp_total = comp_score.count(1)
    if my_total < comp_total:
        print(f'Computer Won The Match by {comp_total-my_total}')
    elif my_total > comp_total:
        print(f'Congratulation')
        print(f'You wan the Match by {my_total-comp_total}')
    else:
        print("Match Tied")
    print('Thank you For playing With us ')