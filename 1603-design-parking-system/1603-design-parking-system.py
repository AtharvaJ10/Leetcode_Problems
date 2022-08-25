class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.d = defaultdict(int)
        self.d[1]+=big
        self.d[2]+=medium
        self.d[3]+=small

    def addCar(self, carType: int) -> bool:
        if self.d[carType]:
            self.d[carType]-=1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)