"""

Problem :  1154A. Restoring Three Numbers
Approach :  Sort the 4 numbers.
            The largest number is always a + b + c.
            Subtract each of the other three numbers from the largest to get a, b, and c.
            a = largest - x[2]
            b = largest - x[1]
            c = largest - x[0]
            
"""

x = list(map(int, input().split()))

x.sort()

s = x[3]

a = s - x[2]
b = s - x[1]
c = s - x[0]

print(a, b, c)
