from deck import Deck
from player import Player

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
        self._reset_bet_each_turn
        
    def lose_points_dealer(self) -> None:
        self.dealer.lose_points(self.penalty)
        self._reset_bet_each_turn
        
    def change_bet(self, bet) -> None:
        if bet < self.penalty:
            return "Cannot change bet to lower value"
        self.penalty = bet
        return f"bet changed to {bet}"
    
    def _reset_bet_and_game_turn(self):
        self.penalty = self.initial_bet
        self.deck.renitialize_deck()
        self.deck.shuffle_deck()