from blackjack.objects.card import Card


class Hand:
    def __init__(self):
        """
        Hand object consists of list of cards on hand
        """
        self.cards = []

    def __str__(self):
        return ",".join([str(c) for c in self.cards])

    def add_card(self, card):
        """
        Add card to hand
        :param card: card object to add to hand
        :return: None
        """
        self.cards += [card]

    def evaluate(self):
        """
        Evaluate value of hand.
        If value is >= 21, make aces count as 1 until values <= 21
        :return: best possible card hand/value
        """
        num_aces = 0
        total_value = 0

        for card in self.cards:
            if card.is_ace():
                num_aces += 1

            total_value += card.get_value()

        # Make one ace count as 1 until there are no more aces/total_value is <= 21
        while total_value > 21 and num_aces > 0:
            total_value -= 10
            num_aces -= 1

        return total_value