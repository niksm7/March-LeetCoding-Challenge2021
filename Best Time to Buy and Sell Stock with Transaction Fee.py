'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

'''

# GREEDY METHOD

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices) # Get the length of list

        if n < 2: # If there are less than 2 elements then we have to buy and sell on the same day which is not valid as per the question so we return 0

             return 0

    
        ans = 0 # To keep track of the answer

        minimum = prices[0] # Tracking the minimum value starting from the 0th element and comparing this with others

        for i in range(1, n): # for loop is from 1 as we already cosidered 0th element as minimum

            if prices[i] < minimum: # if the current number is less than our current minimum then we assign this number to the minimum variable

                minimum = prices[i]

            elif prices[i] > minimum + fee: # If the number is greater than sum of our current mininum and the transaction fee

                ans += prices[i] - fee - minimum # We add this calculation to our answer

                minimum = prices[i] - fee # we re-assign the minimum
        
        # Finally we return the answer
        return ans