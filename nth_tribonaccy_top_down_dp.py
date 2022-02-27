'''
Link: https://leetcode.com/problems/n-th-tribonacci-number/

1137. N-th Tribonacci Number
Easy

1568

97

Add to List

Share
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

 

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
Example 2:

Input: n = 25
Output: 1389537
'''

#this is top down dp
class Solution:
    dp = [-1]*38
    def TopDown(self, n):
        #base case
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif self.dp[n] == -1:
            self.dp[n] = self.TopDown(n-3) + self.TopDown(n-2) + self.TopDown(n-1)
            
        return self.dp[n]
    
    def tribonacci(self, n: int) -> int:
        return(self.TopDown(n))
      
      
