'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        @lru_cache(None)
        def ispalindrome(i, j):
            if i >= j: return True
            return s[i] == s[j] and ispalindrome(i+1, j-1)

        return sum(ispalindrome(i, j) for i in range(len(s)) for j in range(i, len(s)))