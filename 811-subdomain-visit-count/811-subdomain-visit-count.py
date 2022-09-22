class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for domain in cpdomains:
            count, subDomain = domain.split(" ", 1)
            temp = subDomain.split(".")
            for i in range(len(temp)):
                d[tuple(temp[i:])]+=int(count)
        
        res = []
        for i in d:
            res.append(str(d[i])+" "+ ".".join(i))
        return res