# -*- coding=utf-8 -*-


def cut_rope(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    temp_arr = [0 for i in range(n+1)]
    # f(1), f(2), f(3)作为别人切下的子过程的时候与自己本身返回时不同的
    pre = (0, 1, 2, 3)
    for i in range(len(pre)):
        temp_arr[i] = pre[i]

    for i in range(4, n+1):
        max_mul = 0
        for j in range(1, i//2+1):
            max_mul = max(temp_arr[j] * temp_arr[i - j], max_mul)
        temp_arr[i] = max_mul

    return temp_arr[n]


if __name__ == "__main__":
    n = [4, 5]
    for i in n:
        print(cut_rope(i))
