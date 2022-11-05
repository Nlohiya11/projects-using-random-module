import os
import random
print("WELCOME TO THE NUMBER GUESSING GAME\n")
print("Computer has a random number for you to guess")
numbers = []
for i in range(0, 101):
    numbers.append(i)
game_over = True
is_continue = True
while is_continue:
    difficulty_level = input("choose a difficulty level\ne for easy/ m for medium / h for hard : ")
    looses = 0
    if difficulty_level == "e":
        lives = 10
        print("you have 10 lives to guess the correct number")
    elif difficulty_level == "m":
        lives = 7
        print("you have 7 lives")
    elif difficulty_level == "h":
        print("you have 5 lives")
        lives = 5
    else:
        print("wrong input")
    random_no = random.choice(numbers)
    while game_over:
        guess = int(input("You guessed : "))
        if guess == random_no:
            print(f"You guessed the word correctly : {random_no}\n")
            game_over = False
        else:
            looses += 1
            if guess > random_no:
                print(f"Your guess {guess} is too high")
            elif guess < random_no:
                print(f"Your guess {guess} is too low")
            print(f"you lost 1 life.\nNow you have {lives - looses} lives left to guess the correct number...\n")
        if looses == lives:
            game_over = False
            print("You lost all you lives try again")
    if input("Do you want to play it again? y/n : ") == "y":
        game_over = True
        os.system('cls')
    else:
        is_continue = False
