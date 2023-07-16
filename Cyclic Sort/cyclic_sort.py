"""MY CODE"""

def cyclic_sort(nums):
  # TODO: Write your code here

  # define counter
  i = 0

  # iterate through
  while i < len(nums):

    # while the number in the first position isn't right, swap
    if nums[i] != i + 1:

      # swap
      temp = nums[i]
      nums[i] = nums[temp - 1]
      nums[temp - 1] = temp

    # increment
    else:
      i += 1

  return nums

"""SOLUTION

def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1
  return nums


def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()

"""