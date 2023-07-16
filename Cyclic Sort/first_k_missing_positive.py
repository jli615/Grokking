"""MY CODE"""

def find_first_k_missing_positive(nums, k):
  missingNumbers = []
  # plan: same algorithm but at then end, just check through in a unique way
  # add k 0's to nums as buffer!
  for _ in range(k):
    nums.append(0)

  # cyclic sort algorithm
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
  
  # check through
  index = 0
  while k > 0:
    if nums[index] != index + 1:
      missingNumbers.append(index + 1)
      k -= 1
    index += 1

  return missingNumbers

"""SOLUTION


def find_first_k_missing_positive(nums, k):
  n = len(nums)
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]  # swap
    else:
      i += 1

  missingNumbers = []
  extraNumbers = set()
  for i in range(n):
    if len(missingNumbers) < k:
      if nums[i] != i + 1:
        missingNumbers.append(i + 1)
        extraNumbers.add(nums[i])

  # add the remaining missing numbers
  i = 1
  while len(missingNumbers) < k:
    candidateNumber = i + n
    # ignore if the array contains the candidate number
    if candidateNumber not in extraNumbers:
      missingNumbers.append(candidateNumber)
    i += 1

  return missingNumbers


def main():
  print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  print(find_first_k_missing_positive([-2, -3, 4], 2))


main()

"""