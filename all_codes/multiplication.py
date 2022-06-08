def multiplication():
    a = input("Enter the number: ")
    b = input("Enter the another number: ")
    if(a=='' or b==''):
        print("Taking default parameters")
        print(1*3)
    else:
        c = int(a)
        d = int(b)
        print(c*d)   
multiplication()