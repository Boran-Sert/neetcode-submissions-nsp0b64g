class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Adım: Elemanların frekanslarını sayıyoruz
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # 2. Adım: Frekansları indeks olarak tutacağımız "kovaları" oluşturuyoruz
        # Dizinin boyutu en fazla len(nums) + 1 olabilir (0 frekansından dolayı)
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Sayıları, frekanslarına denk gelen indekslere yerleştiriyoruz
        for num, c in count.items():
            freq[c].append(num)
            
        # 3. Adım: En yüksek frekanstan (sondan) başlayarak k tane elemanı topluyoruz
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res