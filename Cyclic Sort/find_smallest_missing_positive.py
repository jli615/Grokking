"""MY CODE"""

def find_first_smallest_missing_positive(nums):
  # order numbers as long as it is not negative, negatives will settle in in missing slots
  # define and iterate through
  i = 0
  while i < len(nums):
    # define current number
    j = nums[i] - 1
    # swap as long as they are not equal or out of range
    if j >= 0 and j < len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  # check to for first missing number
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return i + 1

"""SOLUTION

def find_first_smallest_missing_positive(nums):
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(n):
    if nums[i] != i + 1:
      return i + 1

  return len(nums) + 1


def main():
  print(find_first_smallest_missing_positive([-3, 1, 5, 4, 2]))
  print(find_first_smallest_missing_positive([3, -2, 0, 1, 2]))
  print(find_first_smallest_missing_positive([3, 2, 5, 1]))


main()


"""