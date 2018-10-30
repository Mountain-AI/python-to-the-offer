# -*- coding=utf-8 -*-


def get_nk_item(arr, k):
    """求数组中出现次数超过N/K的元素

    Arguments:
        arr {list} -- 数组
        k {int} -- 分母

    Returns:
        tuple -- 所求元素
    """

    if len(arr) < k:
        return 0

    buf_dict = {}
    for i in range(len(arr)):
        if arr[i] in buf_dict:
            buf_dict[arr[i]] += 1
        else:
            if len(buf_dict) < k - 1:
                buf_dict[arr[i]] = 1
            else:
                for item in buf_dict:
                    buf_dict[item] -= 1
        remove_invalid(buf_dict)

    check_valid(arr, k, buf_dict)

    return tuple(buf_dict.keys())


def remove_invalid(buf_dict):
    """删除buf_dict中value值小于1的元素"""

    buf_remove = []
    for item in buf_dict:
        if buf_dict[item] < 1:
            buf_remove.append(item)

    for item in buf_remove:
        buf_dict.pop(item)


def check_valid(arr, k, buf_dict):
    """检测所求的元素是否满足次数要求"""

    buf_remove = []
    for item in buf_dict:
        if arr.count(item) <= len(arr) // k:
            buf_remove.append(item)

    for item in buf_remove:
        buf_dict.pop(item)


if __name__ == "__main__":
    nums = [[2, 2, 2, 2, 2, 5, 5, 5, 5],
            [2, 3, 4, 5, 2, 3, 4, 2, 3, 2, 2, 2, ]]

    print(get_nk_item(nums[1], 4))
    print(nums[1].count(3), len(nums[1])//4)
