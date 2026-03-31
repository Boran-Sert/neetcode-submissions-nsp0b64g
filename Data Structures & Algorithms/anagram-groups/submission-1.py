class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grup = {}
        for kelime in strs:
            key = "".join(sorted(kelime))
            if key not in grup:
                grup[key] = []
                grup[key].append(kelime)
            else:
                grup[key].append(kelime)
        return list(grup.values())