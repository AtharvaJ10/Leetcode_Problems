class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        leap = lambda y: bool(y % 400 == 0 or y % 4 == 0 and y % 100)
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def f(date):
            y, m, d = map(int, date.split('-'))
            x = 365 * (y - 1971) + sum(map(leap, range(1971, y)))
            return x + d + sum(days[:m-1]) + (m > 2 and leap(y))

        return abs(f(date1) - f(date2))
    
        """from datetime import datetime
           class Solution:
                def daysBetweenDates(self, date1: str, date2: str) -> int:
                    return abs((datetime.strptime(date2, '%Y-%m-%d').date() - datetime.strptime(date1, '%Y-%m-%d').date()).days)"""