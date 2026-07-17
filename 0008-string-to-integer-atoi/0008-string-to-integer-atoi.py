class Solution:
    def myAtoi(self, s: str) -> int:

        if s == "":
            return 0

        sl = list(s)

        while sl[0] == " " and len(sl) >= 2:
            sl.pop(0)

        if sl == " ":
            return 0

        nums = "0123456789"

        if set(sl).union({"+"}) == {"+"} or set(sl).union({"-"}) == {"-"}:
            return 0

        if sl[0] == "-":
            positive = False

        elif sl[0] == "+" or sl[0] in nums:
            positive = True

        else:
            return 0

        if sl[0] in ["-","+"]:
            sl.pop(0)


        while sl[0] == "0" and len(sl) >= 2:
            sl.pop(0)

        if sl == "0":
            return 0

        if sl[0] not in nums:
            return 0

        num = ""

        for el in sl:
            if el in nums:
                num += el
            else:
                break

        if positive == True:
            if int(num) < (2 ** 31) - 1:
                return int(num)
            else:
                return (2**31 - 1)

        else:
            if int(num) * (-1) > (-1) * (2 ** 31):
                return int(num) * (-1)
            else:
                return (-1) * (2 ** 31)