# Player class and methods to manipulate pieces

# import files created
import pieces as letters
# other modules that need to be imported
import random


# Ask both players for their names
# stores this string in their respective player variables
# player1 = input("Player 1, what is your name: ")
# player2 = input("Player 2, what is your name: ")


class Player:
    """Class that creates the Player object"""
    def __init__(self, name):
        self._name = name
        self._points = 0
        self._tiles = []

    def get_name(self):
        """Get method to access name of the player"""
        return self._name

    def get_points(self):
        """Get method to access point total for the player"""
        return self._points

    def get_tiles(self):
        """Get method to access the tiles a Player has"""
        return self._tiles

    def replace_used_tiles(self):
        """Method to replace the tiles used by player in the previous turn"""
        counter = 0
        while counter < 7:
            tile = random.choice(letters.tiles)
            self._tiles.append(tile)
            letters.tiles.remove(tile)
            counter += 1
        return "Tiles "


def who_goes_first(p1, p2):
    """Method that decides who goes first randomly"""
    determiner = random.randrange(100)
    if determiner % 2 == 1:
        return f"{p2} will go first"
    else:
        return f"{p1} will go first"


def initialize_tiles(player):
    """Method that randomly initializes the 7 tiles that are given to each player at the beginning of the game"""
    counter = 0
    while counter < 7:
        tile = random.choice(letters.tiles)
        player._tiles.append(tile)
        letters.tiles.remove(tile)
        counter += 1
    return "Tiles initialized"
