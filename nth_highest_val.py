## bubble_sort

'''
If the list is small bubble sort works fine but incase of millions of element in list
If it doesnt fit in memory, we might try other sorting algo ex. merge sort or quick sort etc
by taking CPU cores benefit.
'''
def bubble_sort(arr_list: list) -> list:
    n: int = len(arr_list)
    for i in range(n):
        # (-i) for looping through only remaining unsorted list
        for j in range(n-1-i):
            # swap if current value is greater than next
            if arr_list[j] > arr_list[j+1]:
                arr_list[j], arr_list[j+1] = arr_list[j+1], arr_list[j]

    return arr_list

if __name__ == '__main__':
    # nth highest value
    val = 2
    # list of values
    lst = [10, 7, 7, 5, 2, 3, 11]
    rm_dup = list(set(lst))
    print("Original list : {}".format(lst))
    print("Sorted list : {}".format(rm_dup))
    print("{} highest value is : {}".format(val,bubble_sort(rm_dup)[-val]))