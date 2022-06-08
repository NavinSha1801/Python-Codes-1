import random
a = random.randint(1,20)
def rps(a):
    keep_going = True
    while keep_going:
        b = int(input("Enter the number in range of 1 to 20: "))
        if a > b:
            print("Raise your Choice")
            rps(a)
        elif a < b:
            print("Lower your Choice")
            rps(a)
        elif a == b:
            print("You got it that's the correct answer")
            c = input("Wanna play again y/n: ")
            if(c=='y' or c=='Y'):
                a = random.randint(1,20)
                rps(a)
            elif(c=='n' or c=='N'):
                keep_going=False
                
            else:
                c = input("Invalid input enter again y/n: ")
        else:
            exit
       
rps(a)