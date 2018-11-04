# -*- coding=utf-8 -*-
class GetOccurTimesOfOne():
    """计算1-n中所有数字中1出现的次数"""

    def get_occur_time_of_one(self, num):
        if num is None or num < 1:
            return 0

        length = self.get_num_length(num)
        first = int(str(num)[0])
        # 第一位
        if first == 1:
            first_sum = num % self.base_10(length-1) + 1
        if first != 1:
            first_sum = self.base_10(length - 1)
        # 其他位
        other_num = self.base_10(length - 2) * (length - 1) * first
        next_num = self.get_occur_time_of_one(num % self.base_10(length-1))
        return first_sum + other_num + next_num

    def base_10(self, length):
        num = 1
        while length > 0:
            num *= 10
            length -= 1
        return num

    def get_num_length(self, num):
        length = 0
        while num != 0:
            length += 1
            num = num // 10
        return length


if __name__ == "__main__":
    ex = GetOccurTimesOfOne()
    num = 23457
    print(ex.get_occur_time_of_one(num))
