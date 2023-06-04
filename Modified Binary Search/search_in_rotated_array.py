"""MY CODE"""

def search_rotated_array(arr, key):
  # sort array
  arr_end_index = end_index_rotated_array(arr)

  start_half_of_arr = []
  if arr_end_index < len(arr) - 1:
    start_half_of_arr = arr[arr_end_index + 1:]
  end_half_of_arr = arr[0:arr_end_index]

  sorted_array = start_half_of_arr + end_half_of_arr

  # binary search on sorted array
  start, end = 0, len(sorted_array) - 1
  index = -1
  while start <= end:
    mid = (start + end) // 2
    if sorted_array[mid] == key:
      index = mid
      break
    elif sorted_array[mid] < key:
      start = mid + 1
    else:
      end = mid - 1

  return arr_end_index + 1 + index

def end_index_rotated_array(arr):
  arr_end = arr[-1]

  start, end = 0, len(arr) - 1
  arr_max_index = -1

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] > arr[mid + 1]:
      arr_max_index = mid
      break
    elif arr[mid] < arr_end:
      end = mid - 1
    else:
      start = mid + 1
  
  return arr_max_index


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))


main()

"""SOLUTION

def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid

    if arr[start] <= arr[mid]:  # left side is sorted in ascending order
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:  # key > arr[mid]
        start = mid + 1
    else:  # right side is sorted in ascending order
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1

  # we are not able to find the element in the given array
  return -1


def main():
  print(search_rotated_array([10, 15, 1, 3, 8], 15))
  print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))

main()

"""