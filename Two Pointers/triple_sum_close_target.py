"""MY CODE"""

def triplet_sum_close_to_target(arr, target_sum):
  # TODO: Write your code here
  arr.sort()

  closest = float("inf")
  closest_diff = float("inf")

  for i in range(len(arr)):
    triple_sum = search_pairs(arr, i+1, target_sum - arr[i]) + arr[i]
    if abs(triple_sum - target_sum) < abs(closest_diff) or (abs(triple_sum - target_sum) == closest_diff and triple_sum < target_sum):
      closest_diff = triple_sum - target_sum
      closest = triple_sum

  return closest

def search_pairs(arr, left, target_sum):

  # define pointer
  right = len(arr) - 1

  # define trackers
  closest_sum = float("inf")
  diff = float("inf")

  while left < right:
    curr_sum = arr[left] + arr[right]
    if curr_sum == target_sum:
      return curr_sum
    elif curr_sum < target_sum:
      if abs(curr_sum - target_sum) <= abs(diff):
        closest_sum = curr_sum
        diff = curr_sum - target_sum
      left += 1
    else:
      if abs(curr_sum - target_sum) < abs(diff):
        closest_sum = curr_sum
        diff = curr_sum - target_sum
      right -= 1
  
  return closest_sum

"""SOLUTION

import math


def triplet_sum_close_to_target(arr, target_sum):
  arr.sort()
  smallest_difference = math.inf
  for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while (left < right):
      target_diff = target_sum - arr[i] - arr[left] - arr[right]
      if target_diff == 0:  # we've found a triplet with an exact sum
        return target_sum  # return sum of all the numbers

      # the second part of the following 'if' is to handle the smallest sum when we have more than one solution
      if abs(target_diff) < abs(smallest_difference) or (abs(target_diff) == abs(smallest_difference) and target_diff > smallest_difference):
        smallest_difference = target_diff  # save the closest and the biggest difference

      if target_diff > 0:
        left += 1  # we need a triplet with a bigger sum
      else:
        right -= 1  # we need a triplet with a smaller sum

  return target_sum - smallest_difference


def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()

"""