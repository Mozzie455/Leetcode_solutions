#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # TODO: Convert x into str
        word = str(x)
        # TODO: check if is a palindrome
        return word == word[::-1]


        
# @lc code=end

