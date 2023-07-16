"""MY CODE"""

import heapq

class SlidingWindowMedian:

  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    n = len(nums)
    result = [0.0 for _ in range(n - k + 1)]

    for i in range(0, n):
      # insert element
      if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
        heapq.heappush(self.maxHeap, -nums[i])
      else:
        heapq.heappush(self.minHeap, nums[i])

      self.rebalance_heaps()

      # add medium
      if i - k + 1 >= 0:
        if len(self.maxHeap) == len(self.minHeap):
          result[i - k + 1] = (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
          result[i - k + 1] = - self.maxHeap[0] / 1.0

        # remove element
        element_to_remove = nums[i - k + 1]
        if element_to_remove <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -element_to_remove)
        else:
          self.remove(self.minHeap, element_to_remove)

        self.rebalance_heaps()

    return result

  # remove element from heap
  def remove(self, heap, element):
    # find index of element
    index = heap.index(element)
    # remove element by swapping with last element
    heap[index] = heap[-1]
    del heap[-1]
    # resort heap
    heapq.heapify(heap)

  # rebalance heap
  def rebalance_heaps(self):
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
    elif len(self.minHeap) > len(self.maxHeap):
      heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

"""SOLUTION CODE

from heapq import *
import heapq


class SlidingWindowMedian:
  def __init__(self):
    self.maxHeap, self.minHeap = [], []

  def find_sliding_window_median(self, nums, k):
    result = [0.0 for x in range(len(nums) - k + 1)]
    for i in range(0, len(nums)):
      if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
        heappush(self.maxHeap, -nums[i])
      else:
        heappush(self.minHeap, nums[i])

      self.rebalance_heaps()

      if i - k + 1 >= 0:  # if we have at least 'k' elements in the sliding window
        # add the median to the the result array
        if len(self.maxHeap) == len(self.minHeap):
          # we have even number of elements, take the average of middle two elements
          result[i - k + 1] = -self.maxHeap[0] / \
                              2.0 + self.minHeap[0] / 2.0
        else:  # because max-heap will have one more element than the min-heap
          result[i - k + 1] = -self.maxHeap[0] / 1.0

        # remove the element going out of the sliding window
        elementToBeRemoved = nums[i - k + 1]
        if elementToBeRemoved <= -self.maxHeap[0]:
          self.remove(self.maxHeap, -elementToBeRemoved)
        else:
          self.remove(self.minHeap, elementToBeRemoved)

        self.rebalance_heaps()

    return result

  # removes an element from the heap keeping the heap property
  def remove(self, heap, element):
    ind = heap.index(element)  # find the element
    # move the element to the end and delete it
    heap[ind] = heap[-1]
    del heap[-1]
    # we can use heapify to readjust the elements but that would be O(N),
    # instead, we will adjust only one element which will O(logN)
    if ind < len(heap):
      heapq._siftup(heap, ind)
      heapq._siftdown(heap, 0, ind)

  def rebalance_heaps(self):
    # either both the heaps will have equal number of elements or max-heap will have
    # one more element than the min-heap
    if len(self.maxHeap) > len(self.minHeap) + 1:
      heappush(self.minHeap, -heappop(self.maxHeap))
    elif len(self.maxHeap) < len(self.minHeap):
      heappush(self.maxHeap, -heappop(self.minHeap))


def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

"""
