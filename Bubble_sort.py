#Bubble sort
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                swap(arr, i, j)

arr = [9, 4, 5, 1, 5, 13, 10]
bubble_sort(arr)
for i in arr:
    print(i, end=" ")
