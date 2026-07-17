class Solution(object):
    def hammingWeight(self, n):
        rem = []

        while n != 0:
            rem.append(n % 2)
            n //= 2
        
        rem.reverse()

        return rem.count(1)