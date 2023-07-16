"""MY CODE"""

from heapq import *

def find_Kth_smallest_number(nums, k):
  # TODO: Write your code here
  max_heap = []
  for i in range(k):
    heappush(max_heap, -nums[i])

  for i in range(k, len(nums)):
    if nums[i] < -max_heap[0]:
      heappop(max_heap)
      heappush(max_heap, -nums[i])

  return -max_heap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

"""SOLUTIONS
MAX HEAP
from heapq import *


def find_Kth_smallest_number(nums, k):
  maxHeap = []
  # put first k numbers in the max heap
  for i in range(k):
    heappush(maxHeap, -nums[i])

  # go through the remaining numbers of the array, if the number from the array is smaller than the
  # top(biggest) number of the heap, remove the top number from heap and add the number from array
  for i in range(k, len(nums)):
    if -nums[i] > maxHeap[0]:
      heappop(maxHeap)
      heappush(maxHeap, -nums[i])

  # the root of the heap has the Kth smallest number
  return -maxHeap[0]


def main():

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

QUICKSORT PARTITIONING
def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

RANDOMIZED PARTITIONING
import random


def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  pivotIndex = random.randint(low, high)
  nums[pivotIndex], nums[high] = nums[high], nums[pivotIndex]

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

MEDIAN OF MEDIANS
def find_Kth_smallest_number(nums, k):
  return find_Kth_smallest_number_rec(nums, k, 0, len(nums) - 1)


def find_Kth_smallest_number_rec(nums, k, start, end):
  p = partition(nums, start, end)

  if p == k - 1:
    return nums[p]

  if p > k - 1:  # search lower part
    return find_Kth_smallest_number_rec(nums, k, start, p - 1)

  # search higher part
  return find_Kth_smallest_number_rec(nums, k, p + 1, end)


def partition(nums, low, high):
  if low == high:
    return low

  median = median_of_medians(nums, low, high)
  # find the median in the array and swap it with 'nums[high]' which will become our pivot
  for i in range(low, high):
    if nums[i] == median:
      nums[i], nums[high] = nums[high], nums[i]
      break

  pivot = nums[high]
  for i in range(low, high):
    # all elements less than 'pivot' will be before the index 'low'
    if nums[i] < pivot:
      nums[low], nums[i] = nums[i], nums[low]
      low += 1

  # put the pivot in its correct place
  nums[low], nums[high] = nums[high], nums[low]
  return low


def median_of_medians(nums, low, high):
  n = high - low + 1
  # if we have less than 5 elements, ignore the partitioning algorithm
  if n < 5:
    return nums[low]

  # partition the given array into chunks of 5 elements
  partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

  # for simplicity, lets ignore any partition with less than 5 elements
  fullPartitions = [
    partition for partition in partitions if len(partition) == 5]

  # sort all partitions
  sortedPartitions = [sorted(partition) for partition in fullPartitions]

  # find median of all partations; the median of each partition is at index '2'
  medians = [partition[2] for partition in sortedPartitions]

  return partition(medians, 0, len(medians)-1)


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

  # since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(find_Kth_smallest_number([5, 12, 11, -1, 12], 3)))


main()

"""