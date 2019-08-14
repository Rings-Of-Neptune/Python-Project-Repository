# Multiplication Table - Week 4
# Name: Ian Wallace
# Date: 8/8/2019

# Program introduction
print("""
=======================
Multiplication Tables!
=======================""")

# Declare variables, gather input
size = input("What size multiplication table would you like? (2-10):  ")

# Define the multiplication table function


def table(tableSize):
    print("\t\t--- Multiplication Table ({0} - {1}) ---\n")
    for each in range(1, 10):
        print(each)
        for i in range(1, int(tableSize)):
            print(int(each) * int(i))


# If number is too high, alert user. If correct, break loop.
if int(size) >= 2 and int(size) <= 10:
    table(size)
