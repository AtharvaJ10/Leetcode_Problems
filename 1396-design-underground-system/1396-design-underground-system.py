from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.dito={}
        self.place=defaultdict(lambda:[0,0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.dito[id]=[stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        retrieve=self.dito[id]
        self.place[(retrieve[0],stationName)][0]+=t-retrieve[1]
        self.place[(retrieve[0],stationName)][1]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        hold=self.place[(startStation,endStation)]
        return float(hold[0]/hold[1])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)