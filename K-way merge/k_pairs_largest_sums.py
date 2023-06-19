"""MY CODE"""
from heapq import *

def find_k_largest_pairs(nums1, nums2, k):
  result = []
  # TODO: Write your code here
  if len(nums1) > k:
    nums1 = nums1[:k]
  if len(nums2) > k:
    nums2 = nums2[:k]

  min_heap = []
  # form: (sum, [pair])

  for i in range(len(nums1)):
    element1 = nums1[i]
    for j in range(len(nums2)):
      element2 = nums2[j]
      sum = element1 + element2
      if len(min_heap) < k:
        heappush(min_heap, (sum, [element1, element2]))
      else:
        if sum > min_heap[0][0]:
          heappop(min_heap)
          heappush(min_heap, (sum, [element1, element2]))

  for element in min_heap:
    result.append(element[1])
  
  return result

  
      



  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()

"""SOLUTION

from __future__ import print_function
from heapq import *


def find_k_largest_pairs(nums1, nums2, k):
  minHeap = []
  for i in range(0, min(k, len(nums1))):
    for j in range(min(k, len(nums2))):
      if len(minHeap) < k:
        heappush(minHeap, (nums1[i] + nums2[j], i, j))
      else:
        # if the sum of the two numbers from the two arrays is smaller than the smallest(top)
        # element of the heap, we can 'break' here. Since the arrays are sorted in the
        # descending order, we'll not be able to find a pair with a higher sum moving forward
        if nums1[i] + nums2[j] < minHeap[0][0]:
          break
        else:  # we have a pair with a larger sum, remove top and insert this pair in the heap
          heappop(minHeap)
          heappush(mianHeap, (nums1[i] + nums2[j], i, j))

  result = []
  for (num, i, j) in minHeap:
    result.append([nums1[i], nums2[j]])

  return result


def main():
  print("Pairs with largest sum are: " +
        str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3)))


main()

"""