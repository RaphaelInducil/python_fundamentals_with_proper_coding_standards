# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# initialize highest as value

highest = None

# while loop, ask user input
# if num > highest, turn highest into num

while True:
    try:
        num = int(input("Enter a number (or any non-number to stop): "))
        if highest is None or num > highest:
            highest = num

# error handling for invalid input

    except ValueError:
        break

# print highest

if highest is not None:
    print("The highest number is:", highest)
else:
    print("No valid numbers were entered.")

# end