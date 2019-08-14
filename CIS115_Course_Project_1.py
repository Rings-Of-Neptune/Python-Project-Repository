# Guess the Number - Week 4
# Name: Ian Wallace
# Date: 8/8/2019

# Import the random module
import random

# Program introduction
print("""
=========================
Welcome to my Guess the number program!
=========================""")

# Declare variables
mynumber = random.randint(1, 10)

# Query user for input
# If number is too high, alert user. If correct, break loop.
while True:
    # Input validation sequence
    count = 1
    try:
        guess = int(input("Guess a number between 1 and 10.  "))
        if guess < mynumber:
            count += 1
            print("\nToo low.\n")
        elif guess > mynumber:
            count += 1
            print("\nToo high.\n")
        else:
            print("\nYou guessed it in " + str(count) + " attempts!\n")
            break
    except ValueError:
        print("\nNumbers only!\n")
