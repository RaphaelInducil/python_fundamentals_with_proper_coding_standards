# Inducil, Raphael CLouiee A.
# 3-13-06
# batch 1, Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

# send message instruction to user
# print all the even numbers starting from 0 to 100
# use for loop

print("9. All the even numbers starting from 0 to 100 are: ")
for num in range(101):
    if num % 2 == 0:
        print(num, end=" ")

# end