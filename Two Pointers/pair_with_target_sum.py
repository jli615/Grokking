"""MY CODE"""

def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  start, end = 0, len(arr) - 1
  while start != end and arr[start] + arr[end] != target_sum:
    if arr[start] + arr[end] < target_sum:
      start += 1
    else:
      end -= 1
  
  if start == end:
    return [-1, -1]
  return [start, end]

"""SOLUTION

def pair_with_targetsum(arr, target_sum):
  left, right = 0, len(arr) - 1
  while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
      return [left, right]

    if target_sum > current_sum:
      left += 1  # we need a pair with a bigger sum
    else:
      right -= 1  # we need a pair with a smaller sum
  return [-1, -1]


def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))


main()

"""