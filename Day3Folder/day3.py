# Write all your codes for Day 3 here.
# REMEMBER to change main.py to import this file.
# You can COMMENT out the previous task before going on to the next task
# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# print(int(num1) + int(num2))

# name = input("What is your name? ")
# num_pen = input("How many pens did you buy? ")

# print(name + " bought " + num_pen + " pens.")

# num1 = int(input("What is the first number to add? "))
# num2 = int(input("What is the second number to add? "))

# print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
# print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
# print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
# print(str(num1) + " x " + str(num2) + " = " + str(num1 * num2))

# age1 = int(input("How old is personA? "))
# age2 = int(input("How old is personB? "))

# if age1 > age2:
#     print("PersonA is older than PersonB.")
#     print("This is the seond line")
# else:
#     print("PersonA is NOT older than PersonB")

# password = "abcdefg"
# userPass = "nil"
# tries = 0

# for i in range(3):
#     if userPass != password:
#         userPass = input("What is the password? ")
#         if tries < 3:
#             if userPass == password:
#                 print("You have logged in")
#             else:
#                 print("Wrong! Try again.")
#                 tries = tries + 1

# if tries >= 3:
#     print("System has locked out.")

# import random

# ranNum = random.randint(1, 3)

# userGuess = int(input("What do you think the number is? "))

# if userGuess == ranNum:
#     print("Good job! You are right")
# else:
#     print("You didn't guess correctly. The number was " + str(ranNum) + ".")

import random

num1 = random.randint(51, 100)
num2 = random.randint(51, 100)
ans = num1 + num2

userAns = int(input("What is " + str(num1) + " + " + str(num2) + "? "))

if userAns == ans:
    print("You are correct!")
else:
    print("womp womp")