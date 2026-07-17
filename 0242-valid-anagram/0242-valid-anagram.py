class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ls, lt = list(s), list(t)

        # for el in ls:
        #     if el in lt:
        #         lt.remove(el)

        #     else:
        #         return False

        # return len(lt) == 0

        
        sl, st = list(s), list(t)
        sl.sort()
        st.sort()
        return sl == st