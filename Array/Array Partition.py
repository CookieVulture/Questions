"""
561. Array Partition I
Easy

744

2298

Add to List

Share
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].

"""

# My solution

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum1 = 0
        i = 0
        while i<len(nums):
            num1 = nums[i]
            num2 = nums[i+1]
            sum1 += min(num1, num2)
            i+=2
        return sum1

# Optimal Solution


class Solution2(object):

    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
