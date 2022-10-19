from itertools import chain
import sys

def make_diamond(n: int):
    for i in chain(range(1, n + 1), reversed(range(1, n))):
        print(f"{' ' * (n - i)}{str(i) * (2 * i - 1)}")


if __name__ == "__main__":
    make_diamond(int(sys.argv[1]))