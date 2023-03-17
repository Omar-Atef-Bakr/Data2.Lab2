from time_fun import timed_function
from heap import Heap
import random
import sys

sys.path.append('../')
import plot_fun


PLOT = False
# PLOT = True

def quick_sort(array : list[int], start: int, end: int):
    length = end - start + 1
    if length <= 1:
        return
    pivot = random.randint(start, end)
    array[pivot],array[start] = array[start],array[pivot]
    unkown = start+1
    last1 = start+1
    while unkown <= end:
        if array[unkown] < array[start]:
            array[last1],array[unkown] = array[unkown],array[last1]
            last1+=1
        unkown += 1
    array[start], array[last1 - 1] = array[last1 - 1], array[start]

    quick_sort(array, start, last1 - 2)
    quick_sort(array, last1, end)


def merge_sort(nums: list[int], start: int, end: int) -> None:
    mid = (end + start) // 2

    if start < end:
        merge_sort(nums, start, mid)
        merge_sort(nums, mid+1, end)
        merge(nums, start, end, mid+1)


def merge(nums, start, end, mid):
    p1 = start
    p2 = mid
    result = []
    while p1 < mid and p2 <= end:
        if nums[p1] < nums[p2]:
            result.append(nums[p1])
            p1 += 1
        else:
            result.append(nums[p2])
            p2 += 1

    while p1 < mid:
        result.append(nums[p1])
        p1 += 1

    while p2 < end:
        result.append(nums[p2])
        p2 += 1

    for i, val in enumerate(result):
        nums[start+i] = val


def insertion_sort(nums: list[int]):
    p = 1
    while p < len(nums):
        i = p
        num = nums[p]

        while i >= 0:
            if num <= nums[i-1] and i > 0:
                nums[i] = nums[i-1]
                i -= 1
            else:
                nums[i] = num
                break

        p += 1


def selection_sort(nums: list[int]):
    p = 0
    while p < len(nums)-1:
        min = p
        for i,num in enumerate(nums[p:]):
            if num < nums[min]:
                min = i + p
        nums[min], nums[p] = nums[p], nums[min]
        p += 1

# nums = [0,2,4,6,8,1,3,5,7,9]
# random.shuffle(nums)
# print(f"before Msort: {nums}")
# merge_sort(nums, 0, len(nums)-1)
# print(f"after Msort: {nums}")
# nums.sort()


# array = [random.randint(0,100) for _ in range(10)]
# print('before Qsort:',array)
# quick_sort(array, 0, len(array)-1)
# print('after Qsort',array)
# insertion_sort(array)
# print(array)

# selection_sort(array)
# print(array)

def heap_sort(array):
    heap = Heap(array)
    # print(heap.nums)
    heap.heap_sort()
    # print(heap.nums)

timed_selection_sort = timed_function(selection_sort)
timed_insertion_sort = timed_function(insertion_sort)
timed_heap_sort = timed_function(heap_sort)
timed_merge_sort = timed_function(merge_sort)
timed_quick_sort = timed_function(quick_sort)

selection_sort_time = []
insertion_sort_time = []
heap_sort_time = []
merge_sort_time = []
quick_sort_time = []


if PLOT:
    # sizes = [1000, 25000, 50000, 100000]
    sizes = [10,50,100,150]

    for size in sizes:
        array = [random.randint(0, 10000) for _ in range(size)]

        print(f"--------------{size}---------------")
        selection_sort_time.append(timed_selection_sort(array.copy()))
        insertion_sort_time.append(timed_insertion_sort(array.copy()))
        heap_sort_time.append(timed_heap_sort(array.copy()))
        merge_sort_time.append(timed_merge_sort(array.copy(), 0, size-1))
        quick_sort_time.append(timed_quick_sort(array.copy(), 0, size-1))

    arr = [1,2,3,4,5,6,7,8,9,10]

    plot_fun.plot_data(selection_sort_time, insertion_sort_time, heap_sort_time, merge_sort_time, quick_sort_time, x=sizes,
                       labels = ["selection", "insertion", "heap", "merge", "quick"], xlabel = 'time', ylabel = "size")

    plot_fun.plot_data(selection_sort_time, insertion_sort_time, x=sizes,
                       labels = ["selection", "insertion"], xlabel = 'time', ylabel = "size")

    plot_fun.plot_data(heap_sort_time, merge_sort_time, quick_sort_time, x=sizes,
                       labels = ["heap", "merge", "quick"], xlabel = 'time', ylabel = "size")


