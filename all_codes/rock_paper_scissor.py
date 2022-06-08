a = int(input("Enter the input between 1->rock, 2->paper, 3->scissor: "))
b = int(input("Enter the input between 1->rock, 2->paper, 3->scissor: "))
if a==1:
    if b==1:
        print("tie")
    elif(b==2): 
        print("2 wins")
    elif(b==3):
        print("1 wins")
    else:
        print("B enter wrong input")
elif a==2:
    if b==1:
        print("1 wins")
    elif(b==2):
        print("Tie")
    elif(b==3):
        print("2 wins")
    else:
        print("2 enter wrong input")
elif a==3:
    if b==1:
        print("2 wins")
    elif(b==2):
        print("1 wins")
    elif(b==3):
        print("Tie")
    else:
        print("2 enter wrong input")
else:
    print("a Enter the wrong input")