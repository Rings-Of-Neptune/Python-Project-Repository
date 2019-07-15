# Program introduction
print("""
Welcome to the Registration Form!
""")

# Declare variables, calculate new variables
firstname = str(input("First name? "))
lastname = str(input("Last name? "))
birthyear = int(input("Birth year? "))
tempPassword = str(firstname + "*" + str(birthyear))

# Output results
print("Welcome " + firstname + " " + lastname + "!")
print("Your registration is complete.")
print("Your temporary password is: " + tempPassword)
