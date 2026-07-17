
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)

        for i in range(1, n + 1):
            arr[i] = arr[i >> 1] + (i & 1)

        return arr
    
    
#         arr = [0] * (n+1)
#         for i in range(n+1):
#             ic = i
#             while i > 0:
#                 if i % 2 == 1:
#                     arr[ic] += 1
#                 i = i // 2

#         return arr