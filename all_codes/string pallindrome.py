from urllib.request import AbstractBasicAuthHandler


a = input("Enter the String: ")
i=0
j=len(a)-1
c=0
while i<j:
    if (a[i]==a[j]):
        c=1
    else:
        c=0
    i=i+1
    j=j-1
if(c==1):
    print("String is pallindrome ")
else:
    print("String is not pallindrome ")