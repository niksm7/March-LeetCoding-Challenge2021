'''
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]

'''

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:

        # Make a list of all words in lower case
        wordlist2 = [i.lower() for i in wordlist]

        # Make other list of words where the vowels are replaced by 1 and the words are in lower case only
        wordlist3 = [re.sub(r'[aeiouAEIOU]', '1', i )for i in wordlist2]

        # In this list we will append our final values
        lst = []

        for i in queries: # Iterating through each word

            # If the word is as it is in the wordlist we append the word
            if i in wordlist:
                lst.append(i)
            
            # If the word is present in the wordlist if we ignore character case then we return the first matching character

            elif i.lower() in wordlist2:
                lst.append(wordlist[wordlist2.index(i.lower())])
            
            # If after replacing vowels with 1 we find that the number is present in our wordlist3 we return the first matching word from our main wordlist

            elif re.sub(r'[aeiou]', '1', i.lower()) in wordlist3:
                lst.append(wordlist[wordlist3.index(re.sub(r'[aeiou]', '1', i.lower()))])
            
            # Else we simply append empty string
            else:
                lst.append("")
        
        # Finally we return the string
        return lst