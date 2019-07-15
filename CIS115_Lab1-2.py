# Program introduction
print("""
Paycheck Calculator
""")

# eclare variables, calculate new values
hoursWorked = float(input("Hours worked? "))
hourlyPayRate = float(input("Hourly rate? "))
grossPay = round(hoursWorked * hourlyPayRate, 2)
taxRate = 0.18
taxAmount = grossPay * taxRate
takehomePay = round(grossPay - taxAmount, 2)

# Output results
print("Your take-home pay is: $" + str(takehomePay))
