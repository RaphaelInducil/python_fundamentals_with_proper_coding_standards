# Inducil, Raphael CLouiee A.
# 3-12-25
# batch 2, Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

# user input 2 numbers

num1 = int(input("Choose a number: "))
num2 = int(input("Choose a second number: "))

# compare 2 numbers
# print "not equal" if not same number

if num1 != num2:
    print("Number", num1, "and", num2, "are not equal")
else:
    print(num1, "and", num2, "are equal")

# end
