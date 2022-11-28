import random
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
difficulty = input("choose a difficulty. type easy or hard: ").lower()
random_number = random.randint(1, 101)
i = 5
j = 10


def guess_func(guess_number, number):
    if guess_number == number:
        print("you made the right guess")
        exit(0)
    elif guess_number > number:
        print("guess too hight")
    else:
        print("guess too low")


def difficulty_func(lives):
    if lives == 0:
        print("you lose")
        exit(0)
    print(f"you have {lives} attempts to guess the number")
    user_guess = int(input("make a guess: "))
    guess_func(user_guess, random_number)
    lives -= 1


while True:
    if difficulty == "easy":
        difficulty_func(j)
        j -= 1
    elif difficulty == "hard":
        difficulty_func(i)
        i -= 1
