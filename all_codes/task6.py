

menu = input('''
    Menu:
    1)  Add Student
    2)  Update Student Details
    3)  Remove Student
    4)  Search Student
    5)  Dispaly All Student
    6)  Dispaly Highest Percentage Wise Student List
    7)  Display Lowest Percentafe Wise Student List
    8)  Display Highest Student Name
    9)  Display Lowest Student Name
    10) Add Fees

    ''')

dict_student_detail = dict()
temp = 1
dict1 = dict()
while True:
    if menu.isdigit():
        menu = int(menu)
        break
    else:
        menu = input('''
            Menu:
            1)  Add Student
            2)  Update Student Details
            3)  Remove Student
            4)  Search Student
            5)  Dispaly All Student
            6)  Dispaly Highest Percentage Wise Student List
            7)  Display Lowest Percentafe Wise Student List
            8)  Display Highest Student Name
            9)  Display Lowest Student Name
            10) Add Fees
            Enter in number format only: 
            ''') 
if menu == 1:
    name = input('Enter your name: ')
    while True:
        if name.isalpha():
            break
        else:
            name = input("Enter your name: ")
    dict_student_detail['Name'] = name
    no = input('Enter your Phone Number: ')
    while True:
        if no.isdigit():
            no = int(no)
            break
        else:
            no = input("Enter your number only: ")
    dict_student_detail['Phone Number'] = no
    marks = []
    for i in range(1,6):
        mark = input(f"Enter marks {i}: ")
        marks.append(mark)
    dict_student_detail['Marks'] = marks
    dict1[temp] = dict_student_detail
    temp += 1
print(dict1)
    
