def missingNumber(nums):
    # Subtracting from the actual sum we want the sum of the nums
    # Eg: [3,0,1] has sum 4 ------- (1)
    # Actually there should be [0,1,2,3] and their sum would be 6  ------ (2)
    # subtracting (1) from (2) we get 6-4 = 2 which our missing number
    return sum(range(len(nums)+1)) - sum(nums) 

print(missingNumber([9,6,4,2,3,5,7,0,1]))