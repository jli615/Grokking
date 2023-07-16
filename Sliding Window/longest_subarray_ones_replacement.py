"""MY CODE"""

def length_of_longest_substring(arr, k):
  # TODO: Write your code here
  #env variables
  windowStart = 0
  max_len = 0

  #counters
  number_counter = {0: 0, 1: 0}

  for windowEnd in range(len(arr)):

    #account for end character
    end_char = arr[windowEnd]
    number_counter[end_char] += 1

    #check for condition and shift start forwards
    while number_counter[0] > k:
      start_char = arr[windowStart]
      number_counter[start_char] -= 1
      windowStart += 1

    #check max of current vs maximum
    max_len = max(max_len, windowEnd - windowStart + 1)
  
  return max_len

"""SOLUTION

def length_of_longest_substring(arr, k):
  window_start, max_length, max_ones_count = 0, 0, 0

  # Try to extend the range [window_start, window_end]
  for window_end in range(len(arr)):
    if arr[window_end] == 1:
      max_ones_count += 1

    # Current window size is from window_start to window_end, overall we have a maximum of 1s
    # repeating 'max_ones_count' times, this means we can have a window with 'max_ones_count' 1s
    # and the remaining are 0s which should replace with 1s.
    # now, if the remaining 0s are more than 'k', it is the time to shrink the window as we
    # are not allowed to replace more than 'k' 0s
    if (window_end - window_start + 1 - max_ones_count) > k:
      if arr[window_start] == 1:
        max_ones_count -= 1
      window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
  print(length_of_longest_substring(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))


main()

"""