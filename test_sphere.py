from sphere2 import Sphere, MoveUni
import pytest

test_get_radius = [(10, 10), (20, 20), (30, 30)]

test_uniform_motion = [(10, 4, 6, 137.51), (50, 20, 10, 229.18), (100, 0, 10, 0.0)]

test_acc_motion = [(100, 0, 10, 0.0), (10, 3, 10, 1718.87), (100, 30, 50, 85943.67)]


@pytest.mark.parametrize('radius_valid, radius_expected', test_get_radius)
def test_getRadius(radius_valid, radius_expected):
    ball = Sphere(radius_valid)
    assert ball.get_radius() == radius_expected

@pytest.mark.parametrize('radius, speed, time, grade', test_uniform_motion)
def test_uniformMotion(radius, speed, time, grade):
    res = MoveUni.uniform_motion(radius, speed, time)
    assert res == grade

@pytest.mark.parametrize('radius, boost, time, grade', test_acc_motion)
def test_accMotion(radius, boost, time, grade):
    res = MoveUni.acc_motion(radius, boost, time)
    assert res == grade