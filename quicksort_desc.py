def desc_partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] > x:        # key change for descending quicksort, opposing A[j] <= x in ascending quicksort
            i = i + 1
            (A[i] , A[j]) = (A[j], A[i])
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    return i + 1

def desc_quicksort(A, p, r):
    if p < r:
        q = desc_partition(A, p, r)
        desc_quicksort(A, p, q - 1)
        desc_quicksort(A, q + 1, r)

data = [4, 6, 3, 10, 7, 1, 8, 2, 9, 5]
print("Unsorted Array:")
print(data)

size = len(data)

desc_quicksort(data, 0, size - 1)

print('Sorted Array in Descending Order:')
print(data)
