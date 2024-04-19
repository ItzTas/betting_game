from deck import Deck

class Player():
    def __init__(self, points) -> None:
        self._hand = []
        self.points = points
        self._lost_hand = False
        
    def pick_card(self, deck) -> None:
        self._hand.append(deck.pick_card())
    
    def lose_points(self, penalty) -> None:
        self.points -= penalty
        
    def gain_points(self, gain) -> None:
        self.points += gain
    
    def calculate_hand(self) -> int:
        total_score = 0
        first_ace = False
        for card in self._hand:
            rank = card[1]
            if rank.isdigit():
                total_score += int(rank)
            elif rank != "Ace":
                total_score += 10
            else:
                if not first_ace:
                    first_ace = True
                else:
                    total_score += 1
        
        if first_ace and total_score + 11 <= 21:
            total_score += 11
        elif first_ace:
            total_score += 1
        return total_score
    
class Dealer(Player):
    def __init__(self, points) -> None:
        super().__init__(points)
        
    def pick_card(self, deck) -> None:
        while self.calculate_hand() < 17:
            super().pick_card(deck)