class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sayi_kumesi = set(nums)
        en_uzun_zincir = 0

        for sayi in sayi_kumesi:
            if (sayi - 1) not in sayi_kumesi:
                su_anki_sayi = sayi
                su_anki_zincir = 1

                while (su_anki_sayi + 1) in sayi_kumesi:
                    su_anki_sayi += 1
                    su_anki_zincir += 1

                en_uzun_zincir = max(en_uzun_zincir, su_anki_zincir)
        
        return en_uzun_zincir
        