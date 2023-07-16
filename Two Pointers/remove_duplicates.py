"""MY CODE"""

def remove_duplicates(arr):
  # TODO: Write your code here
  i, insert_unique = 0, 1
  while i < len(arr):
    if arr[i] != arr[insert_unique - 1]:
      arr[insert_unique] = arr[i]
      insert_unique += 1
    i += 1
  return insert_unique
    


  """
  left, right = 0, len(arr) - 1
  remove_next = False
  count = 0
  
  while left <= right:
    if remove_next:
      temp = arr.pop(left)
      arr.append(temp)
      right -= 1
      left -= 1
    else:
      count += 1
    
    if arr[left] == arr[left + 1]:
      remove_next = True
    else:
      remove_next = False
    left += 1
  return count
  """


"""SOLUTION

def remove_duplicates(arr):
  # index of the next non-duplicate element
  next_non_duplicate = 1

  i = 0
  while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
      arr[next_non_duplicate] = arr[i]
      next_non_duplicate += 1
    i += 1

  return next_non_duplicate


def main():
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))


main()

"""