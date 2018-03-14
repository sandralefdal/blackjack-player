from blackjack.objects.card import Card
from blackjack.utilities.create_deck import get_random_deck

class Deck:
    def __init__(self):
        """
        Deck consists of a list of cards
        """
        self.deck = []
        self.VALID_SUITS = ['C', 'D', 'H', 'S']
        self.VALID_RANKS = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def read_from_file(self, filename):
        """
        Read deck from file
        :param filename: path and name of file
        :return: None
        """
        try:
            f = open(filename, 'r')
            deck = f.readline().split(",")
            for card in deck:
                if len(card) != 0:
                    suit = card[0]
                    rank = card[1:]
                    if suit in self.VALID_SUITS and rank in self.VALID_RANKS:
                        self.deck += [Card(card)]
                    else:
                        print('Deck contains invalid cards. Exiting game.')
                        return 0
            f.close()
            return 1
        except FileNotFoundError:
            print("Invalid file path given. Exiting game.")
            return 0
        except ValueError:
            print('Deck contains invalid cards. Exiting game.')
            return 0

    def create_random_deck(self):
        random_deck = get_random_deck()
        for card in random_deck:
            self.deck += [Card(card)]
        return 1

    def has_cards(self):
        return len(self.deck) > 0

    def get_card(self):
        """
        Return next card in deck and remove from deck
        :return: Card object
        """
        if len(self.deck) > 0:
            card = self.deck[0]
            self.deck = self.deck[1:]
            return card
        else:
            return None
