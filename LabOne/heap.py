class Heap:
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.last = len(nums) - 1
        self.build_maximum_heap()

    def build_maximum_heap(self):
        # l = 2i + 1
        # r = 2i + 2
        # i = (r-1)//2

        last_parent = (self.last-1)//2
        while last_parent >= 0:
            self.heapify(last_parent)
            last_parent -= 1

    def heapify(self, i):
        max = i
        l = self.left(i)
        r = self.right(i)

        if l > self.last:
            return

        if self.nums[l] > self.nums[max]:
            max = l

        if r <= self.last and  self.nums[r] > self.nums[max]:
            max = r

        if max == i:
            return

        self.nums[max], self.nums[i] = self.nums[i], self.nums[max]
        self.heapify(max)

    def pop(self):
        max = self.nums[0]
        self.nums[0], self.nums[self.last] = self.nums[self.last], self.nums[0]
        self.last -= 1
        self.heapify(0)
        return max

    @staticmethod
    def left(i):
        return 2 * i + 1

    @staticmethod
    def right(i):
        return 2 * i + 2

    def heap_sort(self):
        res = []
        for i in range(len(self.nums)):
            res.append(self.pop())
        self.nums = res.copy()






