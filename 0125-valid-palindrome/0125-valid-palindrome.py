class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph = "abcdefghijklmnopqrstuvwxyz0123456789"

        cleared = ""
        for char in s:
            if char.lower() in alph:
                cleared += char

        cleared = cleared.lower()

        rev = ""
        for i in range(1, len(cleared) + 1):
            rev += cleared[(-1) * i]

        if rev == cleared:
            return True
        
        else:
            return False