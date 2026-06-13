class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_pair = 0
        seen = set()

        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            max_pair = max(max_pair, len(seen))
        
        return max_pair

