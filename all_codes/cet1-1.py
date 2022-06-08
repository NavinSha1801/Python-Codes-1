'''
Aim: Write a python program which will find all such number which are divisible by 7 but are not multiple of 5 between 2000
and 3200 
'''
c= [];
for i in range(2000,3201):
    if(i%7==0):
        if(i%5==0):
            continue
        else:
            c.append(i)
    
print(c)