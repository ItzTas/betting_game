from deck import Deck

class Blackjack():
    def __init__(self, deck, player, dealer, gamepoints=2000, penalty=500) -> None:
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.gamepoints = gamepoints
        self.penalty = penalty
        
        self.deck.shuffle_deck()