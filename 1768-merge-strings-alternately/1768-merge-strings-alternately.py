class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined = []
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            combined.append(word1[i])
            combined.append(word2[i])
            
        combined.append(word1[min_len:])
        combined.append(word2[min_len:])
        
        return "".join(combined)