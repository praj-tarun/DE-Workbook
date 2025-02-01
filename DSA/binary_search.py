arr = [1,2,4,5,1,3,45,1,9,2,4,51,5]
target = 9
n = len(arr)

#selection sort

for i in range(n):
    curr_min = i
    for j in range(i+1,n):
        if arr[curr_min]>arr[j]:
            curr_min = j
    arr[i],arr[curr_min] = arr[curr_min],arr[i] 

print('Sorted Array: ',arr)

l= 0
r= n-1

while l!=r:
    mid =(l+r)//2
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid]< target:
        l = mid
    else:
        r = mid
    

