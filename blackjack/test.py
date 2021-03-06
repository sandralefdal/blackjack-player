"""
Testing for the game.
"""
import sys

sys.path.append('.')
from blackjack.play import play_game

print("Running tests...")
print()

# No file path to deck given
print("TEST: No file path given to deck. Should create random deck and play.")
play_game()
print()

# File path to deck invalid
print("TEST: Invalid file path given to deck. Should exit game.")
play_game("fake/path")
print()

# Invalid cards in deck provided
print("TEST: Deck containing invalid cards. Should exit game.")
play_game("blackjack/deck/invalid_deck")
print()

# Empty deck
print("TEST: Empty file given as deck. No cards should be dealt, and game finish with no winners.")
play_game("blackjack/deck/empty_deck")
print()

# Deck containing one card
print("TEST: Deck given contains one card. Card should be dealt to sam, and sam should be winner of the game.")
play_game("blackjack/deck/one_card")
print()

# Both start with blackjack
print("TEST: Example from assignment, both players start with blackjack. Sam should win.")
play_game("blackjack/deck/both_initial_blackjack")
print()

# Provided example deck
print("TEST: Example given in assignment. Sam should win.")
play_game("blackjack/deck/deck_test")
print()

for i in range(10):
    print("TEST: Playing with random deck")
    play_game()
    print()
