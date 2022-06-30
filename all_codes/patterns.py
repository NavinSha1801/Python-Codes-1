'''
i -> y-axis
j -> x-axis

'''
size = int(input("Enter the size of pattern: "))
for i in range(size+1):
    for j in range(size+1):
        if (i == size//2 or j == size//2) or (i == 0 and j> size//2) or (i==size and j<size//2) or (j==0 and i<size//2) or (j == size and i>size//2) :
            print('* ',end='')
        else:
            print('  ',end='')
    print("")
