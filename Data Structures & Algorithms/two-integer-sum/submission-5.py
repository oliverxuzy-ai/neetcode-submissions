class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        # target = [current_index, pair_index]

        # pair[pair_num] = pair_index
        # pair_num = target - current_num

        for i in range(len(nums)):
            diff[nums[i]] = i
        
        for n in range(len(nums)):
            if (target - nums[n]) in diff and n != diff[target - nums[n]]:
                return [n,diff[target - nums[n]]] 



