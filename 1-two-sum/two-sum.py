class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Dictionary = {}       
        for i, num in enumerate(nums):
            compl = target - num
            if compl in Dictionary:
                return [Dictionary[compl], i]
            Dictionary[num] = i
        return []