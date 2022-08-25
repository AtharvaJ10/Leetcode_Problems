class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = [1 for i in range(len(ratings))]
        n = len(ratings)
        
        for i in range(n-1):
            if ratings[i+1]>ratings[i]:
                res[i+1] = max(1+res[i], res[i+1])
        
        for i in range(n-2,-1,-1):
            if ratings[i+1]<ratings[i]:
                res[i] = max(1+res[i+1], res[i])
        return sum(res)
        
        """up = 1
        down = 0
        rat = 1
        peak = 0

        for i in range(1,len(ratings)):

            if ratings[i]>ratings[i-1]:
                up+=1
                down =  0
                rat+=up
                peak = up

            elif ratings[i]==ratings[i-1]:
                down = 0
                peak = 0
                up = 1
                rat+=1

            else:
                down+=1
                up = 1
                rat+=down
                if peak<=down:
                    rat+=1

        return rat"""