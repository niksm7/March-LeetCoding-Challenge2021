'''
Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
'''

class Solution:
    def advantageCount(self, A, B):
        # Getting the length of first list
        n = len(A) 

        # Now we reverse sort the list of tuples of index and the number in list B
        B = sorted([(num, i) for i, num in enumerate(B)],reverse=True)

        # Also we reverse sort the A list 
        A = sorted(A,reverse=True)

        # Now we a create a ans list which will be filled with all -1 and have a length equal to the lenght of A

        ans = [-1]*n
        
        # We keep two pointers so that we can iterate from both sides of the list
        beg, end = 0, n - 1
        

        for num, ind in B:

            # if the number at first pointer is greater than the current number then 
            if A[beg] > num:

                # Save the number of the begining index and move the beg pointer forward by 1
                ans[ind] = A[beg]
                beg += 1
    
            else:
                # Save the number of the end index and move the end pointer backward by 1
                ans[ind] = A[end]
                end -= 1

        #return the ans list  
        return ans
        