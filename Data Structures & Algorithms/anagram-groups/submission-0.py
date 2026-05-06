class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for item in strs:
            sorted_string = ''.join(sorted(item))
            if sorted_string not in map:
                map[sorted_string] = []
            map[sorted_string].append(item)

        return list(map.values())