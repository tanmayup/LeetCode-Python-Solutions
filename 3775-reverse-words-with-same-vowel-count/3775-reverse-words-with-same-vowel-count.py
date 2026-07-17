class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        count = 0
        sl = s.split(" ")
        for letter in sl[0]:
            if letter in vowels:
                count += 1
        
        for i in range(1, len(sl)):
            curr_count = 0
            for letter in sl[i]:
                if letter in vowels:
                    curr_count += 1
        
            if curr_count == count:
                wordl = list(sl[i])
                wordl.reverse()
                rev_word = "".join(wordl)
                sl[i] = rev_word

        rev_string = ""
        for word in sl:
            rev_string += f"{word} "

        rev_string = list(rev_string)
        rev_string.pop(-1)
        
        rev_string = "".join(rev_string)

        return rev_string