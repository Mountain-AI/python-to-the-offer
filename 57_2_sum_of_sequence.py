# -*- coding=utf-8 -*-


def get_sequence(g_sum):
    if g_sum < 3:
        return None

    small, big = 1, 2
    res = []
    while small <= g_sum // 2:
        cur_sum = sum(range(small, big+1))
        if cur_sum == g_sum:
            res.append((small, big))
            big += 1
        elif cur_sum < g_sum:
            big += 1
        else:
            small += 1

    return res


if __name__ == "__main__":
    print(get_sequence(15))
