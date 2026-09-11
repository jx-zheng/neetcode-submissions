from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = defaultdict(list)

        for _str in strs:
            sorted_str = str(sorted(_str))
            anagrams_map[sorted_str].append(_str)
        
        ret = []
        for _, anagram_list in anagrams_map.items():
            ret.append(anagram_list)
        
        return ret
