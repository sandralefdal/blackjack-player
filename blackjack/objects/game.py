from blackjack.objects.deck import Deck
from blackjack.objects.player import Player


class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

        #Index of players to get access of players by name
        self.players_index = {}
        for i in range(len(players)):
            self.players_index[players[i].name] = i

        self.next_player_index = 0

    def initialise(self):
        """
        Initialise game by dealing two cards to each player.
        Cards are dealt in the order of the list of players
        :return: state of the game {IN_PLAY, LOSS}
        """
        for iteration in range(2):
            for player in self.players:
                if self.deck.has_cards():
                    card = self.deck.get_card()
                    player.deal_card(card)
                else:
                    return self.evaluate(game_is_done=True)

        return self.update_next_player_index()

    def play_card(self):
        """
        Play a card to next player who's turn it is to receive a card
        After the card is dealt it is checked if the game is done
        There are three ways the game can be done:
            - There are no more cards in the deck
            - One player has lost
            - There are no more players who wants more cards
        :return:
        """
        new_card = self.deck.get_card()
        player_to_deal = self.players[self.next_player_index]

        player_to_deal.deal_card(new_card)
        score_to_beat = self.get_score_to_beat(player_to_deal)
        play = player_to_deal.get_play(score_to_beat)

        if play == 'LOSS' or not self.deck.has_cards():
            return self.evaluate(game_is_done=True)
        elif play == 'STOP':
            # Next player in line to get dealt a card is updated
            return self.update_next_player_index()
        else:
            return "IN_PROGRESS"

    def get_score_to_beat(self, player):
        """
        Dealer's tactic is to always draw if sam has better score than dealer
        :param player: player to return tactic for.
        :return: None if sam, sam's score if dealer
        """
        score_to_beat = None
        if player.name == 'dealer':
            score_to_beat = self.players[self.players_index['sam']].get_hand_value()
        return score_to_beat

    def update_next_player_index(self):
        """
        Determine next player to deal card to
        Game is considered done if there are no more players who wants to draw more cards
        :return: state of game
        """
        while self.next_player_index < len(self.players):
            player = self.players[self.next_player_index]
            score_to_beat = self.get_score_to_beat(player)

            if player.get_play(score_to_beat) == 'DRAW':
                return "IN_PROGRESS"
            self.next_player_index += 1
        return self.evaluate(game_is_done=True)

    def evaluate(self, game_is_done = False):
        """
        Evaluate hands. Winner is announced if either;
        at least one player has lost, or game_is_done = True
        :return: state of the game
        """
        blackjacks = []
        losers = []
        for player in self.players:
            if player.get_hand_value() == 21:
                blackjacks += [player]
            elif player.get_hand_value() > 21:
                losers += [player]

        sam = self.players[self.players_index['sam']]
        dealer = self.players[self.players_index['dealer']]

        if len(blackjacks) == 2:
            self.print_final_state(sam, dealer)
            return "DONE"
        elif len(blackjacks) == 1:
            winner = blackjacks[0]
            loser = [p for p in self.players if p.name != winner.name][0]
            self.print_final_state(winner, loser)
            return "DONE"
        elif len(losers) == 2:
            self.print_final_state(dealer, sam)
            return "DONE"
        elif len(losers) == 1:
            winner = [p for p in self.players if p.name not in losers[0].name][0]
            loser = losers[0]
            self.print_final_state(winner, loser)
            return "DONE"
        elif game_is_done:
            # We already know that neither player has a card value of >= 21
            winner = []
            max_score = 0
            for player in self.players:
                score = player.get_hand_value()
                if score > max_score:
                    max_score = score
                    winner = [player]
                elif score == max_score:
                    winner += [player]

            if len(winner) == 2:
                print("It's a tie!")
                print('sam: %s' % str(self.players[self.players_index['sam']].hand))
                print('dealer: %s' % str(self.players[self.players_index['dealer']].hand))
            else:
                winner = winner[0]
                loser = [p for p in self.players if p.name != winner.name][0]
                self.print_final_state(winner, loser)

            return "DONE"
        else:
            return "IN_PROGRESS"

    def print_final_state(self, winner, loser):
        """
        print to std out final state of game
        :param winner: player object of winner of the game
        :param loser: player object of loser of the game
        :return: None
        """
        print(winner.name)
        print('%s: %s' % (winner.name, str(winner.hand)))
        print('%s: %s' % (loser.name, str(loser.hand)))






