"""MY CODE"""


def search_min_diff_element(arr, key):
  # TODO: Write your code here
  closest_element = None
  closest_distance = -1

  start, end = 0, len(arr) - 1

  while start <= end:
    mid = (start + end) // 2
    if arr[mid] == key:
      return key

    if not closest_element or abs(key - arr[mid]) < closest_distance:
      closest_element = arr[mid]
      closest_distance = abs(key - arr[mid])

    elif arr[mid] > key:
      end = mid - 1
    else:
      start = mid + 1


  return closest_element


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()

"""SOLUTION

def search_min_diff_element(arr, key):
  if key < arr[0]:
    return arr[0]
  n = len(arr)
  if key > arr[n - 1]:
    return arr[n - 1]

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      return arr[mid]

  # at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array
  # return the element which is closest to the 'key'
  if (arr[start] - key) < (key - arr[end]):
    return arr[start]
  return arr[end]


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()

"""