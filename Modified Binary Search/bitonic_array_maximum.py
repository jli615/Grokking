"""MY CODE"""

def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1

  while start <= end:
    mid = (start + end) // 2

    if mid + 1 < len(arr) and arr[mid + 1] > arr[mid]:
      start = mid + 1
    elif mid - 1 >= 0 and arr[mid - 1] > arr[mid]:
      end = mid - 1
    else:
      return arr[mid]
  # TODO: Write your code here
  #return -1


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()

"""SOLUTION

def find_max_in_bitonic_array(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return arr[start]


def main():
  print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
  print(find_max_in_bitonic_array([3, 8, 3, 1]))
  print(find_max_in_bitonic_array([1, 3, 8, 12]))
  print(find_max_in_bitonic_array([10, 9, 8]))


main()

"""