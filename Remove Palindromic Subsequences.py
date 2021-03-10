'''
Given a string s consisting only of letters 'a' and 'b'. In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string, if it is generated by deleting some characters of a given string without changing its order.

A string is called palindrome if is one that reads the same backward as well as forward.

Example:

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "". 
Remove palindromic subsequence "a" then "bb".

'''
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == "": # If the string provided is empty we simply return 0
            
            return 0

        elif s == s[::-1]: # If the complete string is palindrome then we return 1

            return 1

        else: # else there can only be 2 letters according to the question so atmost it will take 2 steps like removing all a's in first round and removing all b's in second.

            return 2