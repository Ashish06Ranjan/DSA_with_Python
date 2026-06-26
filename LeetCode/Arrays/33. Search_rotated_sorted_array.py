"""
Problem : 33. Search in Rotated Sorted Array
Approach :  Use Binary Search.
            Find the middle element.
            Determine whether the left or right half is sorted.
            Check if the target belongs to that sorted half.
            Move left or right accordingly.
            Return the index if found, otherwise -1.
"""
class Solution(object):
    def search(self, nums, target):
      left=0
      right = len(nums)-1
      while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
          return mid
        if nums[left]<=nums[mid]:
          if nums[left]<= target <nums[mid]:
            right = mid-1
          else:
            left = mid+1
        else:
          if nums[mid]<target<=nums[right]:
            left=mid+1
          else:
            right=mid-1
      return -1
