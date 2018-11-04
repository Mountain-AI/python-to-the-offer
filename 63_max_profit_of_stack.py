# -*- coding=utf-8 -*-


def get_max_profit(arr):
    if arr is None or len(arr) < 2:
        return 0

    min_price = arr[0]
    max_profit = arr[1] - min_price
    for item in arr[2:]:
        if item < min_price:
            min_price = item
        max_profit = max(max_profit, item - min_price)

    return max_profit


if __name__ == "__main__":
    num = [9, 11, 8, 5, 7, 12, 16, 14]
    print(get_max_profit(num))  # The anster is 11
