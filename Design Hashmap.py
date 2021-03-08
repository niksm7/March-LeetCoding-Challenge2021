'''
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.

'''

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 100
        self.bucket = [[] for _ in range(self.cap)] # Creating a List filled with empty lists which will act as buckets
    
    def hash_function(self,key): # This function will return the hashed key which will help us in choosing the bucket to which we want to store our key value pair

        return key % self.cap # This very basic way to hash and can cause collision problems but as we are provided the key as integer we have not much options left

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_value = self.hash_function(key) # Getting the bucket value for this particular key

        current_bucket = self.bucket[hash_value] # Getting the bucket from the bucket list
        
        exists = False # This pointer is to see if the key doesn't already exists

        for i in range(len(current_bucket)): # Inside the bucket there can be n number of lists of key value pairs so we iterate through them

            if current_bucket[i][0] == key: # If the ith element's 0 index which will be the key matches with our key that means the key already exists 

                exists = True # Changing it to True

                current_bucket[i][1] = value # Assigning the key with new value

                # As we need no more iterations we simply break the loop

                break
        
        # If our "exists" pointer is still False that means the key doesn't exist and we need to append the key value pair list to that particular bucket

        if not exists: 
            self.bucket[hash_value].append([key,value])
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_value = self.hash_function(key) # Getting the bucket value for this particular key

        current_bucket = self.bucket[hash_value] # Getting the bucket from the bucket list
        
        for i in range(len(current_bucket)):# Inside the bucket there can be n number of lists of key value pairs so we iterate through them

            if current_bucket[i][0] == key: # If we get a match for our key 

                return current_bucket[i][1] # we return the value

        # If we haven't returned till here that means the key does not exists
        # so we return -1
      
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_value = self.hash_function(key) # Getting the bucket value for this particular key

        current_bucket = self.bucket[hash_value] # Getting the bucket from the bucket list
        
        for i in range(len(current_bucket)):# Inside the bucket there can be n number of lists of key value pairs so we iterate through them

            if current_bucket[i][0] == key: # If we get the key matched

                current_bucket.pop(i) # Then we remove that particular sub-list consisting of key value pair

                # As no more iterations are needed we break the loop
                
                break