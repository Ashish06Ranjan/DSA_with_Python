"""
Problem : 56. Merge Intervals
Approach : Sort all intervals. Create an empty result list.
            If the current interval overlaps with the last interval in the result, merge them.
            Otherwise, add the current interval to the result. Print the final merged intervals.
"""
class Solution(object):
    def merge(self, intervals):

        intervals.sort()

        result = []

        for interval in intervals:

            if result == []:
                result.append(interval)

            elif interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])

            else:
                result.append(interval)

        return result
