import argparse
import operator
import math 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operator', type=str)
    parser.add_argument('values', nargs="*", type=float)
    args = parser.parse_args()

    try:
        if hasattr(math, args.operator):
            res = getattr(math, args.operator)
        elif hasattr(operator, args.operator):
            res = getattr(operator, args.operator)
        else:
            quit('Incorrect input')
        print(res(*args.values))
    except ZeroDivisionError as x:
        print(x)
    except ValueError as y:
        print(y)
main()
