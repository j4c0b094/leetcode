class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l2 = list(set(nums))
        if len(l2) != len(nums):
            return True
        return False