class Solution:
    def firstUniqChar(self, s: str) -> int:
        # for el in s:
        #     if s.count(el) == 1:
        #         return list(s).index(el)

        # return -1

        freq = {}
        for el in s:
            if el not in freq:
                freq[el] = 1
            
            else:
                freq[el] += 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1