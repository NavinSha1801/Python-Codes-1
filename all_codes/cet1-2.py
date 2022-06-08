type = input("You want to deposit or widtraw type d/w: ")
c = 1000
print("Hello user your initial amount is {}".format(c))
if type=='d'or type == 'D':
    value = int(input("Enter the amount you want to deposit: "))
    c = c+value
    print("your total balance is {}".format(c))
elif type=='w'or type=='W':
    value = int(input("Enter the amount you want to withdraw: "))
    c = c-value
    print("your total balance is {}".format(c))
else :
    print("you entered wrong information")
print("Please collect your card")
    