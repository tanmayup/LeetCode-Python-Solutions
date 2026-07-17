class Solution(object):
    def countDigits(self, num):
        numl = list(str(num))
        while "0" in numl:
            numl.remove("0")
        count = 0
        for digit in numl:
            if num % int(digit) == 0:
                count += 1

        return count