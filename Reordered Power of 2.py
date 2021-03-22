'''
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
'''

from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:

        # Check if the given number itself is the power of 2

        if N and (not(N & (N - 1))): # The logical and of the number and bitwise and of number and its previous number gives us the boolean value for power of 2

            return True

        #Else we get all the permutations tuples of the given number but not starting with 0

        q = [''.join(tups) for tups in permutations([i for i in str(N)]) if tups[0] != "0"] 

        # We iterate through each of the tuple values to check if any of them matches the power of 2 value and return True
        for i in q:
            if int(i) and (not(int(i) & (int(i) - 1))):
                return True
        
        # If nothing is returned we return False
        return False