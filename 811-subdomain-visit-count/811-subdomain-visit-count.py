class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for domain in cpdomains:
            count, url = domain.split(" ", 1)
            sub_domain = url.split(".")
            for i in range(len(sub_domain)):
                d[tuple(sub_domain[i:])]+=int(count)
        
        res = []
        for key in d:
            temp = '.'.join(key)
            res.append(str(d[key]) + " "+ temp)
        return res
                       