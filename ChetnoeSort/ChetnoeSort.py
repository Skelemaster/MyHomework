class Solution:
    def sort(self, temp_nums: list[int])->list[int]:
        if len(temp_nums)<=1:
            return temp_nums
        mid=len(temp_nums)//2
        nums1=[]
        nums2=[]
        nums3=[]
        for i in temp_nums:
            if i<temp_nums[mid]:
                nums1.append(i)
            elif i>temp_nums[mid]:
                nums3.append(i)
            else:
                nums2.append(i)
        return self.sort(nums1)  + nums2 + self.sort(nums3)
    def ChetnoeSort(self, nums: list[int])->list[int]:
        temp_nums=[]
        for i in nums:
            if i%2==0:
                temp_nums.append(i)        
        temp_nums=self.sort(temp_nums)
        for i in range(len(nums)): 
            if nums[i]%2==0:
                nums.pop(i)
                nums.insert(i,temp_nums[0])
                temp_nums.pop(0)
        return nums