'''
Problem statement
You are given an infinite array consisting of only ones and zeroes, in sorted order. You have to find the index of the first occurrence of 1.

Example:
If the array is 0 0 0 0 1 1 1 1… then, the first occurrence of 1 will be at index 4 therefore the answer here is 4.
'''


def firstOne(get):
    
    # Write your code here.
    # This function returns the first index of the occurence of 1
    l,r = 0,1

    while get(r)!=1:
        r*=2
    while l!=r:
        mid = (l+r)//2
        if get(mid-1)==0 and get(mid)==1:
            return mid
        elif get(mid)<1:
            l=mid
        else:
            r=mid
    return