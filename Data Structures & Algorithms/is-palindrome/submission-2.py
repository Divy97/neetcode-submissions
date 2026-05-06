class Solution:
    def isPalindrome(self, s: str) -> bool:
        validate = []
        for char in s:
            if char.isalnum():
                validate.append(char.lower())

        for i in range(len(validate) // 2):
            if(validate[i] != validate[len(validate) - i - 1]):
                return False
        return True