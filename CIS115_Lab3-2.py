# Program introduction
print("""
====================
Shipping Calculator
====================""")

# Declare variables
continuePrompt = ""

# Process input and generate output
while continuePrompt == "y" or continuePrompt == "":
    inputNumber = float(input("\nCost of items ordered: "))
    shippingCost = 0.00
    if inputNumber < 0:
        print("You must enter a positive number. Please try again.")
    elif inputNumber < 30.00:
        shippingCost = 5.95
    elif inputNumber >= 30.00 and inputNumber < 50.00:
        shippingCost = 7.95
    elif inputNumber >= 50.00 and inputNumber < 75.00:
        shippingCost = 9.95
    elif inputNumber >= 75.00:
        shippingCost = 0.00
    totalCost = float(inputNumber) + float(shippingCost)
    print("Shipping cost: %s \nTotal cost: %s" % (shippingCost, totalCost))
    continuePrompt = input("\nContinue? (y/n):\t")
