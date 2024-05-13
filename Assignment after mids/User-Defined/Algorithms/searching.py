def linear_search(arr, ele):
    '''return index for that element, else -1 if not found'''

    for i in range(len(arr)):
        if arr[i] == ele:
            return i
        
    return -1

def binary_search(arr, low, high, target):
    '''works on sorted arrays only and searches in logn time'''
    if low > high:
        return -1
    
    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binary_search(arr, low, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, high, target)
    
#print(binary_search([1,2,3,4,5], 0, 4 ,1))


def interpolationSearch(arr, lo, hi, x):
    '''Works just like Binary Search but in a slightly better manner'''
    
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
 
        pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
                    (x - arr[lo]))
 
        
        if arr[pos] == x:
            return pos
 
        # If x is larger, x is in right subarray
        if arr[pos] < x:
            return interpolationSearch(arr, pos + 1,
                                       hi, x)
 
        # If x is smaller, x is in left subarray
        if arr[pos] > x:
            return interpolationSearch(arr, lo,
                                       pos - 1, x)
    return -1


def expo_search(arr, target):
    i = 1

    while i< len(arr) and arr[i] < target:
        i *= 2

    return binary_search(arr, i//2, min(i, len(arr)- 1), target)

print(expo_search([1,2,3,4,5], 4))


