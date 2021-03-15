'''
Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
'''

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Use OrderedDict to get smaller keys up front
        dp = OrderedDict()
        for a in sorted(arr):
            total = 1  # The tree with the number itself
            for b in dp:
                div, mod = divmod(a, b)
                if b > div:
                    # Break early when sqrt reached
                    break
                elif mod == 0:
                    # Multiple by 1 if the two children nodes are the same
                    total += dp[b] * dp.get(div, 0) * (1 if b == div else 2)
            dp[a] = total
        return sum(dp.values()) % (10 ** 9 + 7)