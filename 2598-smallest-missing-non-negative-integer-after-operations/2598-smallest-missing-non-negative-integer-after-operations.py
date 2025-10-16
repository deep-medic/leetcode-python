class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        counter = defaultdict(int)
        depth = 0
        i = 0

        for num in nums:
            counter[num % value] += 1

        while True:
            if counter[i] == 0:
                return i + (depth * value)

            counter[i] -= 1

            i = (i + 1) % value
            if i == 0:
                depth += 1