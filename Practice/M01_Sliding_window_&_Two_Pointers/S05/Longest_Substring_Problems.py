#leetcode 3:
#Longest Substring Without Repeating Characters
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a = set()
        left = 0
        right = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left += 1
            a.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
