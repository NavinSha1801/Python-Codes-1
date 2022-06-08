import random
rand_int = random.randint(0,10)
temp = 1
user_guess = input("Enter the Number: ")
while True:
    if user_guess.isdigit():
        user_guess = (int)(user_guess)
        break
    else:
        print("Kindly Enter Number only")
        user_guess = input("Enter the Number again: ")
# main code goes here
while True: 
    if rand_int < user_guess:
        print("Your guess is high, low down a little bit")
        user_guess = input("Enter the Number: ")
        temp += 1
        while True:
            if user_guess.isdigit():
                user_guess = (int)(user_guess)
                break
            else:
                print("Kindly Enter Number only")
                user_guess = input("Enter the Number again: ")
    elif rand_int > user_guess:
        print("Your guess is Low, up a little bit")
        user_guess = input("Enter the Number: ")
        temp += 1
        while True:
            if user_guess.isdigit():
                user_guess = (int)(user_guess)
                break
            else:
                print("Kindly Enter Number only")
                user_guess = input("Enter the Number again: ")
    else:
        print("Yep you got this")
        print(f"You got this number in {temp} atempts")
        break
