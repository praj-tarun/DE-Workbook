"""
Maximum area of all possible rectangles that can be formed. The twist here is that you can also reduce any element by atmost 1. 
find the maximum area of all the rectangles that can be fomed.

Note: One element can only be used once to form a single rectangle.

Input1: n = 8 arr[] = [2,3,3,4,6,6,8,8]
Output: 54
Explanation: There are two rectangles that can be formed one with edges [6,6,8,8] and another with by reducing 4 by 1 to 3 a
nd reducing 3 by 1 to 2 so the edges will [2,2,3,3]
Therefore 6 * 8 + 2 * 3 = 54

Input2: [2,1,6,5,4,4]
Output: 20
Explanation: Here just 1 rectangle is possible with maximum by reducing 6 with 5 and hence 5*4 = 20
"""

def max_area(arr):
    # Frequency map to count occurrences of each element
    arr.sort(reverse=True)
    n = len(arr)-1
    res = []
    i = 0
    while i<n:
        if arr[i]==arr[i+1] or arr[i]-1 == arr[i+1]:
            res.append(arr[i+1])
            i+=2
        else:
            i+=1
    if len(res)%2!=0:
        res.pop()
    i = 0
    ans = 0
    while i<len(res):
        ans += res[i]*res[i+1]
        i+=2

    return ans

# Test cases
test_cases = [
    ([2, 6, 6, 2, 3, 5], 12),
    ([4, 3, 2, 3, 4, 5, 2, 4], 22),
    ([2, 1, 6, 5, 4, 4], 20),
    ([2, 3, 3, 4, 6, 6, 8, 8], 54),
    ([10, 10, 10, 10, 11, 10, 11, 10], 210),
    ([3, 4, 5, 6], 15),
    ([3, 2, 5, 2], 0),
    ([11, 11, 10, 10, 10, 10, 10, 11, 10, 30, 10, 9, 9, 8, 8, 7, 6, 5, 10, 12, 12], 439)
]

# Testing the function
for i, (arr, expected) in enumerate(test_cases, 1):
    result = max_area(arr)
    print(f"Test Case {i}: {'Pass' if result == expected else 'Fail'} (Expected: {expected}, Got: {result})")
