class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # 1. SATIRLARI KONTROL ET
        for satir in board:
            rakamlar = [r for r in satir if r != "."]
            if len(rakamlar) != len(set(rakamlar)):
                return False

        # 2. SÜTUNLARI KONTROL ET
        for sutun in zip(*board):
            rakamlar = [s for s in sutun if s != "."]
            if len(rakamlar) != len(set(rakamlar)):
                return False

        # 3. 3x3 KARELERİ KONTROL ET
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                kare = []
                for i in range(3):
                    for j in range(3):
                        hucre = board[r + i][c + j]
                        if hucre != ".":
                            kare.append(hucre)
                
                if len(kare) != len(set(kare)):
                    return False
                
        return True