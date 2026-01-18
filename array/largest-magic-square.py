class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        
        # 建立前綴和陣列
        rowSum = [[0] * (n + 1) for _ in range(m)]
        colSum = [[0] * (n) for _ in range(m + 1)]
        diag = [[0] * (n + 1) for _ in range(m + 1)]
        antiDiag = [[0] * (n + 1) for _ in range(m + 1)]
        
        for r in range(m):
            for c in range(n):
                rowSum[r][c+1] = rowSum[r][c] + grid[r][c]
                colSum[r+1][c] = colSum[r][c] + grid[r][c]
                diag[r+1][c+1] = diag[r][c] + grid[r][c]
                antiDiag[r+1][c] = antiDiag[r][c+1] + grid[r][c]

        def is_magic(r, c, k):
            # 以第一行的總和作為基準
            target = rowSum[r][c + k] - rowSum[r][c]
            
            # 1. 檢查行
            for i in range(r + 1, r + k):
                if rowSum[i][c + k] - rowSum[i][c] != target:
                    return False
            
            # 2. 檢查列
            for j in range(c, c + k):
                if colSum[r + k][j] - colSum[r][j] != target:
                    return False
            
            # 3. 檢查正對角線 (\)
            if diag[r + k][c + k] - diag[r][c] != target:
                return False
            
            # 4. 檢查副對角線 (/)
            if antiDiag[r + k][c] - antiDiag[r][c + k] != target:
                return False
            
            return True

        # 從最大可能邊長 k 開始向下枚舉
        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        
        return 1