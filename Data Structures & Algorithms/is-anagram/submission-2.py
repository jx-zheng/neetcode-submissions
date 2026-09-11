from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = Counter(s)
        t_counter = Counter(t)

        for (letter, count) in s_counter.items():
            if t_counter[letter] != count:
                return False

        return True