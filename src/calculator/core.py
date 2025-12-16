# src/calculator/core.py
import operator

OPS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
}

PRECEDENCE = {
    '+': 1, '-': 1,
    '*': 2, '/': 2,
    '**': 3,
}

def apply_op(op, left, right):
    return OPS[op](left, right)

def has_precedence(op1, op2):
    return PRECEDENCE[op1] >= PRECEDENCE[op2]

def evaluate_expression(expression: str) -> float:
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
            continue
        elif char.isdigit() or (char == '-' and (i == 0 or expression[i-1] in OPS or expression[i-1] == '(')) or char == '.':
            # Handle negative numbers and decimal points
            j = i
            if char == '-': # Capture leading negative for a number
                j += 1
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            if j == i + 1 and expression[i] == '-': # Just a minus sign, not a negative number
                tokens.append(char)
                i += 1
            else:
                tokens.append(float(expression[i:j]))
                i = j
            continue
        elif char in OPS:
            # Handle '**' operator
            if char == '*' and i + 1 < len(expression) and expression[i+1] == '*':
                tokens.append('**')
                i += 2
            else:
                tokens.append(char)
                i += 1
            continue
        elif char == '(':
            tokens.append(char)
            i += 1
            continue
        elif char == ')':
            tokens.append(char)
            i += 1
            continue
        else:
            raise ValueError(f"Malformed expression: Invalid character '{char}'")

    if not tokens:
        raise ValueError("Malformed expression: Empty expression")

    output_queue = []
    operator_stack = []

    for token in tokens:
        if isinstance(token, float):
            output_queue.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError("Malformed expression: Mismatched parentheses")
            operator_stack.pop() # Pop '('
        elif token in OPS:
            while (operator_stack and operator_stack[-1] != '(' and
                   ((token != '**' and has_precedence(operator_stack[-1], token)) or
                    (token == '**' and PRECEDENCE[operator_stack[-1]] > PRECEDENCE[token]))): # Right-associativity for **
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        else:
            raise ValueError(f"Malformed expression: Unexpected token '{token}'")

    while operator_stack:
        if operator_stack[-1] == '(':
            raise ValueError("Malformed expression: Mismatched parentheses")
        output_queue.append(operator_stack.pop())

    # Evaluate RPN
    operand_stack = []
    for token in output_queue:
        if isinstance(token, float):
            operand_stack.append(token)
        elif token in OPS:
            if len(operand_stack) < 2:
                raise ValueError("Malformed expression: Insufficient operands for operator")
            right = operand_stack.pop()
            left = operand_stack.pop()
            try:
                result = apply_op(token, left, right)
                operand_stack.append(result)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero")
            except Exception as e:
                raise ValueError(f"Malformed expression: Error during calculation - {e}")
        else:
            raise ValueError(f"Malformed expression: Unexpected token during RPN evaluation '{token}'")

    if len(operand_stack) != 1:
        raise ValueError("Malformed expression: Invalid number of operands")

    return operand_stack[0]