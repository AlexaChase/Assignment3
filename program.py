print("Welcome, please choose the size of the pizza: ")
pizzasize= input("large or extra-large: ")
if pizzasize== "small":
    print("Error, this size is not available")
if pizzasize== "medium":
    print("Error, this size is not available")
if pizzasize=="large":
    pizzabill =+ 6
if pizzasize=="extra-large":
    pizzabill=+ 10
topping1=input("Would you like a topping Y or N: ")
if topping1 == "N":
    subtotal= pizzabill
    print("Subtotal: $",subtotal)
    tax= pizzabill * 0.13
    print("Tax: $", tax)
    finalcost= pizzabill * 1.13
    print("Final Cost: $", finalcost)
if topping1== "Y":
    toppingsbill1= 1
    print(input("Please select a topping: "))
    topping2=input("Would you like a second topping Y or N: ")
    if topping2== "N":
        subtotal= pizzabill + toppingsbill1
        print("Subtotal: $",subtotal)
        tax= (pizzabill + toppingsbill1) * 0.13
        print("Tax: $", tax)
        finalcost= (pizzabill + toppingsbill1) * 1.13
        print("Final Cost: $", finalcost)
    if topping2== "Y":
        toppingsbill2= 1.75
        print(input("Please select a topping: "))
        topping3=input("Would you like a third topping Y or N: ")
        if topping3== "N":
            subtotal= pizzabill + toppingsbill1 + toppingsbill2
            print("Subtotal: $",subtotal)
            tax= (pizzabill + toppingsbill1 + toppingsbill2) * 0.13
            print("Tax: $", tax)
            finalcost= (pizzabill + toppingsbill1 + toppingsbill2) * 1.13
            print("Final Cost: $", finalcost)
        if topping3== "Y":
            toppingsbill3= 2.50
            print(input("Please select a topping: "))
            topping4=input("Would you like a third topping Y or N: ")
            if topping4== "N":
                subtotal= pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3
                print("Subtotal: $",subtotal)
                tax= (pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3) * 0.13
                print("Tax: $", tax)
                finalcost= (pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3) * 1.13
                print("Final Cost: $", finalcost)
            if topping4== "Y":
                toppingsbill4=+ 3.35
                print(input("Please select a topping: "))
                subtotal= pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3 + toppingsbill4
                print("Subtotal: $",subtotal)
                tax= (pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3 + toppingsbill4) * 0.13
                print("Tax: $", tax)
                finalcost= (pizzabill + toppingsbill1 + toppingsbill2 + toppingsbill3 + toppingsbill4) * 1.13
