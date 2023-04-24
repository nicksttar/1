import random
import time


class Deck:
    """Class to create and manage deck of cards"""

    def __init__(self) -> None:
        self.masty = [chr(i) for i in range(9829, 9833)]

    def get_deck(self) -> list:
        """Creates deck to each round"""
        c = ["V", "Q", "K", "T"]
        val_deck = [j+i for i in self.masty for j in c]
        num_deck = [str(j)+i for i in self.masty for j in range(2,11)]
        full_deck = num_deck+val_deck
        return full_deck

    def get_card(self, deck: list) -> str:
        """Returns random card and remove it from deck till end game"""
        card = random.choice(deck)
        deck.remove(card)
        return card

    def get_cards_dict(self) -> dict:
        """Dictionary with value of each card"""
        deck = self.get_deck()
        cards_dict = {}
        for card in deck:
            if card[0:-1].isdigit():
                cards_dict[card] = int(card[0:-1])
            elif card[0:-1].isalpha() is True:
                cards_dict[card] = int({"V": 10, "Q": 10, "K": 10, "T": 11}[card[0:-1]])
        return cards_dict

    def get_card_value(self, rank: str) -> int:
        """Returns the value of a given card"""
        cards_dict = self.get_cards_dict()
        return cards_dict[rank]



class Game:
    """Class to manage game settings"""

    def get_user(self) -> None:
        """Displays game rules"""
        time.sleep(1)
        print("""
        Rules of the Black Jack:
        Before the game you place a bet and the game starts. There is a deck of cards with values ​​from 2 to 21. 
        At the beginning of each round you have two cards your task is to make the number of points more than your opponent, 
        but not more than 21 otherwise there will be a bust. You can take 1 card or leave your points as they are. 
        The opponent draws an additional card until he has 18 points or more. At the end of the game, 
        if you have 21 or less points but more than your opponent, you get a win depending on your bet.
        """)

    def introduction(self) -> None:
        """Displays game introduction"""
        print("""----------------------------
Black Jack by nicksttar v2.0
----------------------------""")
