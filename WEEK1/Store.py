again = True

while(again):
    print("Welcome to Kyle Store")
    print("    ITEM              PRICE")
    print("1. PINAYPAY ======== 12 Pesos")
    print("2. Turon    ======== 10 Pesos")
    print("3. Siomai   ======== 10 Pesos")
    print("4. Ngohiong ======== 15 Pesos\n")

    pinaypay = int(12)
    turon = int(10)
    siomai = int(10)
    ngohiong = int(15)

    order = input("Please choose want you to order. Input number only!: ")
    def switch(order):
        if order == "1":
            total = pinaypay
            return total
        elif order == "2":
            total = turon
            return total
        elif order == "3":
            total = siomai
            return total
        elif order == "4":
            total = ngohiong
            return total
        else:
            print("Invalid Input!")
    if order == "1": 
        print(" Your order is Pinaypay")
    elif order == "2": 
        print("Your order is Turon")
    elif order == "3": 
        print("Your order  is siomai")
    elif order == "4": 
        print("Your order is ngohiong")
    else:
        print("Invalid Order!")
    print("Your total is: ", switch(order), " Pesos")
    again = input("Do you want to order again? Press Y if yes and N if No: ")
    if again == "Y":
        again = True
    else:
        again = False
        print("Come back again! Thank you.")


