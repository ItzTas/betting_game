from black_jack import Blackjack
from player import Player, Dealer
from deck import Deck
import time
class Blackjackgame():
    def __init__(self) -> None:
        self._blackjack = None
        self.player_points = None
        self.dealer_points = None
        self.game_points = 0
        self.initial_bet = 250
        self.start_game()
        self.set_black_jack()
        self.play()
         
    def start_game(self) -> None:
        while True:
            diferent_points = input("Do you want to have diferent points than the dealer? no/yes ").lower()
            if diferent_points == "yes":
                self.player_points = self.get_valid_points("How many points do you want to have? ")
                self.dealer_points = self.get_valid_points("How many points do you want the dealer to have? ")
                break
            elif diferent_points == "no":
                self.game_points = self.get_valid_points("How many points do you want the game to have? ")
                break
            else:
                print("The answer must be yes or no")
        
        if self.dealer_points is None and self.player_points is None and self.game_points < self.initial_bet:
            self.initial_bet = self.game_points
        elif self.dealer_points and self.player_points and self.dealer_points < self.player_points and self.dealer_points < self.initial_bet:
            self.initial_bet = self.dealer_points
        elif self.dealer_points and self.player_points and self.player_points < self.dealer_points and self.player_points < self.initial_bet:
            self.initial_bet = self.player_points
            
        while True:
            change_initial_bet = input(f"The initial bet is {self.initial_bet} do you want to change it? no/yes ").lower()
            if change_initial_bet == "yes":
                self.initial_bet = self.get_valid_initial_bet("What is your initial bet? ")
            elif change_initial_bet == "no":
                break
            else:
                print("The answer must be yes or no")
                
    def set_black_jack(self):
        self._blackjack = Blackjack(Deck(), Player(0), Dealer(0), self.game_points, self.player_points, self.dealer_points, self.initial_bet)
                
    def get_valid_points(self, prompt):
        while True:
            try:
                points = int(input(prompt))
                if points <= 0:
                    print("The number cannot be lower than/or 0")
                else:
                    return points
            except ValueError:
                print("Must be a number") 
                        
    def get_valid_initial_bet(self, prompt):
        while True:
            try:
                points = int(input(prompt))
                if self.dealer_points is None and self.player_points is None and self.game_points < points:
                    print("The initial bet cannot be lower than the gamepoints")
                elif self.dealer_points and self.player_points and self.dealer_points < self.player_points and self.dealer_points < points:
                    print("The initial bet cannot be lower than the dealer points")
                elif self.dealer_points and self.player_points and self.player_points < self.dealer_points and self.player_points < points:
                    print("The initial bet cannot be lower than your points")
                else:
                    return points
            except ValueError:
                print("It must be a number")
                
    def get_valid_bet(self, prompt):
        pass
            
    def calculate_outcome(self):
        if self._blackjack.player.calculate_hand() == self._blackjack.dealer.calculate_hand():
            return "It is a tie"
        if self._blackjack.player_lost() or self._blackjack.player.calculate_hand() < self._blackjack.dealer.calculate_hand():
            self._blackjack.lose_points_player()
            self._blackjack.gain_points_dealer()
            return f"You lost {self._blackjack.penalty} points! now you have {self._blackjack.player.points} and the dealer has {self._blackjack.dealer.points}"
        elif self._blackjack.dealer_lost() or self._blackjack.player.calculate_hand() > self._blackjack.dealer.calculate_hand():
            self._blackjack.lose_points_dealer()
            self._blackjack.gain_points_player()
            return f"The dealer lost {self._blackjack.penalty} points! now he has {self._blackjack.dealer.points} and you have {self._blackjack.player.points}"
        
    def play(self):
        print("\n\n\n")
        print("---Starting game---")
        print("\n")
        time.sleep(1)
        print("--Picking your cards--")
        print("\n")
        time.sleep(0.7)
        self._blackjack.player_pick_card()
        time.sleep(0.4)
        self._blackjack.player_pick_card()
        time.sleep(0.4)
        print("\n")
        print("--Picking the dealer cards--")
        print("\n")
        time.sleep(0.7)
        self._blackjack.dealer_pick_one_card()
        time.sleep(0.4)
        self._blackjack.dealer_pick_one_card()
        print("\n\n\n")        
        while True:
            time.sleep(0.6)
            play = input("What do you want to do? \nLook at my cards \nLook at the dealer cards \nLook at my points \nLook at the dealer points \nPick a card from the deck \nSkip the turn \nChange the bet \nAllegate victory \n:").lower()
            if self._blackjack.player.points <= 0:
                print("You lost good luck next time")
            if play == "look at my cards":
                print("\n")
                print(self._blackjack.player)
                print("\n")
            if play == "look at the dealer cards":
                print("\n")
                print(self._blackjack.dealer)
                print("\n")
            if play == "look at my points":
                print("\n")
                print(f"You have {self._blackjack.player.points} points")
                print("\n")
            if play == "look at the dealer points":
                print("\n")
                print(f"The dealer has {self._blackjack.dealer.points} points")
                print("\n")
            if play == "pick a card from the deck":
                print("\n")
                self._blackjack.player_pick_card()
                print("\n")
                if self._blackjack.player_lost():
                    print("Your cards have surpassed 21") 
                    print(self.calculate_outcome())
                    print("\n")
            if play == "change the bet":
                try:
                    bet = int(input("Place your new bet"))
                    self._blackjack.change_bet() #improve
                except ValueError:
                    print("\n")
                    print("It must be a number")
                    print("\n")
            if play == "skip the turn":
                print("\n")
                print("It is the dealer turn now")
                print("\n")
                time.sleep(0.7)
                self._blackjack.dealer_pick_card()
                print("\n")
                time.sleep(0.7)
                print("The dealer skips his turn")
                if self._blackjack.dealer_lost():
                    print(self.calculate_outcome())
                    print("\n")
            if play == "allegate victory":
                print(self.calculate_outcome)
            else:
                print("\n")
                print("Please choose a valid answer")
                print("\n")