 #Count sort Algorithm
def Count_sort(arr, N):
    max = arr[0]
    for i in range(N):
        if arr[i]>max:
            max = arr[i]
    
    A = [0] * (max + 1)
    for i in range(max+1):
        A[i] = 0
    for i in range(N):
        A[arr[i]]+=1
    index = 0
    for i in range(max+1):
        if A[i] > 0:
            while A[i]>0:
                arr[index] = i
                A[i] -= 1
                index += 1
arr = [9, 4, 5, 1, 5, 13, 10]
n = len(arr) - 1
Count_sort(arr,n)
for i in arr:
    print(i, end = " ")