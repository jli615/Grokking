"""MY CODE"""

def find_missing_numbers(nums):
  missingNumbers = []
  # define itereator
  i = 0
  # iterate through
  while i < len(nums):
    # define current number
    j = nums[i]
    # check to see if the index j belongs in already has a correct 
    if nums[j - 1] == j:
      i += 1
    # swap
    else:
      nums[j-1], nums[i] = nums[i], nums[j-1]

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i+1)

  return missingNumbers

"""SOLUTION

def find_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []

  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)

  return missingNumbers


def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()

"""