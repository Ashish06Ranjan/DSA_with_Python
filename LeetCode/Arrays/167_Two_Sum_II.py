"""
Problem : 167. Two Sum II - Input Array Is Sorted
Approach :  Place one pointer at the beginning and one at the end of the sorted array.
            Calculate their sum.
            If the sum is equal to the target, return the indices.
            If the sum is smaller than the target, move the left pointer right.
            If the sum is greater than the target, move the right pointer left.
            Repeat until the pair is found.
"""

class Solution(object):
    def twoSum(self, numbers, target):
        
        left = 0
        right = len(numbers) - 1

        while left < right:

            s = numbers[left] + numbers[right]

            if s == target:
                return [left + 1, right + 1]

            elif s < target:
                left += 1

            else:
                right -= 1
