# -*- coding:utf-8 -*-
class Solution:
    def Add(self, a, b):
        while(b & 0xFFFFFFFF > 0):  # 防止b溢出32位范围
            a, b = (a ^ b), ((a & b) << 1)
        print(hex(a))
        if abs(a) >= 0xFFFFFFFF:
            return a & 0xFFFFFFFF
        return a


if __name__ == "__main__":
    ex = Solution()
    print(ex.Add(-2**30, -1))√
