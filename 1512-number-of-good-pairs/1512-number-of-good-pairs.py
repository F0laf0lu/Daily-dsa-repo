class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        num_map = {}
        count = 0

        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                count += num_map[num]
                num_map[num] += 1
        return count
        