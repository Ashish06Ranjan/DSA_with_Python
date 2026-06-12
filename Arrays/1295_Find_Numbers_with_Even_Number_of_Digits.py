"""
Problem: 1295. Find Numbers with Even Number of Digits

Approach:
Count the digits of each number and check if the count is even.

"""

class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1

        return count
