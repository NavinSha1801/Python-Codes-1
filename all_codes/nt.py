num = int(input("Enter the size of pattern: "))
# for i in range(num+1):
#     # for k in range(i+1):
#     #     print('*',end='')
#     for j in range(num+1):
#         if j >= num-i:
#             print('*',end='')
#         else:
#             print(" ",end='')
#     print('')
for i in range(num+1):
    for j in range(num+1):
        if i == num or i == 0 or j == 0 or j == num:
            print("* ",end="")
        else:
            print("  ",end='')
    print("")