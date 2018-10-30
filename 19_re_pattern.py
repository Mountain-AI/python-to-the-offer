# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return False
        # 如果s长度不为0，而pattern长度为0，这种情况不可能匹配成功
        elif len(s) != 0 and len(pattern) == 0:
            return False
        # 如果s长度为0， 而pattern长度不为0，那么可能会有pattern为'（.*）*'的情况
        elif len(s) == 0 and len(pattern) != 0:
            # 如果pattern第二位为0, pattern推进两个
            if len(pattern) > 1 and pattern[1] == '*':
                return self.match(s, pattern[2:])
            else:
                return False
        # 如果s和pattern长度都不为0
        else:
            # pattern第二位为*
            if len(pattern) > 1 and pattern[1] == '*':
                # 如果s[0] != pattern[0]
                if s[0] != pattern[0] and pattern[0] != '.':
                    return self.match(s, pattern[2:])
                # 如果s[0] == pattern[0], 那么有三种情况
                    # 1. s不变，pattern后移两步（pattern前两个字符等价于空）
                    # 2. s右移一个， pattern右移两个 （pattern前两个字符等价于一个字符）
                    # 3. s右移一个， pattern不右移 （pattern前两个字符等价于多个字符)）
                else:
                    return self.match(s, pattern[2:]) or \
                        self.match(s[1:], pattern[2:]) or \
                        self.match(s[1:], pattern)
            # pattern第二位不是*
            else:
                # 比较第一位的情况
                if s[0] == pattern[0] or pattern[0] == '.':
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


if __name__ == "__main__":
    s = 'aaa'
    pattern = ['a.a', 'ab*ac*a']
    ex = Solution()
    for pa in pattern:
        print(ex.match('', '.*'))
