import json


# Hollik, Homework 13.1

class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds

    def save_data(self):
        with open("data.txt", "w") as score_file:
            score_file.write(json.dumps(self.__dict__))


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


choice = input("Please type (A) to create an Football player and (B) to create an Baskteball Player").lower()

if choice == "a":
    football_player = FootballPlayer(first_name=input("Name:"),
                                     last_name=("Last Name:"),
                                     height_cm=input("Height:"),
                                     goals=input("Goals:"),
                                     red_cards=input("Red Cards:"),
                                     weight_kg=input("WeightKG:"),
                                     yellow_cards=input("Yellow Cards:")
                                     )
    football_player.save_data()
elif choice == "b":
    basketball_player = BasketballPlayer(first_name=input("Name:"),
                                         last_name=("Last Name:"),
                                         height_cm=input("Height:"),
                                         points=input("Points:"),
                                         rebounds=input("Rebounds:"),
                                         weight_kg=input("WeightKG:"),
                                         assists=input("Assists:")
                                         )
    basketball_player.save_data()
