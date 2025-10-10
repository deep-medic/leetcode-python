class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        max_num = -float(inf)
        start = 0
        energy.reverse()
        pre_sum = 0

        while start < k:
            depth = 0
            total = 0
            while start + k * depth < length:
                total += energy[start + k * depth]
                depth += 1

                max_num = max(max_num, total)
            start += 1
            print (f"start:{start}, depth:{depth}, length:{length}, total:{total}")

        return max_num