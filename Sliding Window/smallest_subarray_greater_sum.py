"""MY CODE"""

def smallest_subarray_sum(s, arr):
  # TODO: Write your code here
  min_len = float("inf")
  movingSum = 0
  windowStart = 0
  for windowEnd in range(len(arr)):
    movingSum += arr[windowEnd]
    while movingSum >= s:
      min_len = min(min_len, windowEnd - windowStart + 1)
      movingSum -= arr[windowStart]
      windowStart += 1

  return min_len


"""SOLUTION

import math


def smallest_subarray_sum(s, arr):
  
  min_length = math.inf
  window_sum = 0
  window_start = 0
  for window_end in range(0, len(arr)):
      window_sum += arr[window_end]  # add the next element
    # shrink the window as small as possible until the 'window_sum' is smaller than 's'
      while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        window_sum -= arr[window_start]
        window_start += 1
      
  if min_length == math.inf:
    return 0
  return min_length


def main():
  print("Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
  print("Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])))


main()


"""