def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        sorted_less = quick_sort(less_than_pivot)
        sorted_greater = quick_sort(greater_than_pivot)
        sorted_arr = sorted_less + [pivot] + sorted_greater
        print("Sorting step:", sorted_arr)
        return sorted_arr

# Demo
arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("Original array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
