"""
53. Maximum Subarray
Easy

6996

318

Add to List

Share
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

# My approach


class Solution:
    def maxSubArray(self, nums):
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1,len(nums)):
            curSum = max(curSum + nums[i], nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum


# Optimal Solution

class Solution1:
    def maxSubArray(self, nums):
        if not nums:
            return 0
        _sum = 0
        min_sum = 0
        best_sum = float('-inf')
        for x in nums:
            _sum += x
            if (_sum-min_sum)>best_sum:
                best_sum = _sum-min_sum
            if _sum<min_sum:
                min_sum  = _sum

        return best_sum
