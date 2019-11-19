import json
import random
import datetime

# Hollik, Homework 11.1 and 11.2

player_name = input("Hello, whats your name?")

current_time = datetime.datetime.now()
print(current_time)

secret = random.randint(1, 30)
attempts = 0
wrong_guesses = []

score_data = {"player_name": player_name,
              "attempts": attempts,
              "date": datetime.datetime.now(),
              "secret": secret,
              "unsuccessful_guesses": wrong_guesses}

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

while True:
    guess = int(input("Guess the secret number (between 1 and 30): "))
    attempts += 1

    if guess == secret:
        score_list.append({
            "player_name": player_name,
            "attempts": attempts,
            "date": str(datetime.datetime.now()),
            "secret": secret,
            "unsuccessful_guesses": wrong_guesses
        })

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        wrong_guesses.append(guess)
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        wrong_guesses.append(guess)
        print("Your guess is not correct... try something bigger")
