"""
Problem : 2126A. Only One Digit
Approach : Convert x to a string.
          Find the smallest digit in the string.
          Print that digit.

"""

t = int(input())

for _ in range(t):
    x = input()
    print(min(x))
