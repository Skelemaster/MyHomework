class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if len(digits)==0:
            return "Список пуст"
        list_nums=[]
        temp_str=""
        for i in digits:
            temp_str+=f"{i}"
        temp_str=str(int(temp_str)+1)
        for i in temp_str:
            list_nums.append(int(i))
        return list_nums
