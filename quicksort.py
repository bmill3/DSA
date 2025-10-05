def partition(A, p, r):
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            (A[i] , A[j]) = (A[j], A[i])
    (A[i + 1], A[r]) = (A[r], A[i + 1])
    return i + 1

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

data = [4, 6, 3, 10, 7, 1, 8, 2, 9, 5]
print("Unsorted Array:")
print(data)

size = len(data)

quicksort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)