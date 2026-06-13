"""
Problem :  13. Roman to Integer 
Approach : Store the value of each Roman numeral in a dictionary. Traverse the string from left to right.
            If the current numeral is smaller than the next numeral, subtract its value; otherwise, add it.
            Add the value of the last numeral and return the result.

"""
class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I': 1,'V': 5,'X': 10,'L': 50,
            'C': 100,'D': 500,'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]

        total += roman[s[-1]]
        return total
