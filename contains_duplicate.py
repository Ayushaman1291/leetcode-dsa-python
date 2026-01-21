# LeetCode Easy — Daily Practice
# Contains Duplicate

class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
