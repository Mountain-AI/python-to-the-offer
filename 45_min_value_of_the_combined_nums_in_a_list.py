# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) < 1:
            return None

        temp_dict = {key: str(value) for key, value in enumerate(numbers)}
        longest = self.get_longest(temp_dict.values())
        for i in range(len(temp_dict)):
            while len(temp_dict[i]) < longest:
                temp_dict[i] = temp_dict[i] + temp_dict[i][-1]

        res = []
        for item in sorted(temp_dict.items(), key=lambda item: item[1]):
            res.append(numbers[item[0]])
        return int(''.join(map(str, res)))

    def get_longest(self, arr):
        longest = 0
        for item in arr:
            if len(item) > longest:
                longest = len(item)
        return longest


if __name__ == "__main__":
    nums = [3, 32, 321]
    ex = Solution()
    print(ex.PrintMinNumber(nums))
