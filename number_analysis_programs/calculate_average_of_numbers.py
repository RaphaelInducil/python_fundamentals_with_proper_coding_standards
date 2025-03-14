# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

# initialize numbers list

numbers = []

# while loop,user input
# append numbers
# error handling

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        numbers.append(num)
    except ValueError:
        break

# sum numbers to get average // number for input
# print average
# end