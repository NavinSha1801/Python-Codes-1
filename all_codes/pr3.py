a = int(input("Enter the number1: "))
b = int(input("ENter the number2: "))
op = input("Enter The operand: ")
if (op=='+'):
    print(a+b)
elif(op=='-'):
    print(a-b)
elif(op=='*'):
    print(a*b)
elif(op=='/'):
    print(a/b)
else:
    print("Invalid operand")