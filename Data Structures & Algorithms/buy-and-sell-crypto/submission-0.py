class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        en_dusuk_fiyat = prices[0] 
        maksimum_kar = 0
        
        for su_anki_fiyat in prices:
            if su_anki_fiyat < en_dusuk_fiyat:
                en_dusuk_fiyat = su_anki_fiyat
            
            else:
                kar = su_anki_fiyat - en_dusuk_fiyat
                maksimum_kar = max(maksimum_kar, kar)
                
        return maksimum_kar