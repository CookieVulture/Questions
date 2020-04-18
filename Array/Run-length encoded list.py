'''

1313. Decompress Run-Length Encoded List
Easy

125

391

Add to List

Share
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements with value val concatenated in a sublist. Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.



Example 1:

Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].
'''

# My solution


class Solution:

    def decompressRLElist(self, nums):
        ls = []
        total = len(nums)
        i=0
        while i<total:
            freq = int(nums[i])
            val = int(nums[i+1])
            for j in range(freq):
                ls.append(val)
            i+=2
        return ls

# Optimal Solution

    def decompressRLElist2(self, nums):
        ans = []
        for i in range(0, len(nums), 2):
            for _ in range(nums[i]):
                ans.append(nums[i + 1])
        return ans
