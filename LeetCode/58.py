class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range (-1, -(len(s) + 1), -1):
            if s[i].isalpha():
                count += 1
                if -i == len(s):
                    return count
            elif count > 0:
                return count
