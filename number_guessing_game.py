import random

number = random.randint(1, 10)
tries = 0

name = input("Enter Player name")
name = name.strip()

print(f"Hello! {name}")
print("Would You Like to guess to win ?")
print("1) Yes\n 2) No\n")

option = input("Enter 1 or 2")
option = int(option)

if option == 1:
    print("\n I am thinking a number between 1 and 10.")
    print("You have to guess within three tries")

    guess = input("Guess the number ")
    guess = int(guess)
    tries += 1

    if guess > number:
        print("Guess Lower")
    if guess < number:
        print("Guess Higher")

    while guess != number and tries < 3:
        guess = input("Sorry Guess Again")
        guess = int(guess)
        tries += 1
        print(guess)

    if guess == number:
        print("You Won!")
        print(f"Number of tries:{tries}")
        print(guess)
    else:
        print("Sorry Better Luck Next time")
elif option == 2:
    print("Thank You")
else:
    print("Invalid Option")




