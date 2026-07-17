# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         result = []
#         for i in range(len(candies)):
#             candies[i] += extraCandies
#             print(candies)
#             if max(candies) == candies[i]:
#                 result.append(True)
#             else:
#                 result.append(False)

#             candies[i] -= extraCandies

#         return result

# class Solution:
#     def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
#         result = []
#         for candy in candies:
#             if candy + extraCandies >= max(candies):
#                 result.append(True)
#             else:
#                 result.append(False)

#         return result

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        return [candy + extraCandies >= max(candies) for candy in candies]