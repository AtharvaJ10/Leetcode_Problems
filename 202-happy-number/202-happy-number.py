class Solution:
    def get_num(self,num):
        sum1 = 0
        while num>0:
            rem = num % 10
            sum1+= rem*rem
            num = num//10
        return sum1
    
    
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n!=1 and n not in visited:
            visited.add(n)
            n = self.get_num(n)
        if n==1:
            return True
        else:
            return False