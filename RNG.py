########################################################################################################################
########################################################################################################################

from random import randint

#change the range of the number make it easier/harder
number = randint(1, 10)
# change number of tries to make it easier/harder
number_of_tries = 3

# ask for name of the player
user_name = input("Hello, what's your name? \n")
number_of_guesses = 0

########################################################################################################################

#print intro and rules
print(f"Okay {user_name}...I am Guessing a number between 1 and 10:")
print(f"type a number on your keyboard")
print(f"and also remember {user_name}, \nyou have {number_of_tries} tries to guess the number!")


########################################################################################################################

while number_of_guesses < number_of_tries:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
if guess == number:
    print(f"You guessed the number in {number_of_guesses} tries!\ntry one more time")
else:
    print(f"You didnt guess the number {user_name}, too bad. \nThe number was: {number}\ntry one more time")


########################################################################################################################
########################################################################################################################
