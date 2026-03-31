class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        s1_counts = {}
        for char in s1:
            s1_counts[char] = s1_counts.get(char, 0) + 1
            
        for i in range(n2 - n1 + 1):
            pencere = s2[i : i + n1]
            
            pencere_counts = {}
            for char in pencere:
                pencere_counts[char] = pencere_counts.get(char, 0) + 1
            
            if pencere_counts == s1_counts:
                return True
                
        return False