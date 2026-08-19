class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(index):
            if index == n:
                return True

            if index in memo:
                return memo[index]

            for end in range(index + 1, n + 1):
                if s[index:end] in wordSet and dfs(end):
                    memo[index] = True
                    return True

            memo[index] = False
            return False

        return dfs(0)