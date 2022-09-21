import argparse

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first', type=float)
    parser.add_argument('operator')
    parser.add_argument('second', type=float)

    args = parser.parse_args()

    print(op[args.operator](args.first, args.second))

main()
