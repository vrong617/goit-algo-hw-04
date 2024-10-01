import timeit
import random
import pandas as pd


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


sizes = [1000, 5000, 10000]
test_data = {size: random.sample(range(size * 10), size) for size in sizes}


def run_sorting_benchmark():
    results = {}
    for size, data in test_data.items():
        arr1, arr2, arr3 = data[:], data[:], data[:]
        time_insertion = timeit.timeit(lambda: insertion_sort(arr1), number=1)
        time_merge = timeit.timeit(lambda: merge_sort(arr2), number=1)
        time_timsort = timeit.timeit(lambda: sorted(arr3), number=1)
        results[size] = {
            'insertion_sort': time_insertion,
            'merge_sort': time_merge,
            'timsort': time_timsort
        }

    return results


benchmark_results = run_sorting_benchmark()
df = pd.DataFrame(benchmark_results).T
print(df)
