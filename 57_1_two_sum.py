# -*- coding=utf-8 -*-


def two_sum(arr, g_sum):
    if arr is None or len(arr) < 2:
        return None

    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == g_sum:
            return arr[start], arr[end]
        elif arr[start] + arr[end] < g_sum:
            start += 1
        else:
            end -= 1


if __name__ == "__main__":
    arr = [1, 2, 4, 7, 11, 15]
    g_sum = 15
    print(two_sum(arr, g_sum))
