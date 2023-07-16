"""MY CODE"""

def find_duplicate(nums):
  # from 1 to n, so shift index back 1
  # define iterate and iterate through
  i = 0
  while i < len(nums):
    # assign current num to variable
    if nums[i] != i:
      j = nums[i]
      # if nums[j] and nums[i] don't match up, swap
      if nums[j] != nums[i]:
        nums[i], nums[j] = nums[j], nums[i]
      else:
        return nums[j]
    else:
      i += 1

  return nums[0]

"""SOLUTION


def find_duplicate(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      j = nums[i] - 1
      if nums[i] != nums[j]:
        nums[i], nums[j] = nums[j], nums[i]  # swap
      else:  # we have found the duplicate
        return nums[i]
    else:
      i += 1

  return -1


def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()

"""