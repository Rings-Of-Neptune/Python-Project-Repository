change = int(input())

if change == 0:
    print("No change")
    
if change // 100 >= 1:
    dollars = change // 100
    change = change - (dollars * 100)
    if dollars >= 2:
        print(dollars, "Dollars")
    else:
        print(dollars, "Dollar")
    
if change // 25 >= 1:
    quarters = change // 25
    change = change - (quarters * 25)
    if quarters >= 2:
        print(quarters, "Quarters")
    else:
        print(quarters, "Quarter")

if change // 10 >= 1:
    dimes = change // 10
    change = change - (dimes * 10)
    if dimes >= 2:
        print(dimes, "Dimes")
    else:
        print(dimes, "Dime")
    
if change // 5 >= 1:
    nickels = change // 5
    change = change - (nickels * 5)
    if nickels >= 2:
        print(nickels, "Nickels")
    else:
        print(nickels, "Nickel")

if 1 <= change < 5:
    pennies = change
    if pennies >= 2:
        print(pennies, "Pennies")
    else:
        print(pennies, "Penny")
