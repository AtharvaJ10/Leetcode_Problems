class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0 for i in range(10)]
        for i in range(len(s)):
            if s[i]=='z':
                count[0]+=1
            elif s[i]=='w':
                count[2]+=1
            elif s[i]=='u':
                count[4]+=1
            elif s[i]=='x':
                count[6]+=1
            elif s[i]=='g':
                count[8]+=1
            elif s[i]=='o': #1-2-4
                count[1]+=1
            elif s[i]=='h': #3-8
                count[3]+=1
            elif s[i]=='f': #4-5
                count[5]+=1
            elif s[i]=='s': #6-7
                count[7]+=1
            elif s[i]=='i':
                count[9]+=1 #7-9
            
        count[1]-=count[2]+count[4]+count[0]
        count[3]-=count[8]
        count[5]-=count[4]
        count[7]-=count[6]
        count[9] -= count[5]+count[6]+count[8]
        
        print(count)
        return ''.join(str(i)*count[i] for i in range(len(count)) if count[i]!=0)