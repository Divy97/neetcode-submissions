class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False 
        
        char_s = {}
        for char in s:
            if char in char_s:
                char_s[char] += 1
            else:
                char_s[char] = 1
        
        for char in t:
            if char not in char_s or char_s[char] == 0:
                return False 
            char_s[char] -= 1

        return True
        