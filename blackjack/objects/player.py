from blackjack.objects.hand import Hand

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()
        self.status = 'PLAYING'

    def deal_card(self, cards):
        """
        Add cards to player's hand
        :param cards: list of cards to add
        :return: None
        """
        self.hand.add_card(cards)

    def get_play(self, min_to_beat = None):
        """
        Determine what play the player wants to do. If min_to_beat is None, tactic is
        'STOP' if hand >= 17, otherwise 'DRAW' if hand value is < 17
        :type min_to_beat: if player tactic is to get more than min_to_beat (dealer with sam)
        :return: {STOP, DRAW}
        """
        hand_value = self.hand.evaluate()
        if hand_value > 21:
            return 'LOSS'
        elif min_to_beat is not None and hand_value < min_to_beat:
            return 'DRAW'
        elif hand_value >= 17:
            return 'STOP'
        else:
            return 'DRAW'

    def get_hand_value(self):
        return self.hand.evaluate()
