import pytest
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle


@pytest.fixture
def create_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def create_square():
    return Square(10)


@pytest.fixture
def create_circle():
    return Circle(10)


@pytest.fixture
def create_triangle():
    return Triangle(3, 4, 5)

