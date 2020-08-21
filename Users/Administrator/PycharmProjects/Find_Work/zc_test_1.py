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