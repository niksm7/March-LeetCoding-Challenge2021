'''
A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
'''

# Basically you have to join words using "#" but only words which are not suffixes of some word like "me" is a suffix of "time" so we don't consider "me" while merging the words in final string
 
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:

        n = len(words) # Get the length of words

        unique_words = set(words) # We create a set so that we only take unique values
        
        for word in words: # Iterate over words

            m = len(word) # get hold of the length of each word that we encounter
            
            # Now we check for all possible suffixes of this word and remove the suffixes which are present in the set

            for j in range(1,m): # This loop will iterate from the 1st letter of the word because the suffix cannot be the whole word.

                if word[j:] in unique_words: # We check if this particular suffix is present in the set and if it is

                    unique_words.remove(word[j:]) # we remove that suffix

        return len("#".join([i for i in unique_words])+"#") # Finally we join all the words with "#" and append a "#" at the end and return the length of this string
    
'''
Example explanation : When we have word = time
m = 4
j will go from 1 to 3
now during this we encounter when j = 2
word[j:] = "time"[2:] = "me" 
And this "me" is present in the set of words we have so we simply remove it.
'''
