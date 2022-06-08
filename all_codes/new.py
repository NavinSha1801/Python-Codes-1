from turtle import numinput


def pallindrome(num):
    temp = num
    temp0=0
    while num > 0 :
        r = num%10
        num = (int)(num/10)
        temp0 = (temp0*10)+r
    print(temp0)
    if(temp==temp0):
        print("Given number is pallindrome")
    else:
        print("Given number is not pallindrome")

a = int(input("Enter the number: "))
pallindrome(a)
    
     