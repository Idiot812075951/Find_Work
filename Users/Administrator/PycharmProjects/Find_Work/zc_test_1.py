#这是一个，力扣的题目答案，大概是二进制多位数，转换成全是0的最小次数，如100，
# 转化成000需要反转几次
class Solution:
    def minFlips(self, target: str) -> int:
        flips, prev = 0, "0"
        for curr in target:
            if curr != prev:
                flips += 1
                prev = curr
        return flips


s=Solution()
print(s.minFlips("10011101010100"))