class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count_dict = Counter(nums)
        len_nums = len(nums)
        max_num = max(nums)
        sum_dict = {}

        for i in range(1, max_num+1):
            sum_dict[i] = i * count_dict.get(i, 0)

        dp = [0] * (max_num + 1)

        dp[0] = 0
        dp[1] = sum_dict.get(1, 0)

        for i in range(2, max_num + 1):
            current = sum_dict.get(i, 0)
            dp[i] = max(current + dp[i-2], dp[i-1])

        return dp[-1]