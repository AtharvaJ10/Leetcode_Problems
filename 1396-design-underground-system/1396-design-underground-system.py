from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.check = {}
        self.result=defaultdict(lambda:[0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checked_in = self.check.pop(id)
        route = (checked_in[0], stationName)
        self.result[route][0]+=t-checked_in[1]
        self.result[route][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.result[route][0]/self.result[route][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)