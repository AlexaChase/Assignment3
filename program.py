print("Welcome, please choose the size of the pizza: ")
pizzasize= input("large or extra-large: ")
if pizzasize== "small":
    print("Error, this size is not available")
if pizzasize== "medium":
    print("Error, this size is not available")
if pizzasize=="large":
    bill =+ 6
if pizzasize=="extra-large":
    bill=+ 10
topping1=input("Would you like a topping Y or N: ")
if topping1 == "N":
    subtotal= bill
    print("Subtotal: $",subtotal)
    tax= bill * 0.13
    print("Tax: $", tax)
    finalcost= bill * 1.13
    print("Final Cost: $", finalcost)
if topping1== "Y":
    bill=+ 1
    print(input("Please select a topping: "))
    topping2=input("Would you like a second topping Y or N: ")
    if topping2== "N":
        subtotal= bill
        print("Subtotal: $",subtotal)
        tax= bill * 0.13
        print("Tax: $", tax)
        finalcost= bill * 1.13
        print("Final Cost: $", finalcost)
    if topping2== "Y":
        bill=+ 1.75
        print(input("Please select a topping: "))
        topping3=input("Would you like a third topping Y or N: ")
        if topping3== "N":
            subtotal= bill
            print("Subtotal: $",subtotal)
            tax= bill * 0.13
            print("Tax: $", tax)
            finalcost= bill * 1.13
            print("Final Cost: $", finalcost)
        if topping3== "Y":
            bill=+ 2.50
            print(input("Please select a topping: "))
            topping4=input("Would you like a third topping Y or N: ")
            if topping4== "N":
                subtotal= bill
                print("Subtotal: $",subtotal)
                tax= bill * 0.13
                print("Tax: $", tax)
                finalcost= bill * 1.13
                print("Final Cost: $", finalcost)
            if topping4== "Y":
                bill=+ 3.35
                print(input("Please select a topping: "))
                subtotal= bill
                print("Subtotal: $",subtotal)
                tax= bill * 0.13
                print("Tax: $", tax)
                finalcost= bill * 1.13
