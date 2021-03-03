'''You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.'''


def findErrorNums(nums):
    # Find the length of nums
    n = len(nums) 

    lst = [] # This list will be returned at the end

    # Maintaning a dictionary to check if number appears twice
    dct = {}

    for i in nums:

        if i not in dct: # If the number is not in dictionary then add it 
            dct[i] = 1

        else: # If the number is already in the dictionary that means the number has appeared more than once so append it to our list and break the loop
            lst.append(i)
            break

    # this for loop is to find the missing number    
    for i in range(1, n+1):

        # If a particular number is not present in nums then append it to our list and break the loop
        if i not in nums:
            lst.append(i)
            break

    #Finally return the lst with 2 numbers    
    return lst

print(findErrorNums([1,2,2,4]))