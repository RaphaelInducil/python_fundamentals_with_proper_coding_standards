# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 3, Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# create a list for num

numbers = []

# user input 10 num

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# limit duplicate using numbers.count == 1, print unique numbers

unique_numbers = [num for num in numbers if numbers.count(num) == 1]
print("Unique numbers:", unique_numbers)

# end