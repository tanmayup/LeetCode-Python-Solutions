class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         def checkAnagrams(s, t):
#             sl = list(s)
#             sl.sort()
#             tl = list(t)
#             tl.sort()

#             return sl == tl

#         ans = []

#         for i in range(len(strs)):
#             ans.append([strs[i]])

#         for i in range(len(strs)):
#             for j in range(i+1, len(strs)):
#                 if checkAnagrams(strs[i], strs[j]):
#                     ans[i].append(strs[j])

#         for i in range(len(ans)):
#             if len(list(set(ans[i]))) == 1 and len(ans[i]) != strs.count(ans[i][0]):
#                 ans[i] = list(set(ans[i]))

#         for i in range(len(ans)):
#             for j in range(i + 1, len(ans)):
#                 if set(ans[i]).union(set(ans[j])) == (set(ans[i]) or set(ans[j])):
#                     li = len(ans[i])
#                     lj = len(ans[j])
#                     if li > lj:
#                         ans[j] = []
#                     else:
#                         ans[i] = []

#         while [] in ans:
#             ans.remove([])


#         return ans

        sl = ["".join(sorted(el)) for el in strs]
        combined = list(zip(strs, sl))

        sol = {}

        for i in range(len(combined)):
            if combined[i][1] in sol:
                sol[combined[i][1]].append(combined[i][0])

            else:
                sol[combined[i][1]] = [combined[i][0]]

        return [sol[el] for el in sol]