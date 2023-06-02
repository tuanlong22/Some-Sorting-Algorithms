#Merge sort
def Merge_sort(arr):
  if len(arr) > 1:  
    m = (len(arr)) // 2
    #Dividing the array 
    L = arr[:m]
    R = arr[m:]
    Merge_sort(L)
    Merge_sort(R)
    i = j = k = 0
    
    #Copy data to L[] and R[]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    # Check the remaining elements
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1

arr = [9, 4, 5, 1, 5, 13, 10]
Merge_sort(arr)
for i in arr:
    print(i, end = " ")