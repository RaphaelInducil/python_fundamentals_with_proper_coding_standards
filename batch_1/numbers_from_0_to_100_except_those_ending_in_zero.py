# Inducil, Raphael CLouiee A.
# 3-13-06
# batch 1, Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# send message instruction to user
# for loop, range 101, if remainder is not 0, print output

for num in range(101):
    if num % 10 != 0:
        print(num)

# end