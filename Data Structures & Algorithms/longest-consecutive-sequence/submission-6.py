class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0 
        check = set(nums)
        i = 0

        while i < len(nums):
            temp_max = 0
            if nums[i] - 1 not in check:
                # j = i+1
                temp_max += 1
                num_next = nums[i] + 1
                while num_next in check:
                    temp_max += 1
                    num_next += 1
                    # j += 1

            i += 1
            max_seq = max(temp_max, max_seq)


        return max_seq

