arr = [1,2,4,5,6,2,6,35,34,2]

def selection_sort(arr = [1,3,2]):
    n = len(arr)
    for i in range(n):
        curr_min = i
        for j in range(i+1,n):
            if arr[curr_min]>arr[j]:
                curr_min = j
        arr[curr_min],arr[i] = arr[i],arr[curr_min]
    return arr

print(selection_sort(arr))