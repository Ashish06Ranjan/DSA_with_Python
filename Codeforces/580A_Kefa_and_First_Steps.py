"""
Problem : 580A. Kefa and First Steps
Approach : Keep track of the current non-decreasing subarray length using curr.
          Traverse the array from left to right.
          If a[i] >= a[i-1], extend the current subarray (curr += 1).
          Otherwise, start a new subarray (curr = 1).
          Maintain the maximum length found so far in ans.
          Print ans at the end.

"""
n = int(input())
a = list(map(int, input().split()))

curr = 1
ans = 1

for i in range(1, n):
    if a[i] >= a[i - 1]:
        curr += 1
    else:
        curr = 1

    ans = max(ans, curr)

print(ans)
