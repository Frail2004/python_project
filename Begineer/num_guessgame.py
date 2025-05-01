import pyfiglet

ascii_banner = pyfiglet.figlet_format("Guess Game")
print(ascii_banner)

import random

random_num = random.randint(1, 10)
attempt = 0


while True:
    try:
        guess = int(input("enter your  guess :   "))
        attempt +=1

        if guess > random_num:
            print("too high")

        elif guess < random_num:
            print("too low")

        else:
            print(f"you guessed in {attempt} attempt ")
            break

    finally:
        print("yeah good to go")