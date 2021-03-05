''' Write a program to find the node at which the intersection of two singly linked lists begins.

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''

def getIntersectionNode(headA, headB):
    
    if not headA or not headB: # if there is nothing in headA or headB i.e if they are empty then simply return None
        
        return None
    
    dct = {} # We create a dictionary to store all the possible sub linked lists of A
    
    while headA: # Run this loop until headA is not equal to None

        dct[headA] = 1 # Keep on storing the value of sub linked list of A in the dictionary

        headA = headA.next # Move the head one step ahead
    
    while headB: # Run this loop until headB is not equal to None

        if headB in dct: # If a sub linked list of B is present in the dictionary then we return that because that will be the intersection point of the two linked lists

            return headB

        headB = headB.next # Move the head one step ahead
    

