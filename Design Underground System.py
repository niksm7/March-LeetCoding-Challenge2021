'''
Implement the UndergroundSystem class:

void checkIn(int id, string stationName, int t)
A customer with a card id equal to id, gets in the station stationName at time t.
A customer can only be checked into one place at a time.
void checkOut(int id, string stationName, int t)
A customer with a card id equal to id, gets out from the station stationName at time t.
double getAverageTime(string startStation, string endStation)
Returns the average time to travel between the startStation and the endStation.
The average time is computed from all the previous traveling from startStation to endStation that happened directly.
Call to getAverageTime is always valid.
You can assume all calls to checkIn and checkOut methods are consistent. If a customer gets in at time t1 at some station, they get out at time t2 with t2 > t1. All events happen in chronological order.

 

Example 1:

Input
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

Output
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
'''

class UndergroundSystem:

    def __init__(self):
        
        ## dictionrary for passenger on-board record
        # key: id
        # value: chech-in station, check-in time pair
        
        self.passenger = defaultdict( tuple )
        
        
        ## dictionary for traffic record
        # key: (startStation, endStation) pair
        # value: a list of traverl time
        
        self.traffic_record = defaultdict( list )
    
    # ---------------------------------------------------------------
    
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        # update check-in station and check-in time pair
        
        self.passenger[id] = (stationName, t)
        
        return

    # ---------------------------------------------------------------
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        # update current traversal into corresponding traffic record
        
        start_station, start_time = self.passenger[id]
        end_station, end_time = stationName, t
        
        self.traffic_record[(start_station, end_station)].append( end_time - start_time )
        
        return
    
    # ---------------------------------------------------------------
    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        # get total traffic time as well as total travel count from traffic record
        
        total_traffic_time = sum( self.traffic_record[(startStation, endStation)] )
        total_travel_count = len( self.traffic_record[(startStation, endStation)] )
        
        
        # compute average travel time
        
        return total_traffic_time / total_travel_count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)