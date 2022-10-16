import random
import card
import spritesheet
import pygame
import settings
import my_logger

my_log = my_logger.Default().my_logger

numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

class Deck:
    def __init__(self) -> None:
        my_log.debug('Building Deck')
        self.is_out_of_cards = False
        image = pygame.image.load("./assets/image/spritesheet.png").convert_alpha()
        sprite_sheet =  spritesheet.SpriteSheet(image)

        backside = sprite_sheet.get_image(settings.black_rose, 4, 71, 96, settings.scale)

        self.card_deck = []
        for suit in suits:
            for number in numbers: 
                self.card_deck.append(card.Card(number, suit, sprite_sheet.get_image(numbers.index(number), suits.index(suit), 71, 96, 1.5), backside))


    def shuffle(self) -> None:
        my_log.debug('Shuffling deck')
        random.shuffle(self.card_deck)

    
    def deal (self, index=0) -> object:
        if len(self.card_deck) == 0:
            return False
        else:
            my_log.debug(f'Dealing {self.card_deck[index].number} of {self.card_deck[index].suit}')
            return self.card_deck.pop(index)

    
    def display(self) -> None:
        for card in self.card_deck:
            print(f'{card.number} {card.suit} \n {card.image}')


    def reset_deck(self):
        my_log.debug('Resetting Deck')
        self.__init__()


    def rebuild_from_discard(self, card:object) -> None:
        my_log.debug('Rebuilding deck from waste pile')
        card.face = "down"
        card.is_covered = True
        self.card_deck.append(card)