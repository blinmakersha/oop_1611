"""File with class Sphere."""
from math import pi

alpha = 180


class Sphere:
    """Class for the Sphere."""

    def __init__(self, radius, speed, boost, time):
        """Creates a sphere.

        Args:
            radius: float - radius of sphere.
            speed: float - speed of the sphere.
            boost: float - acceleration of the ball.
            time: float - time when sphere are rolling.
        """
        self.radius = radius
        self.speed = speed
        self.boost = boost
        self.time = time

    def uniform_motion(self):
        """Function finds angle of the uniform motioned by speed sphere.

        Returns:
            angle: float - angle in degrees.
        """
        way = self.speed * self.time
        res = (way * alpha) / (pi * self.radius)
        return round(res, 2)

    def acc_motion(self):
        """Function finds angle of the uniformly accelerated sphere.

        Returns:
            angle: float - angle in degrees.
        """
        speed = self.boost * self.radius
        way = speed * self.time
        res = (way * alpha) / (pi * self.radius)
        return round(res, 2)

# print(Sphere(9, 5, 2, 4).uniform_motion())
# print(Sphere(9, 5, 2, 4).acc_motion())
