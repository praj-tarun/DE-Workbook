
def insertion_sort(arr=[1,3,2]):
    n = len(arr)
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            else:
                break # optimization - as if no swap happen then it means the remaining arr is sorted
    return arr

arr = [6,1,45,1,5,77,23,3]

print(insertion_sort(arr))



