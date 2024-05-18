def partition(array, low, high):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    """
    i = (low - 1)  # index of smaller element
    pivot = array[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if array[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quick_sort(array, low, high):
    """
    The main function that implements QuickSort

    array[] --> Array to be sorted,
    low  --> Starting index,
    high  --> Ending index
    """
    if len(array) == 1:
        return array
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(array, low, high)

        # Separately sort elements before partition and after partition
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)

# Test the code
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)
