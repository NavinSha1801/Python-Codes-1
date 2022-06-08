from os import stat


lst = []
stat0 = True
while stat0:
    stat1 = True
    item = input("Enter your products: ")
    lst.append(item)
    while stat1:
        choice = input("Do u Want to add some more items type \'y\' to add or \'n\' to exit: " ).lower()
        if choice  == 'y' or choice == 'yes':
            stat1 = False
        elif choice == 'n' or choice =='no':
            print(lst)
            stat0,stat1 = False,False
        else:
            print("Invalid Input")
            choice = input("Do u Want to add some more items type \'y\' to add or \'n\' to exit: " ).lower()
