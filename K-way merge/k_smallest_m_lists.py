"""MY CODE"""

from heapq import *

def find_Kth_smallest(lists, k):
  number = -1
  # TODO: Write your code here
  n = 0
  # heap contains (value, list index)
  min_heap = []
  for i in range(len(lists)):
    curr_list = lists[i]
    heappush(min_heap, (curr_list[0], i))
    curr_list.pop(0)
    if len(curr_list) == 0:
      lists.pop(i)
  
  while n < k-1:
    value, list_index = heappop(min_heap)
    curr_list = lists[list_index]
    heappush(min_heap, (curr_list[0], i))
    curr_list.pop(0)
    if len(curr_list) == 0:
      lists.pop(i)
    n += 1


  return min_heap[0][0]


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()

"""SOLUTION

from heapq import *


def find_Kth_smallest(lists, k):
  minHeap = []

  # put the 1st element of each list in the min heap
  for i in range(len(lists)):
    heappush(minHeap, (lists[i][0], 0, lists[i]))

  # take the smallest(top) element form the min heap, if the running count is equal to k return the number
  numberCount, number = 0, 0
  while minHeap:
    number, i, list = heappop(minHeap)
    numberCount += 1
    if numberCount == k:
      break
    # if the array of the top element has more elements, add the next element to the heap
    if len(list) > i+1:
      heappush(minHeap, (list[i+1], i+1, list))

  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()

"""