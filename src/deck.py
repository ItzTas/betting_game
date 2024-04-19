import random

class Deck():
    def __init__(self) -> None:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self._cards = [(suit, rank) for suit in suits for rank in ranks]
        
    def shuffle_deck(self) -> None:
        random.shuffle(self._cards)
        
    def pick_card(self) -> None:
        card = self._cards.pop()
        return card
    
    def renitialize_deck(self) -> None:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self._cards = [(suit, rank) for suit in suits for rank in ranks]