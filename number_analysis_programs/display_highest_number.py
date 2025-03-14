# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# initialize highest as value

highest = None

# while loop, ask user input
# if num > highest, turn highest into num

while True:
        num = int(input("Enter a number (or any non-number to stop): "))
        if highest is None or num > highest:
            highest = num

# error handling for invalid input
# print highest
# end