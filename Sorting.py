# Lists to Sort

messy_lst_1 = [2, 3, 56, 89,545, 654, 879, 654, 1, 2, 3, 6, 4, 8, 9, 7]
messy_lst_2 = ['a', 'g', 'd', 'e', 'i', 'l']
messy_lst_3 = [978876, 3542313, 654, 65489, 321385, 8943, 5464, 56345]

# Bubble Sort

def bubble_sort(lst):
    for j in range(len(lst)):
        for i in range(0, len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[1+i], lst[i]
    return lst

# print(bubble_sort(messy_lst_3))

def insertsion_sort(lst):
    # srtd_lst = []
    for i in range(len(lst)):
        for j in range(i, 0, -1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst

# print(insertsion_sort(messy_lst_1))

def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def print_list(arr):
    for i in arr:
        print(i, end=" ")
    print()

#Trying to write merge sort by my hand

def merge_sort_handmade(lst):
    if len(lst) > 1:
        L_side = lst[:len(lst) // 2]
        R_side = lst[len(lst) //2:]
        middle = len(lst) // 2
        
        merge_sort_handmade(L_side)
        merge_sort_handmade(R_side)

        i = j = k = 0

        while i < len(L_side) and j < len(R_side):
            if L_side[i] < R_side[j]:
                lst[k] = L_side[i]
                i += 1
            else:
                lst[k] = R_side[j]
                j += 1
            k += 1
        
        while i < len(L_side):
            lst[k] = L_side[i]
            i += 1
            k += 1

        while j < len(R_side):
            lst[k] = R_side[j]
            j += 1
            k += 1
    return lst

# print(merge_sort_handmade(messy_lst_3))