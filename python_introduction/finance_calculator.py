# User input for financial details
monthly_income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter your total monthly expenses:"))

# Calculate Monthly savings
monthly_savings = monthly_income - total_monthly_expenses

# Project Annual Savings at annual interest rate of 5%
annual_savings = monthly_savings * 12 
annual_rate = annual_savings * 0.05
projected_savings = annual_savings + annual_rate

# Print out the results
print("Projected savings after one year, with interest, is:", projected_savings)
