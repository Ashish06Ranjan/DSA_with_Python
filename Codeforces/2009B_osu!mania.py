"""

Problem : 2009B osu!mania
Approach : Store all rows in a list. Reverse the list. Find the position of # in each row. Add 1 because Python indexing starts from 0.

"""

t = int(input())

for _ in range(t):
    n = int(input())
    rows = []
    for i in range(n):
        rows.append(input())
    rows.reverse()
    for row in rows:
        print(row.index("#") + 1, end=" ")
    print()
