class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.helper(s, 0, [], "")
    
    def helper(self, curr, index, res, path):
        if index>4:
            return
        if index==4 and not curr:
            res.append(path[:-1])
            return
        
        for i in range(1, len(curr)+1):
            if (curr[:i]=="0") or (curr[0]!="0" and 0<int(curr[:i])<256):
                self.helper(curr[i:], index+1, res, path+curr[:i]+".")
        return res