'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''

class Codec:

    def __init__(self): 
        self.lookup = [] # List that will hold all the longUrls

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = len(self.lookup) # getting the lenght will basically give us the index to which the new longurl will be appended

        self.lookup.append(longUrl) # Append the long url to the list

        return "http://tinyurl.com/" + str(n) # return the concatenated string
    
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        s = int(shortUrl.split('/')[-1]) # getting the last part of the url which will be the index of the longurl in our list

        return self.lookup[s] # get the longurl at that index
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))