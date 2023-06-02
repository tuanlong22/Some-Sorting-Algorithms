#Heap Sort Algorithm
def heapify(arr, n, i):
    largest = i  # Khởi tạo largest là nút cha
    left = 2 * i + 1  # Vị trí của nút con trái
    right = 2 * i + 2  # Vị trí của nút con phải

    # So sánh nút con trái với nút cha
    if left < n and arr[left] > arr[largest]:
        largest = left

    # So sánh nút con phải với nút cha
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Nếu largest không phải là nút cha, thực hiện hoán đổi và tiếp tục heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Xây dựng heap tối ưu từ mảng không có thứ tự
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Trích xuất lần lượt các phần tử từ heap và tái xây dựng heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Hoán đổi phần tử đầu (lớn nhất) với phần tử cuối
        heapify(arr, i, 0)

    return arr


arr = [9, 4, 5, 1, 5, 13, 10]
sorted_arr = heap_sort(arr)

print(sorted_arr)
