import arcade
from game.actor import Actor

class Player(arcade.SpriteCircle, Actor):
    def __init__(self, radius: int, color, soft: bool = False):
        super().__init__(radius, color, soft=soft)

        self._orientation = "RIGHT"
        