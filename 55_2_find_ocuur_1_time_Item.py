# -*- coding=utf-8 -*-


class Solution():
    def find_item(self, arr):
        if arr is None or len(arr) < 4 or len(arr) % 3 != 1:
            return None

        temp = [0 for i in range(32)]
        for item in arr:
            bit_mark = 1
            for i in range(31, -1, -1):
                bit = item & bit_mark
                if bit != 0:
                    temp[i] += 1
                bit_mark = bit_mark << 1

        res = 0
        # 注意生成数时候的顺序
        for _ in temp:
            res = res << 1
            res += _ % 3

        return res


if __name__ == "__main__":
    ex = Solution()
    arr = [3, 3, 3, 1]
    print(ex.find_item(arr))
