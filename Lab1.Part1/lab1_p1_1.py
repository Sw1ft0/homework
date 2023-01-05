import argparse

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first', type=float)
    parser.add_argument('operator', type=str, choices = ["+","-","*","/"])
    parser.add_argument('second', type=float)

    args = parser.parse_args()
    if args.operator == "/" and args.second == 0:
        print("Error! Division by zero is not allowed.")
    else:
        print(op[args.operator](args.first, args.second))
    
main()
