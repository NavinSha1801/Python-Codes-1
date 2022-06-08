def factorial(n):
    if(n<0):
        print("Factorial Dosen't exist")
    elif(n==0):
        print("Factorial of 0 is 1")
    else:
        if(n==1):
            return 1
        else:
            return n*factorial(n-1)
a = int(input("Enter the Number for facctorial: "))
b = factorial(a)
print(b)