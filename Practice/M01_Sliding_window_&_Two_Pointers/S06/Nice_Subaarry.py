'''
Nice- Subarry:

'''
#leetcode : 1248
class Solution(object):
    def numberOfSubarrays(self, nums, k):
        def most(k):
            if k < 0 :
                return 0
            left , right = 0, 0 
            odd = 0
            count = 0
            for right in range(len(nums)):
                if nums[right] % 2 ==1:
                    odd += 1 
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1
                    left += 1
                count += right - left +1
            return count
        return most(k) - most(k-1)

#leetcode: 1763
class Solution(object):
    def longestNiceSubstring(self, s):
        if len(s) < 2:
            return ""
        chars= set(s)   #{'Y', 'a', 'z', 'A','y'}
        for i , c in enumerate(s):    #Return both index and values
            if c.lower() in chars and c.upper() in chars:
                continue
            left = self.longestNiceSubstring(s[:i])    #self--> Object
            right = self.longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
        return s