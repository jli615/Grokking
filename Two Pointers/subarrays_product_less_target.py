"""MY CODE"""

def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  
  # iterate through each left index
  for right in range(len(arr)):

    # adjust product 
    product *= arr[right]

    # adjust left pointer accordingly
    while product >= target:
      product = product / arr[left]
      left += 1

    for k in range(left, right + 1):
      result.append(arr[k:right + 1])

  return result
  
  
  """
  result = []

  # iterate through each left index
  for i in range(len(arr)):

    # define pointers, counters
    right = i + 1
    product = arr[i]

    # move right pointer until we hit ceiling
    while right < len(arr) and product * arr[right] < target:
      product *= arr[right]
      right += 1

    for k in range(i + 1, right + 1):
      result.append(arr[i:k])

  return result
  """

  """SOOLUTION
  
  from collections import deque


def find_subarrays(arr, target):
  result = []
  product = 1
  left = 0
  for right in range(len(arr)):
    product *= arr[right]
    while (product >= target and left <= right):
      product /= arr[left]
      left += 1
    # since the product of all numbers from left to right is less than the target therefore,
    # all subarrays from left to right will have a product less than the target too; to avoid
    # duplicates, we will start with a subarray containing only arr[right] and then extend it
    temp_list = deque()
    for i in range(right, left-1, -1):
      temp_list.appendleft(arr[i])
      result.append(list(temp_list))
  return result


def main():
  print(find_subarrays([2, 5, 3, 10], 30))
  print(find_subarrays([8, 2, 6, 5], 50))


main()

  """