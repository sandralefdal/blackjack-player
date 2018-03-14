class Card:

    def __init__(self, suit_rank):
        self.VALID_SUITS = ['C', 'D', 'H', 'S']
        self.VALID_RANKS = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

        if self.is_valid_card(suit_rank):
            self.suit = suit_rank[0]
            self.rank = suit_rank[1:]
        else:
            raise ValueError("Card '%s' is not of valid form" % suit_rank)

    def is_valid_card(self, card):
        suit = card[0]
        rank = card[1:]
        if suit in self.VALID_SUITS and rank in self.VALID_RANKS:
            return True
        else:
            return False

    def __str__(self):
        return self.suit + self.rank

    def get_value(self):
        """
        Returns value of card. Always returns 11 for Ace.
        :return: value of card
        """
        if self.rank == 'A':
            return 11
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        else:
            return int(self.rank)

    def is_ace(self):
        return self.rank == 'A'
