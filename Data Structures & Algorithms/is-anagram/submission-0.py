class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Uzunluklar farklıysa anagram olmaları imkansızdır
        if len(s) != len(t):
            return False
            
        count = {}
        
        # s'deki harfleri artır, t'deki harfleri aynı anda azalt
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
            
        # Eğer kelimeler anagramsa, tüm anahtarların değeri tam olarak 0 olmalıdır
        for val in count.values():
            if val != 0:
                return False
                
        return True