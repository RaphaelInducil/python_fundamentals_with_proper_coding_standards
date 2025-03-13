# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 2, Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all the remaining numbers.

# user input  range 10 numbers
# num1 - sum of num2 to num10

numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# print the result

print("Result:", numbers[0] - sum(numbers[1:]))

# end