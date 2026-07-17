class Solution:
    def romanToInt(self, s: str) -> int:
        ri = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }
        dec = 0

        for i in range(len(s)):
            if i != len(s) - 1:
                if ri[s[i]] >= ri[s[i+1]]:
                    dec += ri[s[i]]

                else:
                    dec -= ri[s[i]]

            else:
                # if ri[s[i]] < ri[s[i-1]] or ri[s[i]] == ri[s[i-1]]:
                #     dec += ri[s[i]]
                # elif ri[s[i]] > ri[s[i-1]]:
                #     dec += ri[s[i]]
                dec += ri[s[i]]
        return dec