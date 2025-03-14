# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function

# initialize numbers as list value

numbers = []

# while loop, ask user input
# append num
# error handling

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break

# sort numbers
# print sorted numbers
# end