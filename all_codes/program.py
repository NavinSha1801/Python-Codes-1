status0 = True
while status0:
    name = input("Enter Coustomer Name: ")
    while True:
        if name.isalpha():
            break
        else:
            name = input("Enter Coustomer Name: ")
    mobile_no = input("Enter Coustomer Mobile number: ")
    while True:
        if mobile_no.isdigit():
            mobile_no = (int)(mobile_no)
            break
        else:
            mobile_no = input("Enter Coustomer Mobile Number: ")
    age = input("Enter coustomer age: ")
    while True:
        if age.isdigit():
            age = (int)(age)
            break
        else:
            age = input("Enter Coustomer age: ")
    gender = input("Enter Coustomer's gender in m/f: ")
    while True:
        if gender.isalpha():
            break
        else:
            gender = input("Enter Coustomer's gender in m/f: ")
    product_name = input("Enter the product name he/she purchsed: ")
    product_weight = input("Enter the weight of product in grams: ")
    while True:
        if product_weight.isdigit():
            product_weight= (int)(product_weight)
            break
        else:
            product_weight = input("Enter the weight of product in grams only: ")
    gold_price_per_gram = 4670
    making_charges_per_gram = 500
    result = gold_price_per_gram*product_weight
    status = input("Enter your vaccination status y/n: ")
    if status == 'y':
        vaccination = True
    else:
        vaccination = False
    if age >=65:
        if gender == 'm':
            if result <= 200000:
                percent = 20
            elif result >200000 and result <=300000:
                percent = 30
            elif result > 300000:
                percent = 50
        else:
            if result <= 200000:
                percent = 25
            elif result >200000 and result <=300000:
                percent = 35
            elif result > 300000:
                percent = 55
    if age <65:
        if gender == 'm':
            if result <= 200000:
                percent = 15
            elif result >200000 and result <=300000:
                percent = 20
            elif result > 300000:
                percent = 40
        else:
            if result <= 200000:
                percent = 20
            elif result >200000 and result <=300000:
                percent = 30
            elif result > 300000:
                percent = 50

    print(f"\nCoustomer name: \t{name}")
    print(f"Coustomer Age: \t{age}")
    print(f"Coustomer Mobile Number: \t{mobile_no}")
    print(f"Coustomer's Gender: \t{gender}")

    print("\nProduct Description\n")
    print(f"Name of Product: \t{product_name}")
    print(f"Gold Rate in 1 Gram: \t{gold_price_per_gram}")
    print(f"Gold in Gram: \t{product_weight}")
    rate = gold_price_per_gram*product_weight
    print(f"Total Purchase rate:\t {rate}")
    if vaccination == True:
        print(f"You are eligible for discount your net discount percent is : \t{percent}")
    else:
        print("You are not eligible for dicount")
    if vaccination == True:
        minus = (rate*percent)/100
        print(f"Total disamount you gained : \t{minus}")
        disamount = rate-minus
    else:
        disamount = 0
        print(f"Total disamount you gained : \t{disamount}")
    print(f"Making charge: {making_charges_per_gram}")
    total = disamount+(making_charges_per_gram*product_weight)
    gst = (total*3)/100
    print(f"CGST : 1.5% and SGCT: 1.5%")
    print(f"\t\"Net amount : {gst+total}\"")
    cus2 = input("Do you want to Enter another coustomer y/n")
    if cus2 == 'y':
        continue
    else:
        status0 = False