class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.split(" ")

        # while "" in s:
        #     s.remove("")

        # for i in range(len(s) // 2):
        #     temp = s[i]
        #     s[i] = s[len(s) - i - 1]
        #     s[len(s) - i - 1] = temp

        # return " ".join(el for el in s)

        s = s.split()
        s.reverse()

        return " ".join(el for el in s)