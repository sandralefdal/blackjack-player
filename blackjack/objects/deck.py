from blackjack.objects.card import Card
from blackjack.utilities.create_deck import get_random_deck

class Deck:
    def __init__(self):
        """
        Deck consists of a list of cards
        """
        self.deck = []

    def read_from_file(self, filename):
        """
        Read deck from file
        :param filename: path and name of file
        :return: 1 if deck was succeccfully created, 0 if not
        """
        try:
            f = open(filename, 'r')
            deck = f.readline().split(",")
            for card in deck:
                card = card.strip()
                if len(card) != 0:
                    try:
                        c = Card(card)
                    except ValueError:
                        print('Deck contains invalid cards. Exiting game.')
                        return 0
                    self.deck += [c]

            f.close()
            return 1
        except FileNotFoundError:
            print("Invalid file path given. Exiting game.")
            return 0
        except ValueError:
            print('Deck contains invalid cards. Exiting game.')
            return 0

    def create_random_deck(self):
        """
        Creates a full stack of cards "randomly" shuffled.
        :return: 1 if deck was succesfully created, 0 if not
        """
        try:
            random_deck = get_random_deck()
            for card in random_deck:
                self.deck += [Card(card)]
            return 1
        except:
            return 0

    def has_cards(self):
        """
        :return: True if there are cards left in the deck, False otherwise
        """
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
