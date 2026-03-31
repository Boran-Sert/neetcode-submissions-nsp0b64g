class Solution:
    def maxArea(self, heights: list[int]) -> int:
        en_buyuk_alan = 0
        sol = 0
        sag = len(heights) - 1
        
        while sol < sag:
            genislik = sag - sol
            yukseklik = min(heights[sol], heights[sag])
        
            mevcut_alan = genislik * yukseklik
            en_buyuk_alan = max(en_buyuk_alan, mevcut_alan)
            
            if heights[sol] < heights[sag]:
                sol += 1
            else:
                sag -= 1
                
        return en_buyuk_alan