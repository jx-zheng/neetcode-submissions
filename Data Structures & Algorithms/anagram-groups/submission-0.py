from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for _str in strs:
            anagram_map[''.join(sorted(_str))].append(_str)
        
        anagram_lists = [words for _, words in anagram_map.items()]

        return anagram_lists