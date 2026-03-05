from cli import calculate
from calculator import Calculator

def test_user_addition_flow():

    result = calculate(5, "+", 3)

    assert result == 8


def test_clear_after_calculation():

    calc = Calculator()

    result = calc.add(4, 5)

    cleared = calc.clear()

    assert cleared == 0