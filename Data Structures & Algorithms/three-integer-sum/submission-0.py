class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() 

        for i, a in enumerate(nums):
            
            if a > 0:
                break
           
            if i > 0 and a == nums[i - 1]:
                continue

            sol, sag = i + 1, len(nums) - 1
            while sol < sag:
                toplam = a + nums[sol] + nums[sag]
                if toplam > 0:
                    sag -= 1
                elif toplam < 0:
                    sol += 1
                else:
                    res.append([a, nums[sol], nums[sag]])
                    sol += 1

                    while nums[sol] == nums[sol - 1] and sol < sag:
                        sol += 1
                        
        return res