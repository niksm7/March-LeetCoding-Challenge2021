'''
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.

 

Example 1:

Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
Output: ["facebook","google","leetcode"]

'''

from itertools import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        # create a Counter Instance where letter will be the key and their count in the string will be their values
        
        cnt = Counter()

        # Iterate through all the strings in the list B

        for b in B:

            # Now we perform merge and update of the dictionaries for example:
            # >>> c1 = ct.Counter({2: 2, 3: 3})
            # >>> c2 = ct.Counter({1: 1, 3: 5})
            # >>> c1 |= c2
            # >>> c1 = Counter({2: 2, 3: 5, 1: 1})

            cnt |= Counter(b)

        # Return those words which match the criteria
        #   
        return [a for a in A if not cnt - Counter(a)]