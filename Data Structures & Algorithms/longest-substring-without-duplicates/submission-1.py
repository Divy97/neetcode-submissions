class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        j = 0 

        unique_chars = {}
        max_len = 0

        while j < len(s):
            unique_chars[s[j]] = unique_chars.get(s[j], 0) + 1

            while len(unique_chars) < (j - i + 1):
                unique_chars[s[i]] -= 1
                if unique_chars[s[i]] == 0:
                    del unique_chars[s[i]]
                i += 1
            else:
                max_len = max(max_len, (j - i + 1))
            
            j +=1
        return max_len

