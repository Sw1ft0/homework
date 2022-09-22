import argparse

parser = argparse.ArgumentParser(description='ebnf')
parser.add_argument('string', nargs='?', type=str)
args = parser.parse_args()

def operate():
    if args.string:
        signs = ['+', '-']
        previous_symbol = ''
        is_valid = True
        for symbol in args.string:
            if symbol.isnumeric() or (symbol in signs and previous_symbol.isnumeric() and symbol != args.string[-1]):
                previous_symbol = symbol
            else:
                is_valid = False
                break
    else:
        is_valid = False

    return is_valid


def main():
    result = operate()
    if result:
        print(result, eval(args.string))
    else:
        print(result, None)

main()
