'''
Prifix : The array elements from starting of index to upto the current index O(1) #without prefix O(n**2)
ex: a = [1,2,3,4,5]
prefix[0] = [1]
prefix[1] = [1,2]
prefix[2] = [1,2,3]
prefix[3] = [1,2,3]
prefix[4] = [1,2,3,4]
prefix[5] = [1,2,3,4,5]

prefix sum :
prefix_sum[0] = 0
prefix_sum[1] = 1
prefix_sum[2] = 3
prefix_sum[3] = 6
prefix_sum[4] = 10

Res = [0,1,3,6,10]
 
Formula :
sum(L,R) = prefix[R] - prefix[L-1]
              or 
sum(L,R) = prefix[R+1] - prefix[L]


Ex :
 [1,7,3,6,5,6] ==> 3,6,5 = 3+6+5 = 14
 sum  -> [0,1,8,11,17,22]
 sum(2,4) = [5] - [2] = 22-8 = 14  #using formula




Algorithm:
1) Calculate total sum 
2) initial value of left_sum is zero 
3) traverse all the array ele 
4) Right_sum = total - left_sum - nums[i]
5) compare left_sum == Right_sum 
6) return particular index 
7)
'''
#leetcode: 724
class Solution:
    def pivotIndex(self, nums):
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            Right_sum = Total_sum - Left_sum - nums[i]
            if Left_sum == Right_sum:
                return i
            Left_sum += nums[i]
        return -1

#leetcode : 1991
class Solution(object):
    def findMiddleIndex(self, nums):
        Total_sum = sum(nums)
        Left_sum = 0
        for i in range(len(nums)):
            Right_sum = Total_sum - Left_sum - nums[i]
            if Left_sum == Right_sum:
                return i
            Left_sum += nums[i]
        return -1

#leetcode: 1732
class Solution(object):
    def largestAltitude(self, gain):
        curr_alt = 0
        maxi_alt = 0
        for i in gain:
            curr_alt += i
            maxi_alt = max(maxi_alt,curr_alt)
        return maxi_alt

#leetcode :2574
