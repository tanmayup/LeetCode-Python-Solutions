class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # s = 0
        # for i in range(1, num):
        #     if num % i == 0:
        #         s += i

        # return s == num

        s = 1
        i = 2

        if num == 1:
            return False

        while i*i < num:
            if num % i == 0:
                s += i

                if i != num // i:
                    s += num // i
            
            i += 1

        return s == num