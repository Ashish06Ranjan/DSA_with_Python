"""
Problem : 383. Ransom Note
Approach :  Traverse each character in the ransomNote.
            For every character:
              Check if it is present in magazine.
              If it is present, remove only one occurrence of that character from magazine because each letter can only be used once.
              If it is not present, immediately return False because we cannot construct the ransom note.
            If all characters of ransomNote are found and removed successfully, return True.

"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
      for ch in RansomNote:
        if ch in magazine :
          magazine = magazine.replace(ch,"",1)
        else:
          return False
      return True 
