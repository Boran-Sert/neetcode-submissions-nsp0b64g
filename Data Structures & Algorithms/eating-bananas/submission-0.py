import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        sol = 1
        sag = max(piles)
        en_iyi_hiz = sag
        
        while sol <= sag:
            k = (sol + sag) // 2 
            
            toplam_saat = 0
            for yigin in piles:
                toplam_saat += math.ceil(yigin / k)
            
            if toplam_saat <= h:
                en_iyi_hiz = k
                sag = k - 1
            else:
                sol = k + 1
                
        return en_iyi_hiz