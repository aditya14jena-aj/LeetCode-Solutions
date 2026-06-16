class Solution:
    def processStr(self, s: str) -> str:
        result = ""

        for i in s:
            if i == "*":
                result = result[:-1]
            elif i == "#":
                result += result
            elif i == "%":
                result = result[::-1]
            else:
                result += i

        return result
