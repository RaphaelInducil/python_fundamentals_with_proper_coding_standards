# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# initialize numbers

numbers = {}

# while loop, user input
# if num in numbers count the nummbers

while True:
    try:
        num = int(input("Enter a number (or any non-numeric value to stop): "))
        if num in numbers:
            numbers[num] += 1

# else dont count
# value error for invalid input, break

        else:
            numbers[num] = 1
    except ValueError:
        break

# print the number with most duplicate

if numbers:
    most_frequent = max(numbers, key=numbers.get)
    print("The number with the most duplicates is:", most_frequent)
else:
    print("No valid numbers were entered.")

# end