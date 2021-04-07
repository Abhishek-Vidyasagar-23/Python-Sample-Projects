import time

# welcome the user
user_name = input("Hello Player enter your name")
print("Hello "+user_name+" Let's play Hangman ")

time.sleep(1)
print("Start Guessing ......")
time.sleep(0.5)

# Guessing word
word = "apple"

guesses = ''

turns = 10

# Create a while loop
while turns > 0:
    failed= 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
        guess = input("Enter character to guess")
        guesses += guess

        if guess not in word:
            turns -= 1

            print("Wrong Guess! Please Try Again")
            print("You have", turns, "left ")
            if turns == 0:
                print("You Lose")


