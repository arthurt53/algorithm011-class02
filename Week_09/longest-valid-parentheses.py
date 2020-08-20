class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0 for _ in range(len(s))]
        if len(s) < 2:
            return 0

        if s[1] == ')' and s[0] == '(':
            dp[1] = 2

        if len(s) == 2:
            return dp[1]

        for i in range(2, len(s)):
            if s[i] == '(':
                dp[i] = 0
                continue
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] +2
                if s[i-1] == ')' and s[i-1-dp[i-1]] == '(' and i-1-dp[i-1]>=0:
                    dp[i] = dp[i-1-dp[i-1]-1] + 2 + dp[i-1]
        print(dp)
        return max(dp)
