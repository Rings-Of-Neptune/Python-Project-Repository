# Program introduction
print("""
Grade Checker
""")

# Collect user input into a variable
inputNumber = int(input("Please enter your grade.\t"))

# Process input and generate output
if inputNumber >= 90:
    print("""
You earned an A.
    """)
elif inputNumber >= 80 and inputNumber <= 89:
    print("""
You earned a B.
    """)
elif inputNumber >= 70 and inputNumber <= 79:
    print("""
You earned a C.
    """)
elif inputNumber >= 60 and inputNumber <= 69:
    print("""
You earned a D.
        """)
else:
    print("""
You earned an F.
    """)
