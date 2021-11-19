import arcade
from game import constants
from game.actor import Actor
from game.point import Point
from game.__init__ import Game
from game.enemy import Enemy
from game.player import Player
from game.bullet import Bullet


def main(screen):
    
    arcade.open_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

    arcade.set_background_color(arcade.color.WHITE)
    
    arcade.Window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    arcade.run()
