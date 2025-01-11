#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # TODO : Create a dictionary for the Roman numerals
        dict = {'I': 1, 'V':5, 'X': 10, 'L':50,'C':100,'D':500, 'M':1000}
        
        # TODO: Initialize the pointers
        total = 0
        n =len(s)
        i = 0
        
        # TODO: Loop until n = 0
        while i < n:
            if i < n-1 and dict[s[i]] < dict[s[i+1]]:
                total += dict[s[i+1]] - dict[s[i]]
                i += 2
            else:
                total += dict[s[i]]
                i += 1
        
# @lc code=end

