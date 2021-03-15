'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # record for first kth node, last kth node, and running cursor
        first_k, last_k, cur = None, None, head
        
        
        # Step #1: locate first_k to corresponding position
        for _ in range(k-1):
            cur = cur.next
        
        first_k = cur
        
        # Step #2: locate last_k to corresponding position
        last_k, cur = head, cur.next

        
        while cur:
            cur, last_k = cur.next, last_k.next
        
        # Step #3: swap value between first kth node and last kth node
        first_k.val, last_k.val = last_k.val, first_k.val
        
        return head