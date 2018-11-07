# -*- coding=utf-8 -*-



def get_multi_list(arr):
    if arr is None or len(arr) < 1:
        return -1
    if len(arr) == 1:
        return arr

    length = len(arr)
    res = [0 for i in range(len(arr))]

    res[0] = 1
    for i in range(1, length):
        res[i] = res[i-1]*arr[i-1]

    temp = 1
    for j in range(length-2, -1, -1):
        temp *= arr[j+1]
        res[j] *= temp

    return res


if __name__ == "__main__":
    num = [1, 2, 3, 4, 5]
    print(get_multi_list(num))
