class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_nums = dict()

        for i in nums:
            if i not in count_nums:
                count_nums[i] = 1
            else:
                count_nums[i] += 1

                if count_nums[i] > 1:
                    return True
                
        return False