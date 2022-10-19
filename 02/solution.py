from itertools import chain

def display_pattern(num: int):
    size = 2 * num - 1
    stack = []
    for i in chain(range(1, num + 1), reversed(range(1, num))):
        for j in range(1, i + 1):
            stack.append(j)
            print(j, end=" ")

        for k in range(size - 2 * len(stack)):
            print(stack[-1], end=" ")

        if (i == num):
            stack.pop()

        while stack:
            print(stack.pop(), end=" ")

        print()


if __name__ == "__main__":
    number = input("Enter an integer: ") 
    display_pattern(int(number))