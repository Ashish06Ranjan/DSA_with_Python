"""
Problem : 1399A. Remove Smallest
Approach :  Sort the array.Check adjacent elements.
            If any adjacent difference is greater than 1, then it's impossible to remove all elements and end with one element → print "NO".
            Otherwise, print "YES".
"""

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    possible = True

    for i in range(n - 1):
        if a[i + 1] - a[i] > 1:
            possible = False
            break

    if possible:
        print("YES")
    else:
        print("NO")
