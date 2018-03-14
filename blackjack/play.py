"""
Implementation of game of Poker between two players, Sam and Dealer.
"""
import sys

from blackjack.objects.player import Player
from blackjack.objects.deck import Deck
from blackjack.objects.game import Game


def play_game(deckfile = None):
    """
    Plays a game between dealer and sam
    :param deckfile: file path to deck file
    :return:
    """
    # Initialize players
    sam = Player("sam")
    dealer = Player("dealer")

    # Initialize deck
    deck = Deck()
    if deckfile is not None:
        success = deck.read_from_file(deckfile)
    else:
        success = deck.create_random_deck()

    if success == 1:
        # Initialize game
        game = Game(deck, [sam, dealer])
        state = game.initialise()

        # Keep playing until game is done
        while state != 'DONE':
            state = game.play_card()


if __name__ == '__main__':
    """
    Run from command line with one optional argument: filepath to deck
    """
    sys.argv = ["", "deck/deck"]

    deckfile = None
    if len(sys.argv) > 1:
        deckfile = sys.argv[1]

    play_game(deckfile)