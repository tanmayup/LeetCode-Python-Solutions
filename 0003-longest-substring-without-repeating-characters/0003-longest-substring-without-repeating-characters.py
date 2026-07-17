class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = []
        subs = ""

        for i in range(len(s)):
            if s[i] in subs:
                idx = subs.index(s[i])
                sol.append(subs)
                subs = subs[idx+1:]

            subs = subs + s[i]

        sol.append(subs)

        return max([len(i) for i in sol])