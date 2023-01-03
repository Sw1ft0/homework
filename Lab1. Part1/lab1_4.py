import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-W', nargs=1, type=int)
    parser.add_argument('-w', nargs='+', type=int)
    parser.add_argument('-n', nargs=1, type=int)

    args = parser.parse_args()
    if len(args.w) != args.n[0]:
        print("Error!")
    else:
        a = args.W[0]
        b = [0] * (a+1)
        b[0] = 1
        for i in args.w:
            for j in range(a, -1, -1):
                if b[j] == 1 and j+i<=a:
                    b[j + i] = 1
        for i in range(a, -1, -1):
            if b[i] == 1 and i <= a:
                print(i)
                break
main()
