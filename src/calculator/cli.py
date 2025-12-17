# src/calculator/cli.py
import argparse
from calculator.core import evaluate_expression

def main():
    """
    Command-line interface for the calculator.
    """
    parser = argparse.ArgumentParser(description="A simple command-line calculator.")
    parser.add_argument("expression", type=str, help="The mathematical expression to evaluate.")

    args = parser.parse_args()

    try:
        result = evaluate_expression(args.expression)
        print(result)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
