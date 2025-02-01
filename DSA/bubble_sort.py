
def bubble_sort(arr=[1,2,3]):
    n = len(arr)-1
    while n>0:
        for i in range(0,n):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        n-=1
    return arr

def bubble_sort_optimised(arr=[1, 2, 3]):
    n = len(arr)
    for i in range(n):  # Outer loop runs n times
        swapped = False  # Flag to track if any swap was made
        for j in range(0, n - i - 1):  # Inner loop iterates through the unsorted portion of the array
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if the elements are in the wrong order
                swapped = True  # Mark that a swap was made
        if not swapped:  # If no swaps were made in the inner loop, the list is already sorted
            break
    return arr


#arr = list(map(int, input('print spaces separated arr items: ').split()))
arr = [2,3,52,2,21,3]

print(bubble_sort(arr))