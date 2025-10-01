class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict()


        for i in range(len(nums)):         
            pair = target - nums[i]
            if nums[i] in num_dict:
                return [num_dict[nums[i]], i] 
            num_dict[pair] = i 

        

