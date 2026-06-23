"""
Problem : 704. Binary Search
Approach :  Take two pointers: left and right.
            Find the middle element.
            If middle equals target, return its index.
            If target is larger, search the right half.
            If target is smaller, search the left half.
            If the target is never found, return -1.
"""

class Solution(object):
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1
