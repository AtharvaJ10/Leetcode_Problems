class Solution:
    def numberToWords(self, num: int) -> str:
        till19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split(" ")
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split(" ")
        bigs = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand"}
        
        def word(n):
            if n<20:
                return till19[n-1:n]
            elif n<100:
                return [tens[n//10-2]] + word(n%10)
            elif n<1000:
                return [till19[n//100-1]] + ['Hundred'] + word(n%100)
            else:
                for i in [1000000000, 1000000, 1000]:
                    if n//i>0:
                        return word(n//i) + [bigs[i]] + word(n%i)
        return ' '.join(word(num)) if num else 'Zero'