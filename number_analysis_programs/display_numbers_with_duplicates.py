# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 4, Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# initialize list for numbers

numbers = []

# for i in range, input 10 numbers
# append numbers to list

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# create duplicate as new value

duplicates = set()

# if num > 1 count the numbers, add to duplicate
# print duplicate list
# end