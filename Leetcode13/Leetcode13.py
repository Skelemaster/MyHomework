class Solution:
    def romanToInt(self, s: str) -> int:
        list_nums=[]
        for i in s:
            if i == "I":
                i = 1
            elif i == "V":
                i = 5
            elif i == "X":
                i = 10
            elif i == "L":
                i = 50
            elif i == "C":
                i = 100
            elif i == "D":
                i = 500
            elif i == "M":
                i = 1000
            else:
                return "Неверный Ввод"
            list_nums.append(i)
        for i in range(len(list_nums)-1):
            if list_nums[i]<list_nums[i+1]:
                list_nums[i+1]=list_nums[i+1]-list_nums[i]
                list_nums[i]=0
        temp_num=0
        for i in list_nums:
            temp_num+=i
        return temp_num