"""
Problem :  1358A. Park Lighting
Approach : A light can maximum light 2 streets so we will just multiply the input and then divide by 2.
           If the remainder is zero then print the divisor.
           if remainder is non zero then print divisor + 1

"""

n=int(input())
for _ in range (n):
    a,b=map(int,input().split())
 
    if a*b%2==0:
        print(a*b//2)
    else:
        print(a*b//2 + 1)
