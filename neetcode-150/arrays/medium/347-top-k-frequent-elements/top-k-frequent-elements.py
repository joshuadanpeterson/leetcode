import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)
        
        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(heap)[1])
        
        return topk