import random
a = int(input("Enter the number of opponets: "))
o = []
s = []
for i in range(0,a):
    y = int(input("Enter the Score of opponents: "))
    o.append(y)
w = random.choice(o)
b = o.index(w)
x = o[b]*o[b+1]-o[b-1]
s.append(x)
keep_going = True
while keep_going:
    print("Opponent {} is removed".format(w))
    o.remove(w)
    if(len(o)==1):
        keep_going = False
        break
    w = random.choice(o)
    b = o.index(w)
    x = o[b]*o[b-1]
    s.append(x)
print(sum(s)) 