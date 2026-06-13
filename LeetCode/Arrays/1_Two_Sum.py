"""

Problem : 1. Two Sum
Approach : Iterate through every element , For each element, check all remaining elements using a nested loop.
           If the sum of the two elements equals the target, return their indices.
             
"""

nums = list(map(int, input().split()))
target = int(input())

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break
