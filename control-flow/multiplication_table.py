# Prompt user input
number = int(input("Enter number to see its multiplication table:"))

# Generate a multiplication table
for y in range(1, 11):
    print(f"{number}*{y} = {number * y}")
