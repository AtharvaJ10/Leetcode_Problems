class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==" ":
            return 1
        
        set1 = set()
        i,j = 0,0
        length,max1 = 0,0
        while i<len(s):
            if j>=len(s):
                break
            
            if s[j] not in set1:
                set1.add(s[j])
                length+=1
                j+=1
            
            else:
                if s[i] in set1:
                    if max1<length:
                        max1 = length
                    length = 0
                    i+=1
                    j = i
                    set1 = set()
        if max1<length:
            max1 = length
        return max1