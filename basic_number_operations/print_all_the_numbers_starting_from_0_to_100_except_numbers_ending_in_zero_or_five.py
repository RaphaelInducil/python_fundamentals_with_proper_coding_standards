# Inducil, Raphael CLouiee A.
# 3-13-25
# batch 2, Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# while loop 100, print num, add 1 to num
# if remainder is not 0 or 5, print output

num = 1
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1

# end