import arcade
from game.point import Point
from game.velocity import Velocity

class Actor():
    """ Handles the active sprites of the game
    """
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0.0
        self.alive = True
        self.rotate = 0.0
        self.angle = 0.0
        self.points = 0.0        
        
    def advance(self):
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
        self.angle += self.rotate
        
    def is_off_screen(self, screen_width, screen_height):
        if self.center.x > screen_width:
            self.center.x = 0
        elif self.center.x < 0:
            self.center.x = screen_width
        if self.center.y > screen_height: 
            self.center.y = 0
        elif self.center.y < 0:
            self.center.y = screen_height

    def set_orientation(self, orientation):
        """ Make the actor face a certain direction
        ARGS:
            self (LiveActor): an instance of Player
            direction (string): should be in [ "UP", "DOWN", "LEFT", "RIGHT" ]
        """
        orientation = orientation.upper()

        if orientation in [ "UP", "DOWN", "LEFT", "RIGHT" ]:
            self._orientation = orientation
        else:
            self._orientation = "RIGHT"
        
    def get_orientation(self):
        """ Returns the orientation
        ARGS:
            self (LiveActor):
        RETURNS:
            orientation (STR)
        """
        return self._orientation

    def do_updates():
        pass


    # hp functions
    def get_hp(self):
        return self._hp

    def set_hp(self, new_hp):
        self._hp = new_hp

    def change_hp(self, hp_change):
        self._hp = self._hp + hp_change

    def debug_console_hp(self):
        print(self._hp)