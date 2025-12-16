# tests/unit/test_core.py

from src.calculator.core import evaluate_expression

def test_addition():
    assert evaluate_expression("1 + 1") == 2.0

def test_subtraction():
    assert evaluate_expression("5 - 2") == 3.0

def test_multiplication():
    assert evaluate_expression("3 * 4") == 12.0

def test_division():
    assert evaluate_expression("10 / 2") == 5.0

def test_exponentiation():
    assert evaluate_expression("2 ** 3") == 8.0
    assert evaluate_expression("3 ** 2") == 9.0
    assert evaluate_expression("2 ** 3 ** 2") == 512.0 # Right-associativity

def test_order_of_operations():
    assert evaluate_expression("2 + 3 * 4") == 14.0
    assert evaluate_expression("(2 + 3) * 4") == 20.0

def test_division_by_zero():
    # Expect a ZeroDivisionError for division by zero
    try:
        evaluate_expression("10 / 0")
        assert False, "ZeroDivisionError was not raised"
    except ZeroDivisionError as e:
        assert "division by zero" in str(e).lower()

def test_malformed_expression():
    # Expect a ValueError for malformed expressions
    try:
        evaluate_expression("5 * + 2")
        assert False, "ValueError was not raised for malformed expression"
    except ValueError as e:
        assert "malformed expression" in str(e).lower()

    try:
        evaluate_expression("(10 + 5")
        assert False, "ValueError was not raised for malformed expression"
    except ValueError as e:
        assert "malformed expression" in str(e).lower()
