class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.helper(s, 0, [], "")
    
    def helper(self, s, ind, res, path):
        if ind>4:
            return
        if ind==4 and not s:
            res.append(path[:-1])
            return
        
        for i in range(1, len(s)+1):
            if s[:i]=="0" or (s[0]!="0" and 0<int(s[:i])<256):
                self.helper(s[i:], ind+1, res, path+s[:i]+".")
        return res