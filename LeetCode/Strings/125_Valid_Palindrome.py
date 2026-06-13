"""

Problem : 125 Valid Palindrome

Approach : Go through the string and store only the alpha and num values , convert into lower , then check with the reverse values 

"""


class Solution(object):
    def isPalindrome(self, s):

        result=""

        for ch in s:
            if ch.isalnum():
                result+=ch
        
        result = result.lower()

        if result==result[::-1]:
            return True
        else:
            return False
        
