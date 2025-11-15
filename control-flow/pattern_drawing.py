# Prompt User for Pattern size
size = int(input("Enter the size of the pattern:"))

# Start a row counter
row = 1

# while loop to handle row
while row <= size:

  # for loop to print each column in row
    for col in range(size):
        print("*", end="") # prints star side by side

    print() # moves to next line after each row
    row += 1 # increment row counter
