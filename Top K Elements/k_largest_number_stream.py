"""MY CODE"""

from heapq import *

class KthLargestNumberInStream:
  def __init__(self, nums, k):
    # TODO: Write your code here
    self.k = k
    self.heap = []
    for i in range(k):
      heappush(self.heap, nums[i])
    for i in range(k, len(nums)):
      if nums[i] > self.heap[0]:
        heappop(self.heap)
        heappush(self.heap, nums[i])


  def add(self, num):
    if num > self.heap[0]:
      heappop(self.heap)
      heappush(self.heap, num)
    # TODO: Write your code here
    return self.heap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

"""SOLUTION

from heapq import *


class KthLargestNumberInStream:
  minHeap = []

  def __init__(self, nums, k):
    self.k = k
    # add the numbers in the min heap
    for num in nums:
      self.add(num)

  def add(self, num):
    # add the new number in the min heap
    heappush(self.minHeap, num)

    # if heap has more than 'k' numbers, remove one number
    if len(self.minHeap) > self.k:
      heappop(self.minHeap)

    # return the 'Kth largest number
    return self.minHeap[0]


def main():

  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()

"""