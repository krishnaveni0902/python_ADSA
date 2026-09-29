'''
What is sliding window: It is a very important optimization technique in DSA
Mainly used in :
Arrays
Types of sliding window:
2 types 
1) Fixed sliding 
2) Variable Sliding 

1) Fixed Sliding:
Size of the window is fixed. Not Change 

'''
#Maximum sum of consecutive Sub-array of fixed size k 
def max_sum(arr, k):
    n = len(arr)
    maxsum = 0 
    for i in range(n-k+1):
        add = 0
        for j in range(k):
            add = add + arr[i+j]
        maxsum = max(maxsum, add)
    return maxsum
print(max_sum([1,2,3,4,5],3))

#Optimal solution 
def max_sum(arr, k):
    maxsum2 = 0 
    add2 = sum(arr[:k])
    for i in range(k,len(arr)): #i=3
        add2 = add2-arr[i-k] + arr[i]
        maxsum2 = max(maxsum2, add2)
    return maxsum2
print(max_sum([1,2,3,4,5],3))

def max_sum(arr, k):
    add2 = sum(arr[:k])
    print(add2/k)
    for i in range(k,len(arr)): #i=3
        add2 = add2-arr[i-k] + arr[i]
        print(add2/k)
max_sum([1,2,3,4,5],3)
