class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        n = len(coins)

        memo = {}

        def recurse(index, amount):
            if amount == 0:
                return 0

            if index == n:
                return math.inf
            
            if (index, amount) in memo:
                return memo[(index, amount)]

            # Don't take current coin
            not_taken = recurse(index + 1, amount)

            # Take current coin (can take unlimited times)
            taken = math.inf
            if coins[index] <= amount:
                x = recurse(index, amount - coins[index])
                taken = 1 + x if x !=math.inf else math.inf

            memo[(index,amount)] = min(taken, not_taken)
            return memo[(index, amount)]

        ans = recurse(0, amount)
        return -1 if ans == math.inf else ans