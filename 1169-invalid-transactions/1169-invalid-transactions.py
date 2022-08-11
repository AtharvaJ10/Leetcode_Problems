class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hash_map = {}
        for i in transactions:
            name, time, amount, city = i.split(",")
            time = int(time)
            
            if time in hash_map:
                if name in hash_map[time]:
                    hash_map[time][name].add(city)
                else:
                    hash_map[time][name] = set([city])
            else:
                hash_map[time] = {name: set([city])}
        
        invalid = []
        for i in transactions:
            name, time, amount, city = i.split(",")
            time = int(time)
            
            if int(amount)>1000:
                invalid.append(i)
                continue
            
            for j in range(time-60, time+61):
                if j not in hash_map:
                    continue
                if name not in hash_map[j]:
                    continue
                
                if city not in hash_map[j][name] or len(hash_map[j][name])>1:
                    invalid.append(i)
                    break
        return invalid