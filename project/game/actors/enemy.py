import arcade
from game.actor import Actor

class Enemy(arcade.SpriteSolidColor, Actor):
    def __init__(self, width: int, height: int, color):
        super().__init__(width, height, color)
        self.set_hp(10)