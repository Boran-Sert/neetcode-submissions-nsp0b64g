class Solution:
    def trap(self, height: list[int]) -> int:
        if not height: return 0
        
        l, r = 0, len(height) - 1
        sol_max, sag_max = height[l], height[r]
        toplam_su = 0
        
        while l < r:

            if sol_max < sag_max:
                l += 1
                sol_max = max(sol_max, height[l])
                toplam_su += sol_max - height[l]
            else:
                r -= 1
                sag_max = max(sag_max, height[r])
                toplam_su += sag_max - height[r]
                
        return toplam_su