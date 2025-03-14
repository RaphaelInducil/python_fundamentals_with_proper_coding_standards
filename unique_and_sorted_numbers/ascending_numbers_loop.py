# Inducil, Raphael CLouiee A.
# 3-14-25
# batch 3, Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# initialize list holder

numbers = []

# while loop, ask user input
# append input value to list holder

while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)

# sort list holder
# print sorted list holder

        numbers.sort()
        print("Numbers from lowest to highest:", numbers)

# error handling for invalid input

    except ValueError:
            print("Invalid input. Exiting program.")
            break

# end