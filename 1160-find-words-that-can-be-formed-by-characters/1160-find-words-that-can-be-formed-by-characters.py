class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        res = 0
        for i in words:
            word_count = Counter(i)
            for j in word_count:
                if word_count[j]>chars_count[j]:
                    break
            else:
                res+=len(i)
        return res