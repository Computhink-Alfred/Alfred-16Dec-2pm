riddleAns = "Black"
userAns = input("What is the opposite of white? ")
counter = 1

while userAns != riddleAns:
    if counter == 5:
        print("Hint: The answer starts with a capital B")
    if counter == 10:
        print("Hint: The answer is a colour")
    if counter == 15:
        print("Hint: The answer is Bl_ck")
    userAns = input("What is the opposite of white? ")
    counter = counter + 1

print("Yes! You are right! You took " + str(counter) + " attempts.")