def bubble_sort(arr):
    '''Takes in array and then sort it in n square time'''

    size = len(arr)
    for i in range(size):
        should_continue = False
        for j in range((size-i)-1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j] , arr[j+1]
                should_continue = True
        if not should_continue:
            break

    return arr

bubble_sort([5,4,3,2,1])



def insertion_sort(arr):
    '''Go through all elements except firt
    Call it "key"
    Each time, the key would be 'inserted' in its place
    at each step, stuff less than i would be already sorted'''
    for i in range(1, len(arr)):
        key = arr[i] #hold this key
        #start comparing keys to items on its left
        #stop when less or equal value found (or we reach left end)
        j =  i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] #keep moving this to right.
        
        arr[j + 1] = key #INSERT key in free slot (j+1 bcz we decremented j above)
    return arr

def selection_sort(arr):
    '''find the minimum, then next minimum then next and keep swapping with its respective places'''

    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def quick_sort(arr, fst, lst):
    '''recursively sorts array elements in nlogn time'''
    import random

    if fst >= lst:  return

    i, j = fst, lst
    pivot = arr[random.randint(fst, lst)]

    while i <=j :
        while arr[i] < pivot: i+=1
        while arr[j] > pivot: j-=1

        if i <=j:
            arr[i], arr[j] = arr[j], arr[i]
            i , j = i + 1, j - 1

    quick_sort(arr, fst, j)
    quick_sort(arr, i , lst)
    


def merge(arr, low, mid, high):
    '''recursively sorts the array in divide and merge method'''
    temp = []  
    left = low  
    right = mid + 1  
    
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)  
    mergeSort(arr, mid + 1, high) 
    merge(arr, low, mid, high)  




