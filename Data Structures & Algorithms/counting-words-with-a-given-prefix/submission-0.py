class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        for word in words:
            length = len(pref)
            if word[:length] == pref:
                counter += 1

        return counter
        