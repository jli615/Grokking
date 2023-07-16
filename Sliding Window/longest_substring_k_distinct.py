"""MY CODE"""

def longest_substring_with_k_distinct(str1, k):
  # TODO: Write your code here
  windowStart = 0
  letter_count = {}

  max_count = 0

  for windowEnd in range(len(str1)):

    #moving the letters
    letter = str1[windowEnd]
    if letter not in letter_count.keys():
      letter_count[letter] = 0
    letter_count[letter] += 1


    while len(letter_count.keys()) > k:
      letter_count[str1[windowStart]] -= 1
      if letter_count[str1[windowStart]] == 0:
        del letter_count[str1[windowStart]]
      windowStart += 1
    
    max_count = max(max_count, windowEnd - windowStart + 1)
    
  return max_count

"""SOLUTION

def longest_substring_with_k_distinct(str1, k):
  window_start = 0
  max_length = 0
  char_frequency = {}

  # in the following loop we'll try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char not in char_frequency:
      char_frequency[right_char] = 0
    char_frequency[right_char] += 1

    # shrink the sliding window, until we are left with 'k' distinct characters in the char_frequency
    while len(char_frequency) > k:
      left_char = str1[window_start]
      char_frequency[left_char] -= 1
      if char_frequency[left_char] == 0:
        del char_frequency[left_char]
      window_start += 1  # shrink the window
    # remember the maximum length so far
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 2)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("araaci", 1)))
  print("Length of the longest substring: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()

"""