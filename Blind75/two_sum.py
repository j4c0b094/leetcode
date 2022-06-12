class Solution:
    """
    PS: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    https://leetcode.com/problems/two-sum/
    """
    # Brute Force  -- TC : O(n^2) due to double nested for loops to n
    def twoSumBF(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return i, j
    
    # Hashtable -- TC : O(n) single for loop pass and hashmap ops are O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i