"""MY CODE"""

def find_corrupt_numbers(nums):
  # need to process entire array
  # define and iterate through
  i = 0
  while i < len(nums):
    # define current number
    j = nums[i] - 1
    # if the number at index j is not equal to j
    if nums[j] != nums[i]:
      # swap
      nums[j], nums[i] = nums[i], nums[j]
    # or else iterate through
    else:
      i += 1
    
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]

  return [-1, -1]

"""SOLUTION

def find_corrupt_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]

  return [-1, -1]


def main():
  print(find_corrupt_numbers([3, 1, 2, 5, 2]))
  print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))


main()

"""