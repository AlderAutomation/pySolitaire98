import random
import card

numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['hearts', 'diamonds', 'clubs', 'spades']

class Deck:
    def __init__(self) -> None:
        self.card_deck = []
        for suit in suits:
            for number in numbers: 
                self.card_deck.append(card.Card(number, suit))


    def shuffle(self) -> None:
        random.shuffle(self.card_deck)

    
    def deal (self, index=0) -> object:
        return self.card_deck.pop(index)

    
    def display(self) -> None:
        for card in self.card_deck:
            print(f'{card.number} {card.suit}')


    def reset_deck(self):
        self.__init__()