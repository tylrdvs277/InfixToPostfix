# Name:        Tyler Davis
# Course:      CPE 202
# Instructor:  Dave Parkinson
# Assignment:  Assignment 2
# Term:        Fall 2017

from Stacks import StackArray

def infix_to_postfix(infixexpr): 
    """Converts an infix expression to an equivalent postfix expression"""
    """Signature:  a string containing an infix expression where tokens 
    are space separated is the single input parameter and returns a string 
    containing a postfix expression where tokens are space separated"""
    op_stack = StackArray(30)
    tokens = infixexpr.split(" ")
    output = []
    for token in tokens:
        if is_num(token):
            output.append(token)
        elif token == ")":
            while op_stack.peek() != "(":
                output.append(op_stack.pop())
            op_stack.pop()
        else:
            while (not op_stack.is_empty() and 
                   precedence(token) <= precedence(op_stack.peek()) and 
                   token not in "^("):
                output.append(op_stack.pop())
            op_stack.push(token)
    for count in range(op_stack.size()):
        output.append(op_stack.pop())
    return " ".join(output)

def is_num(token):  
    """Determines whether a character is a number"""
    """Input argument: a string representing a single token.
    Tokens are either operators {+-*/^} or numbers.
    Returns a boolean whether the token is a number."""
    try:
        float(token)
        return True
    except ValueError:
        return False

def precedence(operation): 
    """Assigns a relative order of precedence to the operators"""
    """Input argument: a single token that represents an operation.
    Returns an int representing the precedence."""
    ops = ["(", ")", "+", "-", "*", "/", "^"]
    for idx in range(len(ops)):
        if ops[idx] == operation:
            return idx // 2

def postfix_eval(postfixexpr): 
    """Evaluates a postfix expression"""
    """Input argument: a string containing a postfix expression where tokens
    are space separated. Tokens are either operators {+-*/^} or numbers.
    Returns an int or float as the result."""
    tokens = postfixexpr.split(" ")
    num_stack = StackArray(len(tokens))
    for token in tokens:
        if is_num(token):
            num_stack.push(float_or_int(token))
            continue
        second = num_stack.pop()
        first = num_stack.pop()
        result = do_math(token, first, second)
        num_stack.push(result)
    return num_stack.pop()

def float_or_int(num):
    """Determines whether a number is better represented as an int or float"""
    """Input argument: a string representing a number.
    Returns a float or int version of the string."""
    if "." in num:
        return float(num)
    return int(num)

def do_math(op, op1, op2): 
    """Performs the actual mathematic operation"""
    """Input argument: two numbers (floats) and an operation.
    Returns a float representing the result of the operation."""
    if op == "+":
        result = op1 + op2
    elif op == "-":
        result = op1 - op2
    elif op == "*":
        result = op1 * op2
    elif op == "/":
        if op2 == 0:
            raise ValueError
        result = op1 / op2
    else:
        result = op1 ** op2
    return result

def postfix_valid(postfixExpr):
    """Determines whether a string is a valid postfix expression"""
    """Input argument: a string containing a postfix expression.
    Returns true if the expression is valid and false otherwise."""
    num_on_stack = 0
    tokens = postfixExpr.split(" ")
    for token in tokens:
        if is_num(token):
            num_on_stack += 1
        else:
            if num_on_stack < 2:
                return False
            num_on_stack -= 1
    return num_on_stack == 1
