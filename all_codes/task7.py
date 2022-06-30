class menu:
    def menu_printing(self):
        oder = input('''
                Welcome to Amazing Pizza and Pasta Pizzeria
            Press 1: oder menu
            Press 2: Exit
            Enter your choice: ''')
        while True:
            if oder.isdigit():
                oder = int(oder)
                break
            else:
                oder = input('''
                Welcome to Amazing Pizza and Pasta Pizzeria
            Press 1: oder menu
            Press 2: Exit
            Enter your choice again: ''')
        if oder == 2:
            exit()
        print('''
        1 Large Pizza = 10.99 AUD
        2 Large Pizzas = 20.99 AUD
        3 Large Pizzas = 29.99 AUD
        Offer
        ***Buy 4 or more pizzas and get 1.5lt of soft drink Free***

        1 Large Pasta = 9.5 AUD
        2 Large Pasta = 17.00 AUD
        3 Large Pasta = 27.50 AUD

        Offer
        *** Buy 4 or more pastas and get Bruschetta Free***
        *** Buy 4 or more pizza and pastas and get 2 choco brownies***
        ice cream Free***
        ---------------------------------------------------------------------
        ''')
class costomer_detail(menu):
    total = []
    counter_drink = 0
    counter_brownie = 0
    count_pizza = 0
    count_pastas = 0
    total_pizza = 0
    total_pastas = 0
    counter_bruschetta = 0
    def details(self):
        name = input("Enter your name: ")
        print(f"Welcome {name}")
        no_pizza = input("Enter number of pizzas you want : ")
        while True:
            if no_pizza.isdigit():
                no_pizza = int(no_pizza)
                break
            else:
                no_pizza = input("Enter number of pizzas you want : ")
        costomer_detail.total_pizza = 10.99*no_pizza
        costomer_detail.count_pizza += no_pizza
        print(f"Total Pizza Price: {costomer_detail.total_pizza}")
        if no_pizza >= 4:
            print('*** You get 1.5lt of soft drink Free***')
            costomer_detail.counter_drink += 1
        no_pastas = input("Enter no of pastas you want: ")
        while True:
            if no_pastas.isdigit():
                no_pastas = int(no_pastas)
                break
            else:
                no_pastas = input("Enter number of pastas you want : ")
        costomer_detail.total_pastas = 9.5*no_pastas
        costomer_detail.count_pastas += no_pastas
        print(f"Total Pastas Price: {costomer_detail.total_pastas}")
        if no_pastas >= 4:
            print('*** You get Bruschetta Free***')
            print('*** You get 2 choco brownies***')
            costomer_detail.counter_brownie += 1
            costomer_detail.counter_bruschetta +=1
        print(f"Your total order is: {costomer_detail.total_pastas+costomer_detail.total_pizza}")
        costomer_detail.total.append(costomer_detail.total_pastas+costomer_detail.total_pizza)
        print(f'---> Your Net total amount = {costomer_detail.total}')
        
obj = costomer_detail()
obj.menu_printing()
while True:
    obj.details()
    again = input("Do you want to add more coustomer: \'y\' for yes and \'n\' for no").lower()
    if again == 'n':
        print('-----------------------------------------------------')
        print(f'Payment Recieved By Pizza: {costomer_detail.count_pizza*10.99} AUD \n')
        print(f"Payment Recieved By Pastas: {costomer_detail.count_pastas*9.5} AUD \n")
        print(f"Total Payment Recieved: {sum(costomer_detail.total)} AUD\n")
        print(f"Number of 1.5 lt soft drink sold: {costomer_detail.counter_drink}\n")
        print(f"Number of bruschetta given to customer: {costomer_detail.counter_bruschetta}\n")
        print(f"Number of chocco brownies ice cream given to customer: {costomer_detail.counter_brownie}\n")
        print("Bye Bye See you again")
        print('-------------------------------------------------------')
        break
    else:
        continue



