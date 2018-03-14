# Blackjack - player

Simple game of blackjack between two players, sam and dealer.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need Python 3 to run the project. \
To check which python is on your machine, run in the command line:

```
python --version
```

### Installing

This module requires no additional libraries to run.

Clone or download the repo to where you want to run it from.

Then run:

```commandline
cd blackjack-player/
```

To play with a random deck, run:

```buildoutcfg
python blackjack/play.py
```

If you have a deck you want to use, you can run:

```buildoutcfg
python blackjack/play.py {file_path}
```

where \
file_path is the reference to the deck file. \
Deck file contains one line of data where each card is comma separated, in the following format:
```commandline
CA, D4, H7, SJ,..., S5, S9, D10
```

## Running the tests

You can run the automated tests by running
```commandline
python blacjack/test.py
```

### Tests break down

The tests aim to test edge cases, as well as regular plays 

Edge cases: 

* Empty deck of card
* Broken file path
* Deck containing less than 4 cards
* Deck containing invalid cards 

Regular cases:

* Deck given as example in assignment
* 10 iterations of play with a random deck

## Authors

* **Sandra Lefdal** 

