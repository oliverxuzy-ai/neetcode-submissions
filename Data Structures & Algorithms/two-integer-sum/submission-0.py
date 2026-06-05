class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()

        for i in range(len(nums)):
            diff[target - nums[i]] = i
        
        for j in range(len(nums)):
            if nums[j] in diff and j != diff[nums[j]]:
                return [j,diff[nums[j]]]
