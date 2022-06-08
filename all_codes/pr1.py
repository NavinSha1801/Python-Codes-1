def duplicates(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def duplicate(x):
    return list(set(x))

a = [1,2,3,4,5,6,5,4,3,2,1,0]
b = duplicate(a)
c = duplicates(a)
print(f"Function 1 is {b}")
print(f"Function 2 is {c}")