"""MY CODE"""

from collections import deque

def find_permutations(nums):
  results = []
  
  # define queue
  permutations = deque()
  permutations.append([])
  length = len(nums)

  # iterate for each number in the list
  for temp_len in range(length):
    current_num = nums[temp_len]

    # iterate for each permutation in the current list
    queue_length = len(permutations)
    for j in range(queue_length):

      # get current permutation out
      old_perm = permutations.popleft()
      for i in range(temp_len + 1):
        temp_perm = list(old_perm)
        temp_perm.insert(i, current_num)        
        if temp_len == length - 1:
          results.append(temp_perm)
        else:
          permutations.append(temp_perm)

  return results
    
def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

"""SOLUTION

from collections import deque


def find_permutations(nums):
  numsLength = len(nums)
  result = []
  permutations = deque()
  permutations.append([])
  for currentNumber in nums:
    # we will take all existing permutations and add the current number to create new permutations
    n = len(permutations)
    for _ in range(n):
      oldPermutation = permutations.popleft()
      # create a new permutation by adding the current number at every position
      for j in range(len(oldPermutation)+1):
        newPermutation = list(oldPermutation)
        newPermutation.insert(j, currentNumber)
        if len(newPermutation) == numsLength:
          result.append(newPermutation)
        else:
          permutations.append(newPermutation)

  return result


def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

"""