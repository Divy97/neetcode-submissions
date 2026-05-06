class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0 
        j = 0 

        count_map = {}
        max_freq = 0

        result = 0

        while j < len(s):
            count_map[s[j]] = count_map.get(s[j], 0) + 1
            max_freq = max(max_freq, count_map[s[j]])

            while (j - i + 1) - max_freq > k: 
                count_map[s[i]] -= 1
                i += 1
            
            result = max(result, (j - i + 1))
            j += 1
        return result



            