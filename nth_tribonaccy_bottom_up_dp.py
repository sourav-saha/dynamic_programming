'''
https://leetcode.com/problems/n-th-tribonacci-number/

this is bottom up dp
'''

class Solution:
    def BottomUp(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        
        first = 0
        second = 1
        third = 1
        
        for i in range(3, n+1):
            current = first + second + third
            #self.dp[i] = current
            first = second
            second = third
            third = current
    
        return current
    
    def tribonacci(self, n: int) -> int:
        return(self.BottomUp(n))
