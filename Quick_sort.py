def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, l, r):
    if l >= r:
        return
    i = l + 1
    j = r
    pivot = arr[l]
    while i <= j:
        while i<=j and arr[i] < pivot:
            i += 1
        while i<=j and arr[j] > pivot:
            j -= 1
        if i <= j:
            swap(arr, i, j)
            i += 1
            j -= 1
    swap(arr,l,j)
    return j

def quick_sort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quick_sort(arr, l, p)
        quick_sort(arr, p + 1, r)

arr = [9, 4, 5, 1, 5, 13, 10]
n = len(arr)
quick_sort(arr, 0, n - 1)

for i in arr:
    print(i, end=" ")
