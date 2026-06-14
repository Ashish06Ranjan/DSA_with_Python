"""

Problem : 1283A Minutes Before the New Year
Approach : take the input and then calculate the minute using the formula and then subtract from total minutes 

"""
t = int(input())

for _ in range(t):
    h, m = map(int, input().split())

    minutes = h * 60 + m
    print(1440 - minutes)
