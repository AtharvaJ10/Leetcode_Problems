class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = {}
        for i in transactions:
            name, time, amount, city = i.split(",")
            time = int(time)
            if time in d:
                if name in d[time]:
                    d[time][name].add(city)
                else:
                    d[time][name] = set([city])
            else:
                d[time] = {name: set([city])}
        
        invalid = []
        for i in transactions:
            name, time, amount, city = i.split(",")
            time = int(time)
            
            if int(amount)>1000:
                invalid.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in d:
                    continue
                if name not in d[j]:
                    continue
                
                if city not in d[j][name] or len(d[j][name])>1:
                    invalid.append(i)
                    break
        return invalid
