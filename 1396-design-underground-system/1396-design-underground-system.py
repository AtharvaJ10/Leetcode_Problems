class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.routes = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, check_in_time = self.check_in.pop(id)
        route = (start, stationName)
        self.routes[route][0]+=(t - check_in_time)
        self.routes[route][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.routes[route][0]/self.routes[route][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)