class Solution:
    def encode(self, strs: list[str]) -> str:
        if not strs:
            return "##BOS_LISTE##" 
        return "./".join(strs)

    def decode(self, s: str) -> list[str]:
        if s == "##BOS_LISTE##":
            return [] 
        return s.split("./")