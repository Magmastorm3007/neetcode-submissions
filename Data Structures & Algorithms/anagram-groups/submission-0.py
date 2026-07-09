class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp=dict()
        for x in strs:
            key = "".join(sorted(x))
            if key not in mp:
                mp[key] = []
            mp[key].append(x)
        
        result = list(mp.values())
        return result