"""MY CODE"""

def non_repeat_substring(str):
  # TODO: Write your code here
  windowStart = 0
  letter_index = {}
  max_len = 0

  for windowEnd in range(len(str)):
    curr_char = str[windowEnd]
    if curr_char in letter_index.keys():
      windowStart = letter_index[curr_char] + 1
    letter_index[curr_char] = windowEnd
    max_len = max(max_len, windowEnd - windowStart + 1)

  return max_len
    
  """
  windowStart = 0
  letters = {}
  letter_count = 0
  max_len = 0

  for windowEnd in range(len(str)):
    curr_char = str[windowEnd]
    if curr_char not in letters.keys():
      letters[curr_char] = 0
    letters[curr_char] += 1
    letter_count += 1

    while letter_count > len(letters.keys()):
      letter_count -= 1
      curr_start = str[windowStart]
      letters[curr_start] -= 1
      if letters[curr_start] == 0:
        del letters[curr_start]
      windowStart += 1
    
    max_len = max(max_len, letter_count)


  return max_len
  """

  """MY CODE
  
  def non_repeat_substring(str1):
  window_start = 0
  max_length = 0
  char_index_map = {}

  # try to extend the range [windowStart, windowEnd]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    # if the map already contains the 'right_char', shrink the window from the beginning so that
    # we have only one occurrence of 'right_char'
    if right_char in char_index_map:
      # this is tricky; in the current window, we will not have any 'right_char' after its previous index
      # and if 'window_start' is already ahead of the last index of 'right_char', we'll keep 'window_start'
      window_start = max(window_start, char_index_map[right_char] + 1)
    # insert the 'right_char' into the map
    char_index_map[right_char] = window_end
    # remember the maximum length so far
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(non_repeat_substring("aabccbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abbbb")))
  print("Length of the longest substring: " + str(non_repeat_substring("abccde")))


main()

  """