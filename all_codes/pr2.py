def revers(x):
    y = x.split()
    y.reverse() 
    return " ".join(y)
a = input("Enter an String: ")
print(revers(a))