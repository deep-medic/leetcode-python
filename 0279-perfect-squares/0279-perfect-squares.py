class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] + [10**9] * n
        squares = [i*i for i in range(1, math.isqrt(n) + 1)]

        for i in range(1, n + 1):
            for s in squares:
                if s > i:
                    break
                if dp[i - s] + 1 < dp[i]:
                    dp[i] = dp[i - s] + 1
        return dp[n]