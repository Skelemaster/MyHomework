class Solution:
    def ListStr(self, ListStr: list[str], ListInt: list[int]) -> list[str]:
        if len(ListStr) != len(ListInt):
            raise Exception("")
        ListStr1=[]
        for i in range(len(ListStr)):
            ListStr1.append(ListStr[ListInt[i]-1])
        return ListStr1