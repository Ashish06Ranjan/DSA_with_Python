"""
Problem : 268A. Games
"""
n = int(input())
 
teams = []
 
for _ in range(n):
    h, a = map(int, input().split())
    teams.append((h, a))
 
ans = 0
 
for h1, a1 in teams:
    for h2, a2 in teams:
        if h1 == a2:
            ans += 1
 
print(ans)
