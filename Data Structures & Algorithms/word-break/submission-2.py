class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        t = 0
        for w in wordDict:
            t = max(t,len(w))
        n = len(s)
        memo = {}


        def dfs(index):
            if index == n:
                return True

            if index in memo:
                return memo[index]

            for j in range(index, min(n,index+t)):
                if s[index:j+1] in wordSet and dfs(j+1):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)