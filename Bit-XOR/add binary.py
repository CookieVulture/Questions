# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = int(a,2), int(b,2)
        while num2:
            num1, num2 =  num1 ^ num2, (num1 & num2)<<1
        return bin(num1)[2:]


print(Solution.addBinary(None,"11","1"))
print(Solution.addBinary(None,"1010","1011"))

