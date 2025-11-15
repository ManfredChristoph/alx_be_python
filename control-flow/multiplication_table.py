# Prompt user input
number = int(input("Enter number to see its multiplication table:"))

# Generate a multiplication table
x = number
for y in range(1, 11):
    print(f"{x}*{y} = {number * y}")
