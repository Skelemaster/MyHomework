class Solution:
    def Max(self, nums: list[int]) -> int: 
        max_value=nums[0]
        for k in nums:
            if max_value<k:
                max_value=k
        return max_value    
    def Min(self, nums: list[int]) -> int:
        min_value=nums[0]
        for k in nums:
            if min_value>k:
                min_value=k
        return min_value    
    def maxProductDifference(self, nums: list[int]) -> int:
        max_list=[]
        min_list=[]
        max_list.append(self.Max(nums))
        nums.remove(self.Max(nums))
        max_list.append(self.Max(nums))
        nums.remove(self.Max(nums))
        min_list.append(self.Min(nums))
        nums.remove(self.Min(nums))
        min_list.append(self.Min(nums))
        nums.remove(self.Min(nums))
        return ((max_list[0]*max_list[1])-(min_list[0]*min_list[1]))
