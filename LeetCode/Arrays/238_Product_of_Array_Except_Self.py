"""

Problem : 238. Product of Array Except Self
Approach : Store the product of all elements to the left of each index.
            Traverse from right to left and multiply by the product of all elements to the right.
            The resulting array contains the product of all elements except itself.

"""
class Solution(object):
    def productExceptSelf(self, nums):

        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
