user_1 = int(input("user 1 enter your  number: "))
for x in range(20):
    user_2 = int(input("guess the number of user 1: "))
    if user_2 == user_1:
        print("Good job! you found")
        break
    elif user_2 != user_1:
        print("you coudnt find so you are crazy")