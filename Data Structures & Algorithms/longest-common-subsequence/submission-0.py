class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        memo = [[-1]*n for _ in range(m) ]

        def dfs(i,j) -> int:
            if i==m or j==n:
                return 0
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j]= 1 + dfs(i+1,j+1)
                return memo[i][j]
            
            memo[i][j] = max(dfs(i,j+1),dfs(i+1,j))
            return memo[i][j]
        
        return dfs(0,0)
