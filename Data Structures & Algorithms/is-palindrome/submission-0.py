class Solution:
    def isPalindrome(self, s: str) -> bool:
        temiz_metin = "".join(char.lower() for char in s if char.isalnum())
        
        sol, sag = 0, len(temiz_metin) - 1
        
        while sol < sag:
            if temiz_metin[sol] != temiz_metin[sag]:
                return False
            sol += 1
            sag -= 1
            
        return True