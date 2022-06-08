def duplicates():
    a = [1,2,3,4,9,8,10,13,16,18]
    b = [2,9,8,7,16,18,19,20]
    for i in a:
        if i in b:
            a.remove(i)
    print(a)
duplicates()