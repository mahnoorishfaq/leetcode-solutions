class Solution:
    def twoSum(self, nums, target):
        Dictionary = {}       
        for i, num in enumerate(nums):
            compl = target - num
            if compl in Dictionary:
                return [Dictionary[compl], i]
            Dictionary[num] = i
        return []