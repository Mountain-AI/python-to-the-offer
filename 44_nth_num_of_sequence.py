# -*- coding=utf-8 -*-
import sys


def get_nth_num_of_sequence(n):
    if n is None or n < 0:
        return None
    if n < 10:
        return n
    # 判断第n位的数组是几位数组以及对应位数数组在序列中开始的位置
    full_length, start = get_length_and_delta(n)
    # n位为几位数的第几个数的第几位
    nth, delta = (n - start) // full_length, (n - start) % full_length
    num = base_10(full_length - 1) + nth
    return int(str(num)[delta])


def get_nth_of_num(num, i):
    num = list(str(num))
    return int(num[i])


def base_10(length):
    num = 1
    while length > 0:
        num *= 10
        length -= 1
    return num


def get_length_and_delta(n):
    start = i = 1
    while start <= n:
        more = 9 * (10 ** (i - 1)) * i
        start += more
        i += 1
    return i - 1, start - more


if __name__ == "__main__":
    n = int(sys.argv[1])
    print(get_nth_num_of_sequence(n))
