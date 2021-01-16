import random
import time

print("""

**Number Guessing Game**

How to play?

* Guess the number between 1 and 100.
* You have 5 guesses.

* Lets Begin!

Note!

* This idea is not mine
* I just developed it to test myself.
* by Bora Erdem :)

""")

random_number = random.randint(1,100)
right_to_guess = 5

while True:
    guess = int(input("Your Guess:"))

    if guess > 100:
        print("Guess cannot be greater than numbers.")
        break

    else: pass

    if guess < random_number:
        print("Wait 2 second")
        time.sleep(1)
        print("Wait 1 second")
        time.sleep(1)
        print("Say a higher number.")
        right_to_guess -= 1

    elif guess > random_number:
        print("Wait 2 second")
        time.sleep(1)
        print("Wait 1 second")
        time.sleep(1)
        print("Say a lower number.")
        right_to_guess -= 1

    else:
        print("Wait 1 second")
        time.sleep(1)
        print("Congratulations! Number was:",random_number)
        break

    if right_to_guess == 0:
        print("")
        print("**GAME OVER**")
        print("")
        print("> Your Guessing Right is Over.")
        print("> The number was:",random_number)
        print("> Try again please.")
        print("")
        print("**GAME OVER**")
        print("")
        break


