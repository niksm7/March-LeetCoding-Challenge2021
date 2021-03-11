'''
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"

'''
class Solution:
    def intToRoman(self, num: int) -> str:

        # We make a dictionary to refer all the possible unique roman numbers and their respective numericals

        dct = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        # This stack with only unique numericals will be used to compare with given number 
        stack = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

        # This list will hold all the roman numbers
        ans = []

        # Until our given number is not reduced to 0 we run this while loop
        while num > 0: 

            # Each time we check if last element of the stack is greater than given number and if so we pop it
            if stack[-1] > num:
                stack.pop()
            
            # Else we subtract that number from given number
            else:
                num -= stack[-1] 

                # And append its respective roman number to the ans list
                ans.append(dct[stack[-1]])

        # Finally we format the list to string using join and return the string
        return "".join(map(str, ans))