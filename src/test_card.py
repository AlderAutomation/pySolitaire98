import card 
import random 
import my_logger
import settings

my_log = my_logger.Default().my_logger

numbers = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
suits = ['clubs', 'diamonds', 'hearts', 'spades']

number = random.choice(numbers)
suit = random.choice(suits)

card = card.Card(number, suit, "back", "front")

my_log.debug(f"{card.number} {card.suit} from test ")


def test_card():
    card == object


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