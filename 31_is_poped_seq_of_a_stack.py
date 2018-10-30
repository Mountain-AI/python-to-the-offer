# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV) != len(popV):
            return False

        stack = []
        cur_push = 0
        cur_pop = 0
        while stack or cur_push < len(pushV):
            # cur_pop与栈顶相同，则弹出，cur_pop + 1
            if stack and stack[-1] == popV[cur_pop]:
                stack.pop()
                cur_pop += 1
            else:
                # cur_pop与栈顶不同，那么开始压栈，直到找到相等值
                while cur_push < len(pushV) and pushV[cur_push] != popV[cur_pop]:
                    stack.append(pushV[cur_push])
                    cur_push += 1
                if cur_push < len(pushV):
                    stack.append(pushV[cur_push])
                    cur_push += 1
                # 去除长度不等之外的唯一错误情况：找不到相等值压栈
                else:
                    return False

        return True


if __name__ == "__main__":
    pushv = [1, 2, 3, 4, 5]
    popv = [4, 5, 3, 2, 1]
    ex = Solution()
    print(ex.IsPopOrder(pushv, popv))
