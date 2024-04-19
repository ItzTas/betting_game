from deck import Deck

class Player():
    def __init__(self, points) -> None:
        self._hand = []
        self.points = points
        
    def pick_card(self, deck) -> None:
        self._hand.append(deck.pick_card())
    
    def lose_points(self, penalty) -> None:
        self.points -= penalty
    
    def calculate_hand(self) -> int:
        pass