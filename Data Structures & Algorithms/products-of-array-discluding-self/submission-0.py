
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        cevap = []  
        
        for i in range(len(nums)):
            carpim = 1
            for j in range(len(nums)):
                if i != j: 
                    carpim *= nums[j] 
            
            
            cevap.append(carpim) 
            
        return cevap
        