#Reverse Number
# number = int(input("Enter the Number: "))
# while number>0:
#     reverse = number%10 #--> 120%10 == 0 -> reverse   123%10 ==3 -> revese
#     number = number//10 #-> returns the value in interger format 120 -> 12  123 ->12 
#     print(reverse,end='')#-> Prints the reverse variable number

#Pallindrome NUmber
'''The numbers which in reverse format are same as orignal number such type
of number is called Pallindrome Number'''
# number = int(input("Enter the Number: "))
# saved_number = number
# temp = 0
# while number>0:
#     reverse = number%10
#     number = number//10
#     temp = (temp*10)+reverse
# if temp == saved_number:
#     print("The given Number is Pallindrome")
# else:
#     print("The given Number is Not Pallindrome")

#Amstrong Number
'''Sum of cube of every digit of number is equal to orignal Number such type of number is called 
Armstrong Number'''

number = int(input("ENter the Number: "))
saved_number = number
temp = 0
while number>0:
    reverse = number%10
    number = number//10
    temp = temp+(reverse**3)

if temp == saved_number:
    print("The given Number is Armstrong NUmber")
else:
    print("The given Number is Not Armstrong Number")
    