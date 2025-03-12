# Inducil, Raphael CLouiee A.
# 3-13-06
# batch 1, Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# send message instruction to user
# range(10), / with 2, if remainder is not 0, count it

print("8. Count of Odd Numbers Among Ten Inputs")
total_odd = sum(1 for i in range(10) if int(input(f"Enter number {i + 1}: ")) % 2 != 0)

# print the count of odd numbers
# end