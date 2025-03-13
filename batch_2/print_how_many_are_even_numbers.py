# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 2, # Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

# user input 10 numbers

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    
# check if the number is even
# count the even numbers

    if num % 2 == 0:
        count += 1

# print the count of even numbers
# end
