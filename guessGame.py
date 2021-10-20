# guess game given 3 tries.

secretNumber = 5
chances = 0
while chances < 3:
    chances += 1
    user_Input = int(input("Guess the number : "))
    if user_Input == secretNumber:
        print("You win!")
        break
    else:
        print("Wrong guess!")

else:
    print("sorry game over!")
