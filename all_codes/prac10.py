import random
a = random.randint(1,20)
def rps(a):
    keep_going = True
    b = int(input("Enter the number in range of 1 to 20: "))
    while keep_going:
        if a > b:
            print("Raise your Choice")
            b = int(input("Enter the number: "))
        elif a < b:
            print("Lower your Choice")
            b = int(input("Enter the number: "))
        elif a == b:
            print("You got it that's the correct answer")
            c = input("Wanna play again y/n: ")
            a = random.randint(1,20)
            if(c=='y' or c=='Y'):
                b = int(input("Enter the number: "))
            elif(c=='n' or c=='N'):
                keep_going=False
            else:
                c = input("Invalid input enter again y/n: ")
       
rps(a)