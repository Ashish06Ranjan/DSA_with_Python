"""
Problem : 49. Group Anagrams
Approach : Create an empty dictionary to store groups of anagrams. Traverse each word in the given list.
          Sort the characters of the word to create a unique key. If the key is not present in the dictionary, create a new empty list for it.
          Append the original word to the list corresponding to that key. After processing all words, return all the dictionary values as the final groups.

"""

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
