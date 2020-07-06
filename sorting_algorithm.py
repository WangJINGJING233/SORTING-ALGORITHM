# /usr/bin/python
# -*- coding=utf-8 -*-

# 最好时间复杂度   O(n)
# 最坏时间复杂度   O(n^2)
# 平均时间复杂度   O(n^2)
# 空间复杂度      O(1)
# 稳定
def BubbleSort(arr):
    n = len(arr)
    if n < 2: return arr
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 优化 设置标志位
# 当一次循环中没有出现交换，则说明此时数组已经是排好序的了
def BubbleSort_1(arr):
    n = len(arr)
    if n < 2: return arr
    for i in range(n - 1):
        flag = True
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                flag = False
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if flag:
            return


# 最好时间复杂度   O(n^2)
# 最坏时间复杂度   O(n^2)
# 平均时间复杂度   O(n^2)
# 空间复杂度      O(1)
# 不稳定
def SelectSort(arr):
    n = len(arr)
    if n < 2: return arr
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 最好时间复杂度   O(nlogn)
# 最坏时间复杂度   O(n^2)
# 平均时间复杂度   O(nlogn)
# 空间复杂度      O(nlogn)
# 不稳定
def QuickSort(arr, left, right):
    if left >= right: return
    i, j = left, right
    val = arr[left]
    while i < j:
        while i < j and arr[j] >= val:
            j -= 1
        arr[i] = arr[j]
        while i < j and arr[i] <= val:
            i += 1
        arr[j] = arr[i]
    arr[i] = val
    QuickSort(arr, left, j - 1)
    QuickSort(arr, j + 1, right)

# 最好时间复杂度   O(n)
# 最坏时间复杂度   O(n^2)
# 平均时间复杂度   O(n^2)
# 空间复杂度      O(1)
# 稳定
def InsertSort(arr):
    n = len(arr)
    if n < 2: return
    for i in range(1, n):
        j, val = i, arr[i]
        while j >= 1 and arr[j - 1] > val:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

# 最好时间复杂度   O(n)
# 最坏时间复杂度   O(n^2)
# 平均时间复杂度   O(n^1.3)
# 空间复杂度      O(1)
# 不稳定
def ShellSort(arr):
    n = len(arr)
    if n < 2: return
    gap = n // 2
    while gap:
        for i in range(gap, n):
            j, val = i, arr[i]
            while j >= gap and arr[j - gap] > val:
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                j -= gap
        gap //= 2

# 最好时间复杂度   O(nlogn)
# 最坏时间复杂度   O(nlogn)
# 平均时间复杂度   O(nlogn)
# 空间复杂度      O(n)
# 稳定
def MergeSort(arr):
    n = len(arr)
    if n < 2: return arr
    mid = n // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res = res + left[i:] + right[j:]
    return res

# 最好时间复杂度   O(nlogn)
# 最坏时间复杂度   O(nlogn)
# 平均时间复杂度   O(nlogn)
# 空间复杂度      O(1)
# 不稳定
def HeapSort(arr):
    n = len(arr)
    if n < 2: return
    # 调整成大顶堆
    for i in range(n // 2 - 1, -1, -1):
        heapAdjust(arr, i, n)
    # 把root的值放到最后，再把剩下的数据调整成大顶堆
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapAdjust(arr, 0, i)


def heapAdjust(arr, i, n):
    root, left, right = i, 2 * i + 1, 2 * i + 2
    if left < n and arr[root] < arr[left]: root = left
    if right < n and arr[root] < arr[right]: root = right
    if root != i:
        arr[root], arr[i] = arr[i], arr[root]
        heapAdjust(arr, root, n)


arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("BubbleSort")
BubbleSort(arr)
print(arr)

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("SelectSort")
SelectSort(arr)
print(arr)

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("QuickSort")
QuickSort(arr, 0, len(arr) - 1)
print(arr)

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("InsertSort")
InsertSort(arr)
print(arr)

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("ShellSort")
ShellSort(arr)
print(arr)

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("MergeSort")
print(MergeSort(arr))

arr = [7, 3, 4, 6, 5, 1, 9, 0, 2, 8]
print("HeapSort")
HeapSort(arr)
print(arr)
