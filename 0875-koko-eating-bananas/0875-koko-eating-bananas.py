# class Solution(object):
#     def minEatingSpeed(self, piles, h):
#         possk = 1
#         k = []

#         while len(k) == 0:
#             hours = 0
#             for el in piles:
#                 while el != 0:
#                     if el < possk:
#                         el = 0
#                         hours += 1
#                     elif el >= possk:
#                         el -= possk
#                         hours += 1
#             if hours != h:
#                 possk += 1
#             elif hours == h:
#                 k.append(possk)

#         return k[0]


# class Solution(object):
#     def minEatingSpeed(self, piles, h):
#         possk = 1

#         while True:
#             hours = 0

#             for el in piles:
#                 hours += el // possk
#                 if el % possk != 0:
#                     hours += 1

#             if hours > h:
#                 possk += 1
#             else:
#                 return possk
    
class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        ans = right

        while left < right:
            mid = (left + right) // 2
            time = 0

            for p in piles:
                if p / mid == p // mid:
                    time += p // mid
                else:
                    time += (p // mid) + 1

            if time <= h:
                ans = mid
                right = mid
            else:
                left = mid + 1

        return ans