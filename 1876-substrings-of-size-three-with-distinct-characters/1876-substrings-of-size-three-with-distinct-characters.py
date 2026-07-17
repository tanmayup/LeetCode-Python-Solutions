class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-3+1):
            # if len(list(set(ls[i:i+3]))) == 3:
            #     count += 1
            
            if (s[i] != s[i+1]) and (s[i+1] != s[i+2]) and (s[i+2] != s[i]):
                count += 1

        return count