class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        res = 0
        for word in words:
            word_count = Counter(word)
            for c in word_count:
                if word_count[c]>char_count[c]:
                    break
            else:
                res+=len(word)
        return res