'''
1365. How Many Numbers Are Smaller Than the Current Number
Easy

335

10

Add to List

Share
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.



Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation:
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1).
For nums[3]=2 there exist one smaller number than it (1).
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
'''

# My solution


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        dic = {}
        for i in range(101):
            ele = 0
            for j in nums:
                if j<i:
                    ele+=1
            dic[i] = ele
        ls = []
        for k in range(len(nums)):
            ls.append(dic.get(nums[k]))
        return ls

# Optimal Solution


class Solution2:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 102
        for num in nums:
            count[num+1] += 1
        for i in range(1, 102):
            count[i] += count[i-1]
        return [count[num] for num in nums]
