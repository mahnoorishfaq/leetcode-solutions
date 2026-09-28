class Solution(object):
    def lengthOfLongestSubstring(self, s):
        x = {}  # A dictionary that keeps track of each character
        l = ans = 0
        
        for r, c in enumerate(s):
            if c in x:
                l = max(l, x[c] + 1)
            x[c] = r
            ans = max(ans, r - l + 1)
            
        return ans