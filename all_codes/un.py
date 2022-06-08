from re import A


while True:
    op = input("""Press 1 to add
press 2 to sub
press 3 to mul
press 4 to div
press 5 to quit 
Enter The operand: """)
    while True:
        if op.isdigit():
            break
        else:
           op = input("""Press 1 to add
press 2 to sub
press 3 to mul
press 4 to div
press 5 to quit 
Enter The operand again: """) 
    if int(op) == 5:
        print("Exiting the calculator")
        break
    else:
        print("")
    a = input("Enter the number1: ")
    b = input("Enter the number2: ")
    while True:
        if a.isdigit() and b.isdigit():
            a = int(a)
            b = int(b)
            break
        else:
            a = input("Enter the number1 again: ")
            b = input("Enter the number2 again: ")
    if  b==0 and int(op)==4:
        print("B is zero cant divide")
    else:
        if (int(op)==1):
            print(f"{a}+{b} = {a+b}")
        elif(int(op)==2):
            print(f"{a}-{b} = {a-b}")
        elif(int(op)==3):
            print(f"{a}*{b} = {a*b}")
        elif(int(op)==4):
            print(f"{a}/{b} = {a/b}")
        else:
            print("Invalid operand")