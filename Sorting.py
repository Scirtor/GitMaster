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