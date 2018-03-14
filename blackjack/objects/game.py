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

        self.game_state = 'IN_PROGRESS'
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
        if self.deck.has_cards():
            new_card = self.deck.get_card()
            player_to_deal = self.players[self.next_player_index]

            player_to_deal.deal_card(new_card)
            score_to_beat = self.get_score_to_beat(player_to_deal)
            play = player_to_deal.get_play(score_to_beat)

            if play == 'LOSS':
                return self.evaluate(game_is_done=True)
            elif play == 'STOP':
                # New player starts getting dealt cards
                return self.update_next_player_index()
            else:
                return "IN_PROGRESS"
        else:
            return self.evaluate(game_is_done=True)

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
                blackjacks += [player.name]
            elif player.get_hand_value() > 21:
                losers += [player.name]

        if len(blackjacks) == 2:
            print('sam')
            print('sam: %s' % str(self.players[self.players_index['sam']].hand))
            print('dealer: %s' % str(self.players[self.players_index['dealer']].hand))
            return "DONE"
        elif len(blackjacks) == 1:
            winner = blackjacks[0]
            losers = [p.name for p in self.players if p.name != winner]
            print(winner)
            print('%s: %s' % (winner, str(self.players[self.players_index[winner]].hand)))
            for loser in losers:
                print('%s: %s' % (loser, str(self.players[self.players_index[loser]].hand)))
            return "DONE"
        elif len(losers) == 2:
            print('dealer')
            print('dealer: %s' % str(self.players[self.players_index['dealer']].hand))
            print('sam: %s' % str(self.players[self.players_index['sam']].hand))
            return "DONE"
        elif len(losers) == 1:
            winner = [p.name for p in self.players if p.name not in losers][0]
            print(winner)
            print('%s: %s' % (winner, str(self.players[self.players_index[winner]].hand)))
            for loser in losers:
                print('%s: %s' % (loser, str(self.players[self.players_index[loser]].hand)))
            return "DONE"
        elif game_is_done:
            # We already know that neither player has a card value of >= 21
            winner = []
            max_score = 0
            for player in self.players:
                score = player.get_hand_value()
                if score > max_score:
                    max_score = score
                    winner = [player.name]
                elif score == max_score:
                    winner += [player.name]

            if len(winner) == 2:
                print("It's a tie!")
                print('sam: %s' % str(self.players[self.players_index['sam']].hand))
                print('dealer: %s' % str(self.players[self.players_index['dealer']].hand))
            else:
                winner = winner[0]
                print(winner)
                print('%s: %s' % (winner, str(self.players[self.players_index[winner]].hand)))
                losers = [p.name for p in self.players if p.name != winner]
                for loser in losers:
                    print('%s: %s' % (loser, str(self.players[self.players_index[loser]].hand)))

            return "DONE"
        else:
            return "IN_PROGRESS"






