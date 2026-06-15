"""

Problem : 1472A Cards for Friends
Approach : Start with 1 sheet.Keep dividing w by 2 while it is even. Each division doubles the number of sheets.Do the same for h.
          After all possible cuts, compare the total number of sheets with n. If sheets >= n → print "YES"
          Otherwise → print "NO"

"""

n = int(input())

for _ in range(n):
    a,b,c = map(int, input().split())

    pieces = 1

    while a % 2 == 0:
        a = a // 2
        pieces = pieces * 2

    while b % 2 == 0:
        b = b // 2
        pieces = pieces * 2

    if pieces >= c:
        print("YES")
    else:
        print("NO")
