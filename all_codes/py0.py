a = int(input("Enter the number: "))
b = []
for i in range(2,a+1):
    if(a%i)==0:
        b.append(i)
print(b)