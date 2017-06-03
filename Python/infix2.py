#!usr/bin/python

####################
# Author: Nathan Mador-House
# Title: Infix Converter V2
####################

from lib import pyds
def postfixEval(postfixExpr):
    operandStack = pythonDataStructures.Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(resunt)
    return operandStack

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "%":
        return op1 % op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
