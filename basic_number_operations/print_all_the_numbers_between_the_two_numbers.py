# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 2, Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask user to input 2 numbers

num1 = int(input("Choose a number: "))
num2 = int(input("Enter the second number: "))

# for range num1 to num2, print num1 + 1 until num2

for num in range(num1 + 1, num2):
    print(num)

# end