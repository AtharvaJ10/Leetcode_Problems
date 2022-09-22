class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, start: int, end: int) -> bool:
        right = len(self.calender)
        if right==0:
            self.calender.append([start,end])
            return True
        
        left = 0
        while left<right:
            mid = (left+right)//2
            if self.calender[mid][1]<=start:
                left = mid+1
            else:
                right = mid
        
        if left==len(self.calender):
            self.calender.append([start,end])
            return True
        if self.calender[left][0]>=end:
            self.calender.insert(left, [start,end])
            return True
        return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)