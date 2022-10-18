import card 
import deck 
import pygame
import random 
import settings


pygame.init()
screen = pygame.display.set_mode((settings.width1, settings.height1))


# Card Testing #
numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

number = random.choice(numbers)
suit = random.choice(suits)

card = card.Card(number, suit, "back", "front")


def test_number():
    assert card.number == int or str
    assert card.number == 'A' or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 'J' or 'Q' or 'K'


def test_suit():
    assert type(card.suit) == str
    assert card.suit == 'clubs' or 'diamonds' or 'hearts' or 'spades'


def test_flip_card():
    assert card.face == "down"
    card.flip_card()
    assert card.face == "up"
    card.flip_card()
    assert card.face == "down"


def test_rotate_card():
    assert card.rotation == "portrait"
    card.rotate_card()
    assert card.rotation == "landscape"
    card.rotate_card()
    assert card.rotation == "portrait"


# Deck Testing #
deck = deck.Deck()


def suit_counter(suit: str) -> int:
    count = 0 
    for card in deck.card_deck:
        if card.suit == suit: 
            count += 1

    return count 


def test_deck_amounts():
    assert len(deck.card_deck) == 52
    assert suit_counter("hearts") == 13
    assert suit_counter("clubs") == 13
    assert suit_counter("diamonds") == 13
    assert suit_counter("spades") == 13


def test_shuffle():
    deck2 = deck.shuffle()
    assert deck != deck2


def test_deal():
    deal_card = deck.deal()
    assert type(deal_card.suit) == str
    assert deal_card.rotation == "portrait"

    for i in range(55):
        if len(deck.card_deck) <= 0:
            assert deck.deal() == False


def test_disply():
    deck.display()