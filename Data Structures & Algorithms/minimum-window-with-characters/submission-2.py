class Solution:
    def minWindow(self, s: str, t: str) -> str:
        i = 0 
        j = 0
        min_len = float("inf")

        t_chars = {}
        temp = 0

        while temp < len(t):
            t_chars[t[temp]] = t_chars.get(t[temp], 0) + 1
            temp += 1
        
        len_of_map = len(t_chars)

        while j < len(s):
            if s[j] in t_chars:
                t_chars[s[j]] = t_chars.get(s[j], 0) - 1
                if t_chars[s[j]] == 0:
                    len_of_map -= 1
            
            while len_of_map == 0:
                if (j - i + 1) < min_len:
                    min_len = (j - i + 1)
                    start = i

                if s[i] in t_chars:
                    t_chars[s[i]] = t_chars.get(s[i], 0) + 1
                    if t_chars[s[i]] > 0:
                        len_of_map += 1

                i += 1
            j += 1

        return s[start:start + min_len] if min_len != float("inf") else ""



