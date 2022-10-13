class UndergroundSystem:

    def __init__(self):
        self.checkIn_Map ={}
        self.travelHistory_map ={}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIn_Map[id] = [stationName , t ]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkIn_Map :
            startStation, startTime = self.checkIn_Map[id]
            self.travelHistory(startStation,startTime, stationName,t )
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = endStation + "-" + startStation
        if key in self.travelHistory_map:
            history = self.travelHistory_map[key]
            return sum(history)/len(history)
            
            
        
    def travelHistory(self,startStation, startTime, endStation, endTime):
        key = endStation + "-" + startStation
        if key not in self.travelHistory_map:
            self.travelHistory_map[key] = [endTime - startTime]
        else:
            self.travelHistory_map[key].append(endTime - startTime)
        

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)