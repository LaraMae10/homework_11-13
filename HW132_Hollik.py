import datetime
import json
import random


# Hollik, Homework 13.2

class Result:
    def __init__(self, score, player_name, date):
        self.score = score
        self.player_name = player_name
        self.date = str(date)


def play_game(player):
    attempts = 0
    current_time = datetime.datetime.now()

    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1
        score_list = get_score_list()

        if guess == secret:
            result = Result(attempts, player, current_time)
            #   result.save_result()
            score_list.append(result.__dict__)
            save_score_list(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


def get_top_scores(score_list):
    return score_list[:3]


def get_score_list():
    with open("score_list.txt", "r") as score_file:
        return json.loads(score_file.read())


def save_score_list(score_list):
    with open("score_list.txt", "w") as score_file:
        score_file.write(score_list)


while True:
    player_name = input("Hello, whats your name?")
    selection = input("Would you like to A) play a new game, B) see the best scores, or C) quit?").lower()
    secret = random.randint(1, 30)

    if selection == "a":
        play_game(player_name)
    elif selection == "b":
        for score_dict in get_top_scores(get_score_list()):
            print(str(score_dict["score"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
