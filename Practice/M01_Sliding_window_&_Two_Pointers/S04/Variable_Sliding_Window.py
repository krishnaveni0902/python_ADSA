'''
Sliding window:
Types:
1. Fixed --> the size 

2. Variable sliding window:
--> The size is not fixed
--> size may inc or dec 

Real  world application :
Meesho application --> Products cart upto my account 

Algorithm :
step-1: we have to use two pointers
step-2: for loop(True)
step-3: Expand my window 
step-4: check the condition
step-5: if condition is false
step-6: Shrink the window
step-7: Update the answer
'''
# Find the longest subarray with sum less than or equal to k 
# arr= [2,1,3,2,1] k=6
'''
Expand [2] => len=1 => 2<=6(T)
Expand[2,1] =>2+1=> 3<= 6(T)
Expand[2,1,3] =>2+1+3=> 6<= 6(T)
Shrink[2,1,3,2] =>2+1+3+2=> 8<= 6(F)
Expand[1,3,2] =>1+3+2=> 6<= 6(T)
Expand[1,3,2,1] =>1+3+2+1=> 7<= 6(F)
Shrink[3,2,1] => 3+2+1=> 6<= 6(T)
'''
def longest(arr, k):
    left = 0
    right = 0 
    add = 0
    max_len = float('-inf')
    for right in range(len(arr)):
        add += arr[right]
        while add > k:
            add -= arr[left]
            left += 1
        max_len = max(max_len, right - left +1)
    return max_len
print(longest([2,1,3,2,1],6))

#Find the smallest sub-array with sum greater than or equal to k
def smallest(arr, k):
    left = 0
    right = 0 
    add = 0
    min_len = float('inf')
    for right in range(len(arr)):
        add += arr[right]
        while add < k:
            min_len = min(min_len, right-left+1)
            add -= arr[left]
            left += 1 
    return 0 if min_len== float("inf") else min_len 
print(smallest([2,1,3,2,1],6))