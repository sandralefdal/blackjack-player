class Card:
    def __init__(self, suit_rank):
        self.suit = suit_rank[0]
        self.rank = suit_rank[1:]

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