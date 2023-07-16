"""MY CODE"""

def circular_array_loop_exists(arr):
  # iterate through each element of the array
  for i in range(len(arr)):
    # check direction
    direction = arr[i] >= 0

    # define both pointers
    slow, fast = i, i

    # iterate through
    while slow != -1 and fast != -1:
      slow = find_next_element(arr, slow, direction)
      fast = find_next_element(arr, fast, direction)

      # just in case it is self loop
      if fast != -1:
        fast = find_next_element(arr, fast, direction)

      # check to see if fast has cycled around
      if slow == -1 or fast == -1 or slow == fast:
        break

    if slow != -1 and slow == fast:
      return True
      
  return False

def find_next_element(arr, index, is_forward):
  # check direction
  direction = arr[index] >= 0
  if direction != is_forward:
    return -1

  # update index (but keep track of old index)
  old_index = index
  index += arr[index]

  # check for rollover 
  if index >= len(arr):
    index -= len(arr)
  if index < 0:
    index += len(arr)

  # make sure it is not self loop
  if old_index == index:
    return -1
  
  return index



def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()

"""SOLUTION
def circular_array_loop_exists(arr):
  for i in range(len(arr)):
    is_forward = arr[i] >= 0  # if we are moving forward or not
    slow, fast = i, i

    # if slow or fast becomes '-1' this means we can't find cycle for this number
    while True:
      # move one step for slow pointer
      slow = find_next_index(arr, is_forward, slow)
      # move one step for fast pointer
      fast = find_next_index(arr, is_forward, fast)
      if (fast != -1):
        # move another step for fast pointer
        fast = find_next_index(arr, is_forward, fast)
      if slow == -1 or fast == -1 or slow == fast:
        break

    if slow != -1 and slow == fast:
      return True

  return False


def find_next_index(arr, is_forward, current_index):
  direction = arr[current_index] >= 0

  if is_forward != direction:
    return -1  # change in direction, return -1

  next_index = (current_index + arr[current_index]) % len(arr)

  # one element cycle, return -1
  if next_index == current_index:
    next_index = -1

  return next_index


def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()

"""