# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 3, Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# number holder (lowest)

lowest = None

# while loop
# user input

while true:
    num = int(input("Enter a number: "))

# if num < lowest
# turn lowest into num

    if lowest is None or num < lowest:
        lowest = num

# error handling for invalid input
# print lowest
# end