# -*- coding=utf-8 -*-


def print_1_to_n(n):
    if n < 1:
        return

    i = 1
    while len(str(i)) <= n:
        print(i)
        i += 1
    print(' ')


if __name__ == "__main__":
    print(print_1_to_n(2))
