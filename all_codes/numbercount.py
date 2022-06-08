a = '112aaaswe2233444rr'
temp0 = 0
temp = a[0]
for i in a:
    if temp == i:
        temp0 += 1
    else:
        print("({}){}".format(temp0,temp),end="")
        temp0 = 1
        temp = i
print("({}){}".format(temp0,temp),end="")
