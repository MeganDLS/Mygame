import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Ball(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Ball.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the ball's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the ball's image.
        
        Returns:
            An instance of Image.
        """
        return self._image

    # def move_next(self):
    #     """Moves the bat using its velocity."""
    #     position = self._body.get_position()
    #     velocity = self._body.get_velocity()
    #     new_position = position.add(velocity)
    #     self._body.set_position(new_position)   

    # def swing_left(self):
    #     """Steers the bat to the left."""
    #     velocity = Point(-RACKET_VELOCITY, 0)
    #     self._body.set_velocity(velocity)
        
    # def swing_right(self):
    #     """Steers the bat to the right."""
    #     velocity = Point(RACKET_VELOCITY, 0)
    #     self._body.set_velocity(velocity)

    # def swing_up(self):
    #     """Steers the bat to the left."""
    #     velocity = Point(0, -RACKET_VELOCITY)
    #     self._body.set_velocity(velocity)
        
    # def swing_down(self):
    #     """Steers the bat to the right."""
    #     velocity = Point(0, RACKET_VELOCITY)
    #     self._body.set_velocity(velocity)

    # def stop_moving(self):
    #     """Stops the bat from moving."""
    #     velocity = Point(0, 0)
    #     self._body.set_velocity(velocity)
    
    def release(self):
        """Release the ball in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BALL_VELOCITY * rn, BALL_VELOCITY * rn])
        vy = -BALL_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)