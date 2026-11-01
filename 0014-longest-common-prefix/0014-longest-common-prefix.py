class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        ans = strs[0]
        for word in strs:
            if len(word) < len(ans):
                ans = word

        strs.remove(ans)

        for word in strs:
            idx = 0
            for char in word:
                if idx != len(ans) and ans[idx] == char:
                    idx += 1
                else:
                    ans = word[:idx]

        return ans