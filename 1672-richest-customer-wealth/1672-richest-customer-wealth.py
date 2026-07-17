class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for wealth in accounts:
            if sum(wealth) > max_wealth:
                max_wealth = sum(wealth)

        return max_wealth