class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = [-1] * 256 

        left = 0
        right = 0
        max_len = 0

        while right < len(s):
            if hash[ord(s[right])] != -1:
                if hash[ord(s[right])] >= left:
                    left = hash[ord(s[right])] + 1
            
            curr_length = right - left + 1
            max_len = max(curr_length, max_len)

            hash[ord(s[right])] = right 
            right = right + 1

        return max_len        