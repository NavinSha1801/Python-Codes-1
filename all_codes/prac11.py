def f_l():
    a = []
    for i in range(1,6):
        i = int(input("Enter the number {}: ".format(i)))
        a.append(i)
    f,*m,l = a
    c = [f,l]
    print(c)
f_l()
