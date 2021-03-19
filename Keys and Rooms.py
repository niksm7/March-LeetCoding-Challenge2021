'''
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:

Input: [[1],[2],[3],[]]
Output: true
'''
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        stack = [0] # for rooms that we need to visit and we start from room [0]
        
        while stack: # Untill stack is not empty

            room = stack.pop() # We collec the last sub list of our stack

            visited_rooms.add(room) # We consider that room as visited

            for key in rooms[room]: 

                if key not in visited_rooms: # If the room is not visited

                    stack.append(key) # Add it to our stack so that we visit it now

        return len(visited_rooms) == len(rooms) # check if the all the rooms that were present have been visited