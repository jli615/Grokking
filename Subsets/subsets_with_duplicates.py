"""MY CODE"""

def find_subsets(nums):
  list.sort(nums)
  subsets = []
  subsets.append([])
  start_index, end_index = 0, 0
  # iterate through
  for i in range(len(nums)):
    start_index = 0
    # if duplicate
    if i > 0 and nums[i] == nums[i - 1]:
      start_index = end_index + 1
    end_index = len(subsets) - 1
    for j in range(start_index, end_index + 1):
      temp = subsets[j]
      subsets.append(temp + [nums[i]])
          
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

"""SOLUTION

def find_subsets(nums):
  # sort the numbers to handle duplicates
  list.sort(nums)
  subsets = []
  subsets.append([])
  startIndex, endIndex = 0, 0
  for i in range(len(nums)):
    startIndex = 0
    # if current and the previous elements are same, create new subsets only from the subsets
    # added in the previous step
    if i > 0 and nums[i] == nums[i - 1]:
      startIndex = endIndex + 1
    endIndex = len(subsets) - 1
    for j in range(startIndex, endIndex+1):
      # create a new subset from the existing subset and add the current element to it
      set1 = list(subsets[j])
      set1.append(nums[i])
      subsets.append(set1)
  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

"""