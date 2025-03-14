# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 3, Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# initialize list for numbers

numbers = []

# while loop, continue until user input is invalid
# input number

while True:
    try:
        num = int(input("Enter a number: "))

# if num is in numbers print duplicates
# else append num to numbers print unique

        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)

# value error for invalid input

    except ValueError:
            print("Invalid input. Exiting program.")
            break

# end
