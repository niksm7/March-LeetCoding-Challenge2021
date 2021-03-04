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
            nums.remove(i) # remove the extra number from the list
            lst.append(i)
            break

    lst.append(sum(range(n+1)) - sum(nums)) # We subtract the sum of nums from the sum we want which gives us the number that is missing

    #Finally return the lst with 2 numbers    
    return lst

print(findErrorNums([1,2,2,4]))