class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sol = 0
        sağ = len(nums)-1
        while sol <= sağ:
            orta = (sol+sağ) // 2
            orta_deger = nums[orta]
            if orta_deger == target:
                return orta
            elif target > orta_deger:
                sol = orta +1
            else:
                sağ = orta -1
        return -1

