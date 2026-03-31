class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arabalar = sorted(zip(position, speed), reverse=True)
        
        stack = [] 
        
        for p, s in arabalar:
            varis_suresi = (target - p) / s
            
            stack.append(varis_suresi)
            
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
