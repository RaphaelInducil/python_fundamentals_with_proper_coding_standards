# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 3, Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# initialize list for numbers

numbers = []
unique_numbers = []

# user input 10 numbers
# append list numbers

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# if num is not unique, append only the unique numbers

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
# print unique numbers

for num in unique_numbers:
    print(num)

# end
