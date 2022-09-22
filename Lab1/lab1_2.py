import argparse
import operator


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operator')
    parser.add_argument('first', type=float)
    parser.add_argument('second', type=float)
    args = parser.parse_args()

    try:
        func = getattr(operator, args.operator)
    except:
        print('Wrong function')

    print(func(args.first, args.second))

main()
