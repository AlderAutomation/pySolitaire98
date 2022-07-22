import random
import card
import spritesheet
import pygame


numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

class Deck:
    def __init__(self) -> None:
        image = pygame.image.load("./assets/image/cardspritesheet.png").convert_alpha()
        sprite_sheet =  spritesheet.SpriteSheet(image)

        self.card_deck = []
        for suit in suits:
            for number in numbers: 
                self.card_deck.append(card.Card(number, suit, sprite_sheet.get_image(numbers.index(number), suits.index(suit), 71, 96)))


    def shuffle(self) -> None:
        random.shuffle(self.card_deck)

    
    def deal (self, index=0) -> object:
        return self.card_deck.pop(index)

    
    def display(self) -> None:
        for card in self.card_deck:
            print(f'{card.number} {card.suit} \n {card.image}')


    def reset_deck(self):
        self.__init__()