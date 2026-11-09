class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}

        for el in s:
            if el not in d:
                d[el] = 1
            else:
                d[el] += 1

        for el in t:
            if el not in d or d[el] == 0:
                return False
            else:
                d[el] -= 1

        for el in d:
            if d[el] != 0:
                return False

        return True