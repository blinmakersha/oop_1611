from main import Sphere
import pytest

tests_sphere_init = [(4, 4, 4, 4)]

test_uniform_motion = [(10, 4, 2, 6, 137.51), (50, 20, 2, 10, 229.18), (100, 0, 2, 10, 0.0)]

test_acc_motion = [(100, 0, 0, 10, 0.0), (10, 0, 3, 10, 1718.87), (100, 0, 30, 50, 85943.67)]


@pytest.mark.parametrize('radius, speed, boost, time', tests_sphere_init)
def test_init_ball(radius, speed, boost, time):
    ball = Sphere(radius, speed, boost, time)
    assert ball.radius == radius and ball.speed == speed and ball.boost == boost and ball.time == time


@pytest.mark.parametrize('radius, speed,boost, time, grade', test_uniform_motion)
def test_uniformmotion(radius, speed, boost, time, grade):
    ball = Sphere(radius, speed, boost, time)
    res = ball.uniform_motion()
    assert res == grade


@pytest.mark.parametrize('radius,speed, boost, time, grade', test_acc_motion)
def test_accmotion(radius, speed, boost, time, grade):
    ball = Sphere(radius, speed, boost, time)
    res = ball.acc_motion()
    assert res == grade
