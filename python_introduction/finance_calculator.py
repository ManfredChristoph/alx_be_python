# User input for financial details
monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your total monthly expenses:"))

# Calculate Monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings at annual interest rate of 5%
projected_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Print out the results
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_savings}")

