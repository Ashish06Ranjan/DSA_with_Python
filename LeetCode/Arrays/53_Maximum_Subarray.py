"""
Problem : 53. Maximum Subarray
Approach : Kadane's Algorithm
          Initialize current_sum and max_sum with the first element.
          Traverse the array from the second element onwards.
          If current_sum becomes negative, start a new subarray from the current element.
          Otherwise, add the current element to current_sum.
          Update max_sum whenever current_sum becomes larger.
          After traversing the entire array, return max_sum.

"""
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum = current_sum + nums[i]

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum
