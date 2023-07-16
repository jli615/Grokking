"""MY CODE"""

def dutch_flag_sort(arr):
  # define pointers
  insert_one = 0
  insert_two = 0

  # define tracker
  curr_index = 0

  # iterate through each element
  while curr_index < len(arr):

    # define current character
    current = arr.pop(curr_index)


    # different cases
    if current == 0:
      #arr = [0] + arr
      arr.insert(0, 0)
      insert_one += 1
      insert_two += 1
    elif current == 1:
      #arr = arr[0:insert_one] + [1] + arr[insert_one:]
      arr.insert(insert_one, 1)
      insert_two += 1
    else:
      #arr = arr[0:insert_two] + [2] + arr[insert_two:]
      arr.insert(insert_two, 2)

    # shift current index forward
    curr_index += 1

  return 

"""SOLUTION

def dutch_flag_sort(arr):
  # all elements < low are 0, and all elements > high are 2
  # all elements from >= low < i are 1
  low, high = 0, len(arr) - 1
  i = 0
  while(i <= high):
    if arr[i] == 0:
      arr[i], arr[low] = arr[low], arr[i]
      # increment 'i' and 'low'
      i += 1
      low += 1
    elif arr[i] == 1:
      i += 1
    else:  # the case for arr[i] == 2
      arr[i], arr[high] = arr[high], arr[i]
      # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
      high -= 1


def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)


main()

"""