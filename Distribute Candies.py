'''Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.'''


def distributeCandies(candyType):
    # Dividing the length of the list by 2 as Alice is allowed to eat only half the candies it has
    n = len(candyType) // 2 

    # Finding the length of unique candies present

    uni = len(set(candyType))

    # if number of candies alice can eat is greater than the total unique candies then Alice can eat all the candies
    if n >= uni:
        return uni
    # Else if number of candies Alice can eat is less than the total unique candies than it only eat those number of candies
    else:
        return n

print(distributeCandies([1,1,2,2,3,3]))