# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 1, Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

# send message instruction to user

print("7. Sum of Ten Numbers")

# range(10) ask for input, sum it up

total_sum = sum(int(input(f"Enter number {i + 1}: ")) for i in range(10))
print("The sum of the ten numbers is: ", total_sum)

# display output