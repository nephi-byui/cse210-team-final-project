from game.actor import Actor
from game import constants
import arcade

class Bullet(arcade.SpriteCircle, Actor):
    def __init__(self, radius =5, color="red", soft: bool = False):
        super().__init__(radius, color, soft=soft)

    def set_bullet_direction(self):
        
        if self._orientation == "UP":
            self.change_y = constants.BULLET_SPEED
        elif self._orientation == "DOWN":
            self.change_y = -(constants.BULLET_SPEED)
        elif self._orientation == "LEFT":
            self.change_X = -(constants.BULLET_SPEED)
        elif self._orientation == "RIGHT":
            self.change_X = constants.BULLET_SPEED
        """
        # THIS IS NOT WORKING
        if self._orientation == "UP":
            self.velocity = [0,1]
        elif self._orientation == "DOWN":
            self.velocity = [0,-1]
        elif self._orientation == "LEFT":
            self.velocity = [-1,0]
        elif self._orientation == "RIGHT":
            self.velocity = [1,0]
        """

    def set_orientation(self, orientation):
        self._orientation = orientation