'''
https://leetcode.com/problems/n-th-tribonacci-number/

this is bottom up dp
'''

class Solution:
    dp = [-1]*38
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    def BottomUp(self, n):
        first = self.dp[0]
        second = self.dp[1]
        third = self.dp[2]
        
        for i in range(3, n+1):
            current = first + second + third
            self.dp[i] = current
            first = second
            second = third
            third = current
    
        return self.dp[n]
    
    def tribonacci(self, n: int) -> int:
        return(self.BottomUp(n))
