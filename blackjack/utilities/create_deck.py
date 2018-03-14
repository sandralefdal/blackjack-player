import random

"""
Simple script to create a deck in random order
"""


def get_random_deck():
    """
    :return: list of randomly ordered deck of cards
    """
    suits = ['C', 'D', 'H', 'S']
    ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    deck = []

    for suit in suits:
        for rank in ranks:
            deck += [suit+rank]

    random.shuffle(deck)

    return deck