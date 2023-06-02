def Insertion_sort(arr, n):
    for i in range(1, n):
        last = arr[i]
        j = i -1 
        while j>= 0 and arr[j] >last:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1] = last
arr = [9, 4, 5, 1, 5, 13, 10]
n = len(arr) - 1
Insertion_sort(arr,n)
for i in arr:
    print(i, end = " ")