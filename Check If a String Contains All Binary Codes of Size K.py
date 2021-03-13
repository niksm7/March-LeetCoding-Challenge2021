'''
Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.
'''

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        # Collecting all the unique substrings of size k from the given string s
        x = len(set(s[i:i+k] for i in range(0,(len(s)-k)+1))) 

        # Now there should 2^k possibilities with given size suppose given k is 2 so we can make 00,01,10,11 which is 4 = 2**k = 2**2

        # We return the boolean comparison if length of all the unique substrings we got are equal to the number of possibilities.
 
        return x == 2**k