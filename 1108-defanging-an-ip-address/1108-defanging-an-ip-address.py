class Solution:
    def defangIPaddr(self, address: str) -> str:
        # ladd = list(address)

        # for i in range(len(ladd)):
        #     if ladd[i] == ".":
        #         ladd[i] = "[.]"

        # add = "".join(el for el in ladd)

        # return add

        #-------------------------------------------

        while "." in address:
            address = address.replace(".", "[,]")

        while "," in address:
            address = address.replace(",", ".")

        return address

        #-------------------------------------------

        # return address.replace(".", "[.]")