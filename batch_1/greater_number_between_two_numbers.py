# Inducil, Raphael CLouiee A.
# 3-12-25
# batch 1, Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.

# send message instruction to user
# ask user to input first number
# ask user to input second number

print("Greater number between two numbers")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# compare the two numbers
# print the bigger number

if num1 > num2:
    print("The greater number is: ", num1)
elif num1 < num2:
    print("The greater number is: ", num2)
else:
    print("The numbers and are equal")

# end