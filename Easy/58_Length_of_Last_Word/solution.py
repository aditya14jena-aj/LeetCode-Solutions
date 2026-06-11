class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r_l = s.split()
        return len(r_l[-1])
