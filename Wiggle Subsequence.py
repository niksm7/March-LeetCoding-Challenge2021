'''
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

 

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len( nums )
        
        # length of wiggle sequence, ending in positive difference, negative difference
        positive, negative = 1, 1
        
        
        # scan from secnond number to last number
        for i in range(1, n):
        
            if nums[i] > nums[i-1]:
                
                # difference is positive, concatenated with negative prefix wiggle subsequence
                positive = negative + 1
                
            elif nums[i] < nums[i-1]:
                
                # differnce is negative, concatenated with positive prefix wiggle subsequence
                negative = positive + 1
                
        # compute the longest length of wiggle sequence                
        return max(positive, negative) 