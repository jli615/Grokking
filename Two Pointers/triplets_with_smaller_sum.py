"""MY CODE"""

def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  # TODO: Write your code here
  
  # iterate through each "first element" (i) in the triple
  for i in range(len(arr) - 2):

    # define pointers
    left, right = i + 1, len(arr) - 1

    # check through all of them
    while left < right:
      if arr[i] + arr[left] + arr[right] < target:
        count += right - left
        left += 1
      else:
        right -= 1

  return count

"""SOLUTION

def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  for i in range(len(arr)-2):
    count += search_pair(arr, target - arr[i], i)
  return count


def search_pair(arr, target_sum, first):
  count = 0
  left, right = first + 1, len(arr) - 1
  while (left < right):
    if arr[left] + arr[right] < target_sum:  # found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
      # left and right to get a sum less than the target sum
      count += right - left
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum
  return count


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()

"""