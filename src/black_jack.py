from deck import Deck
from player import Player
import time

class Blackjack():
    def __init__(self, deck, player, dealer, gamepoints=2000, playerpoints=None, dealerpoints=None, penalty=250) -> None:
        if not playerpoints:
            playerpoints = gamepoints
        if not dealerpoints:
            dealerpoints = gamepoints
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.gamepoints = gamepoints
        self.penalty = penalty
        self.player.points = playerpoints
        self.dealer.points = dealerpoints
        self.initial_bet = penalty
        
        self.deck.shuffle_deck()
    
    def player_lost(self) -> bool:
        if self.player.calculate_hand() > 21:
            return True
        return False
    
    def dealer_lost(self) -> bool:
        if self.dealer.calculate_hand() > 21:
            return True
        return False
    
    def player_pick_card(self) -> None:
        self.player.pick_card(self.deck)
        
    def dealer_pick_one_card(self):
        self.dealer.pick_card(self.deck)
        
    def dealer_pick_card(self) -> None:
        self.dealer.pick_various_cards(self.deck)
        
    def gain_points_player(self) -> None:
        self.player.gain_points(self.penalty)
        
    def gain_points_dealer(self) -> None:
        self.dealer.gain_points(self.penalty)
        
    def lose_points_player(self) -> None:
        self.player.lose_points(self.penalty)
        
    def lose_points_dealer(self) -> None:
        self.dealer.lose_points(self.penalty)
        
    def change_bet(self, bet) -> None:
        
        if bet < self.penalty:
            print("Cannot change bet to a value lower than the initial bet")
        else:
            self.penalty = bet
            print(f"bet changed to {bet}")
    
    def _reset_bet_and_game_turn(self):
        self.penalty = self.initial_bet
        self.deck.renitialize_deck()
        self.deck.shuffle_deck()
        self.player._hand = []
        self.player_pick_card()
        time.sleep(0.4)
        self.player_pick_card()
        self.dealer._hand = []
        print("\n")
        self.dealer_pick_one_card()
        time.sleep(0.4)
        self.dealer_pick_one_card()
        print("The hands were reseted and the current bet reseted to the initial bet")
        print("\n\n\n")
        print(self.player)
        print("\n\n\n")
        print(self.dealer)