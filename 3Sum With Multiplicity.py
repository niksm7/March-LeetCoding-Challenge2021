'''
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
'''

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        n = len(arr)
        level2 = collections.defaultdict(int) # Making a defualt dictionary with integer values

        for i in range(2, n):
            for j in range(i-1):
                
                # Incrementing the value in dictionary

                level2[arr[j] + arr[i-1]] += 1
            
            # Add the value to the answer

            ans = ans + level2[target - arr[i]]

            #As answer can be big so taking the % of 10**9 + 7

            ans = ans % (10**9 + 7)
        
        return ans