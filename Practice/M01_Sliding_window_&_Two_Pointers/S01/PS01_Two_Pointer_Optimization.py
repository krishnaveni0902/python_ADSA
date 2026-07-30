'''
Two Pointers 
- hconsist of two variables
- it reduces the time and space complexity of the solution 
we use two pointers in arrays(sorted order)

'''

arr = [5,2,7,10]
target = 9
found = False
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        add = arr[i]+ arr[j]
        if add == target:
            print("Found: ", arr[i], arr[j])
            found = True
            break
    if found:
        break 
if not found:
    print("No pairs found")


arr = [5,2,7,10]
arr.sort
target = 9
found = False
left, right = 0, len(arr) - 1
while left < right :
    add = arr[left] + arr[right]
    if add == target:
        print("Found :" , arr[left], arr[right])
        found = True
        break 
    elif add < target:
        left += 1
    else: 
        right -= 1



