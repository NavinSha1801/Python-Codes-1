def fibonnacci(n):
    if(n<=1):
        return n
    return fibonnacci(n-1)+fibonnacci(n-2)
a = int(input("Enter the number: "))
c = []
for i in range(0,a+1):
    c.append(fibonnacci(i))
print(c)
