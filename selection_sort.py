#Selection sort Algorithm
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def Selection_sort(arr,n):
    min = arr[0]
    for i in range (0,n):
        index = i
        min = arr[i]
        for j in range (i,n):
            if arr[j] < min:
                min = arr[j]
                index = j
        swap(arr,i,index)

arr = [9, 4, 5, 1, 5, 13, 10]
n = len(arr)
Selection_sort(arr, n)

for i in arr:
    print(i, end=" ")