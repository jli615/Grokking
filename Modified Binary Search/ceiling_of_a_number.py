"""MY CODE"""

def search_ceiling_of_a_number(arr, key):
  # TODO: Write your code here
  start, end = 0, len(arr) - 1
  curr, curr_index = float("inf"), -1

  while start <= end:
    mid = (start + end) // 2

    if arr[mid] == key:
      return mid
    elif arr[mid] < key:
      start = mid + 1
    else:
      if arr[mid] < curr:
        curr_index = mid
        curr = arr[mid]
        end = mid - 1

  return curr_index


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

"""SOLUTION

def search_ceiling_of_a_number(arr, key):
  n = len(arr)
  if key > arr[n - 1]:  # if the 'key' is bigger than the biggest element
    return -1

  start, end = 0, n - 1
  while start <= end:
    mid = start + (end - start) // 2
    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:  # found the key
      return mid

  # since the loop is running until 'start <= end', so at the end of the while loop, 'start == end+1'
  # we are not able to find the element in the given array, so the next big number will be arr[start]
  return start


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()

"""