# Program introduction
print("""
Change Calculator
""")

# Declare variables
continuePrompt = ""
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# Process input and generate output
while continuePrompt == "y" or continuePrompt == "":
    inputNumber = int(input("Enter number of cents (0-99):\t"))
    while inputNumber >= 25:
        quarters += 1
        inputNumber -= 25
    while inputNumber >= 10:
        dimes += 1
        inputNumber -= 10
    while inputNumber >= 5:
        nickels += 1
        inputNumber -= 5
    if inputNumber < 5:
        pennies += inputNumber
        print("""
Quarters: {}
Dimes: {}
Nickels: {}
Pennies: {}
        """.format(quarters, dimes, nickels, pennies))
        continuePrompt = input("Continue? (y/n):\t")
