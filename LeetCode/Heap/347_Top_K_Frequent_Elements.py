"""
Problem : 347. Top K Frequent Elements
Approach : Create a hash map to count the frequency of each element. Use a heap (nlargest) to get the k elements with the highest frequencies.
            Return those elements.

"""

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        return heapq.nlargest(k, count, key=count.get)
