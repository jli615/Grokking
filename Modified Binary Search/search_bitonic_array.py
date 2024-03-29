"""MY CODE"""

def search_bitonic_array(arr, key):
  # find middle of bitonic array
  start, end = 0, len(arr) - 1

  while start < end:
    mid = (start + end) // 2
    if arr[mid] < arr[mid + 1]:
      start = mid + 1
    else:
      end = mid
  
  middle_of_array_index = start

  # binardy search both sides
  left_array_search  = -1
  right_array_search = -1
  left_array_search = binary_search_index(arr[0:middle_of_array_index], key)
  right_array_search = binary_search_index(arr[middle_of_array_index + 1:], key) + middle_of_array_index + 1

  return max(left_array_search, right_array_search)

def binary_search_index(arr, key):
  start, end = 0, len(arr) - 1

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      start = mid + 1
    else:
      end = mid - 1
  
  return -1


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()

"""SOLUTION
def search_bitonic_array(arr, key):
  maxIndex = find_max(arr)
  keyIndex = binary_search(arr, key, 0, maxIndex)
  if keyIndex != -1:
    return keyIndex
  return binary_search(arr, key, maxIndex + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    if arr[mid] > arr[mid + 1]:
      end = mid
    else:
      start = mid + 1

  # at the end of the while loop, 'start == end'
  return start


# order-agnostic binary search
def binary_search(arr, key, start, end):
  while start <= end:
    mid = int(start + (end - start) / 2)

    if key == arr[mid]:
      return mid

    if arr[start] < arr[end]:  # ascending order
      if key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # descending order
      if key > arr[mid]:
        end = mid - 1
      else:  # key < arr[mid]
        start = mid + 1

  return -1  # element is not found


def main():
  print(search_bitonic_array([1, 3, 8, 4, 3], 4))
  print(search_bitonic_array([3, 8, 3, 1], 8))
  print(search_bitonic_array([1, 3, 8, 12], 12))
  print(search_bitonic_array([10, 9, 8], 10))


main()


"""