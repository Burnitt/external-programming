class Solution:
    def isPalindrome(self, x: int) -> bool:
        char = str(x)
        for i in range (int((len(char)/2))):
            if char[i] != char[-i - 1]:
                return False
        return True
