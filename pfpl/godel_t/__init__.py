#!/usr/bin/env python3.11
from typing import T

class Lang:
    pass

class GodelT:
    pass

class Sort(GodelT):
    pass

class Type(Sort):
    variable = r"\tau"
    args = []

class Nat(Type):
    pass

class Arrow(Type):
    notation = 'arrow'
    args = [ r'\tau_1', r'\tau_2']

class Expression(Sort):
    variable = "e"

class Variable(Expression):
    pass

class UnaryNumeral(Expression):
    pass

class Zero(UnaryNumeral):
    notation = 'zero'

class Successor(UnaryNumeral):
    notation = 'succ'
    args = ["e"]

class Recursor(Expression):
    notation = r'rec[\tau](e0, x, y, e1)(e)'
    args = [ r'\tau', 'e0', 'x', 'y', 'e1', 'e' ]

class Statement(GodelT): pass

class Typehood(Statement):
    notation = r'\tau type'
    args:
        - r'\tau'

class Element(Statement):
    notation = r'e : \tau'
    args:
        - 'e'
        - r'\tau'

Program = list[Statement]

def main():
    pass

if __name__ == "__main__":
    raise SystemExit(main())
