'''
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

 

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
'''

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda key:(key[0], -key[1]))
        tails = []
        for i in range(0, len(envelopes)):
            idx = bisect.bisect_right(tails, envelopes[i][1])
            if idx - 1 >= 0 and tails[idx - 1] == envelopes[i][1]:
                continue
            if idx == len(tails):
                tails.append(envelopes[i][1])
            else:
                tails[idx] = envelopes[i][1]
        return len(tails)