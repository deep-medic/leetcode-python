class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)

        dp = [0] * len_nums

        if len_nums == 1:
            return nums[0]
        elif len_nums == 2:
            return max(nums[0], nums[1])

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        
        for i in range(2, len_nums):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return dp[-1]