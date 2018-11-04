# -*- coding=utf-8 -*-


class Solution():
    def get_max_length_of_undup_str(self, string):
        if string is None or len(string) <= 1:
            return int(string) if string is not None else None

        res = [0 for i in range(len(string))]
        index_arr = [-1 for i in range(52)]
        res[0] = 1
        index_arr[self.get_index(0, string)] = 0
        for i in range(1, len(string)):
            char_index = self.get_index(i, string)
            delta = i - index_arr[char_index]
            if index_arr[char_index] == -1 or delta > res[i-1]:
                res[i] = res[i-1] + 1
            else:
                res[i] = delta
            # 更新当前字符的最新索引
            index_arr[char_index] = i

        return res[-1]

    def get_index(self, index, string):
        temp = ord(string[index])
        if 65 <= temp <= 90:
            return temp - ord('A')
        elif 97 <= temp <= 122:
            return temp - ord('a') + 26
        else:
            raise TypeError('not a valid char!')


if __name__ == "__main__":
    string = input()
    ex = Solution()
    print(ex.get_max_length_of_undup_str(string))
