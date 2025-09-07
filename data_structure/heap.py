import heapq

# Простой пример
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1 (минимальный элемент)

# Сложный пример: k-й наибольший элемент
def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

print(kth_largest([3,2,1,5,6,4], 2))  # 5