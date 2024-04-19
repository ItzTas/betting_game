from black_jack import Blackjack

class Blackjackgame():
    def __init__(self) -> None:
        self.blackjack = None
         
    def start_game(Self) -> None:
        diferent_points = input("Do you want to have diferent points than the dealer? no/yes").lower()
        if diferent_points == "yes":
            player_points = int(input("How many points do you wish to have?"))
            if player_points <= 0 or not player_points:
                print("Invalid answer")
        