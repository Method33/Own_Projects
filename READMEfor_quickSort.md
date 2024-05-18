# Quick Sort Algorithm in Python

This repository contains an implementation of the Quick Sort algorithm in Python.

Quick Sort is a Divide and Conquer algorithm, which is used for sorting arrays in-place. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then recursively sorted.

This implementation includes two main functions: `partition()` and `quick_sort()`.

`partition()` is a helper function that takes the last element as pivot, places the pivot element at its correct position in the sorted array, and places all smaller elements (smaller than pivot) to the left of the pivot and all greater elements to the right of the pivot.

`quick_sort()` is the main function that implements Quick Sort. It uses the `partition()` function to sort the elements before the partition and after the partition.

## How to Use

To run the Quick Sort algorithm on an array, simply call the `quick_sort()` function with your array and the starting and ending index as arguments. For example:

```python
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n - 1)
print("Sorted array is:", arr)
