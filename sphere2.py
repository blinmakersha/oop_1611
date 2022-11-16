"""File with class Sphere."""
from math import pi

alpha = 180


class Sphere:
    """Class for the Sphere."""

    def __init__(self, radius):
        """Creates a sphere.
        Args:
            radius: float - radius of sphere.
        """
        self.radius = radius

    def get_radius(self):
        return self.radius

class MoveUni(Sphere):

    def uniform_motion(radius, speed, time):
        """Function finds angle of the uniform motioned by speed sphere.
        Returns:
            angle: float - angle in degrees.
        """
        way = speed * time
        res = (way * alpha) / (pi * radius)
        return round(res, 2)

    def acc_motion(radius, boost, time):
        """Function finds angle of the uniformly accelerated sphere.
        Returns:
            angle: float - angle in degrees.
        """
        speed = boost * radius
        way = speed * time
        res = (way * alpha) / (pi * radius)
        return round(res, 2)

ball = Sphere(10)

ball_u = MoveUni.uniform_motion(ball.get_radius(), 4, 6)
ball_a = MoveUni.acc_motion(ball.get_radius(), 6, 8)
print(ball_u)
print(ball_a)
