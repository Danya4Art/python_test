import pytest
def func(x):
    return x + 1


def test_answer():
    mas=[1, 5, 3]
    mas[1]=func(2)