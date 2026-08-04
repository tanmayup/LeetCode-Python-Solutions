class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in "+-*/":
                st.append(int(token))
            else:
                r, l = st.pop(), st.pop()
                if token == "/":
                    ans = int(l / r)
                elif token == "+":
                    ans = l + r
                elif token == "-":
                    ans = l - r
                else:
                    ans = l * r
                st.append(ans)

        return st[0]