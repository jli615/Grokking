"""MY CODE"""

from heapq import *

def find_closest_elements(arr, K, X):
  result = []
  # TODO: Write your code here
  heap = []
  for i in range(K):
    distance = abs(arr[i] - X)
    heappush(heap, (-distance, arr[i]))

  for i in range(K, len(arr)):
    distance = abs(arr[i] - X)
    if distance < (-heap[0][0]):
      heappop(heap)
      heappush(heap, (-distance, arr[i]))

  for distance, num in heap:
    result = [num] + result

  result.sort()
  return result


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()

"""SOLUTION

from heapq import *


def find_closest_elements(arr, K, X):
  index = binary_search(arr, X)
  low, high = index - K, index + K

  low = max(low, 0)  # 'low' should not be less than zero
  # 'high' should not be greater the size of the array
  high = min(high, len(arr) - 1)

  minHeap = []
  # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
  for i in range(low, high+1):
    heappush(minHeap, (abs(arr[i] - X), arr[i]))

  # we need the top 'K' elements having smallest difference from 'X'
  result = []
  for _ in range(K):
    result.append(heappop(minHeap)[1])

  result.sort()
  return result


def binary_search(arr,  target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = int(low + (high - low) / 2)
    if arr[mid] == target:
      return mid
    if arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  if low > 0:
    return low - 1
  return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
 no
"""