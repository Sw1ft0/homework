import argparse
import operator
import math 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operator', type=str)
    parser.add_argument('values', nargs="*", type=float)
    args = parser.parse_args()

    if hasattr(math, args.operator):
        res = getattr(math, args.operator)
    else:
        res = getattr(operator, args.operator)

    print(res(*args.values))

main()
