"""MY CODE"""

def find_string_anagrams(str1, pattern):
  result_indexes = []
  # TODO: Write your code here

  #environmental variables
  windowStart = 0
  letter_counter = {}
  matched = 0

  #letter counter - how many total letters in the pattern
  reference_letters = {}
  for letter in pattern:
    if letter not in reference_letters.keys():
      reference_letters[letter] = 0
    reference_letters[letter] += 1

  #loop
  for windowEnd in range(len(str1)):
    #count letter
    end_char = str1[windowEnd]
    if end_char not in letter_counter.keys():
      letter_counter[end_char] = 0
    letter_counter[end_char] += 1
    if letter_counter[end_char] == reference_letters[end_char]:
      matched += 1

    #check against reference list
    if matched == len(reference_letters.keys()):
      result_indexes.append(windowStart)
    
    #remove letter
    if windowEnd - windowStart + 1 >= len(pattern):
      start_char = str1[windowStart]
      if letter_counter[start_char] == reference_letters[start_char]:
        matched -= 1
      letter_counter[start_char] -= 1
      windowStart += 1

  return result_indexes

"""SOLUTION

def find_string_anagrams(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  result_indices = []
  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # Decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):  # Have we found an anagram?
      result_indices.append(window_start)

    # Shrink the sliding window
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        char_frequency[left_char] += 1  # Put the character back

  return result_indices


def main():
  print(find_string_anagrams("ppqp", "pq"))
  print(find_string_anagrams("abbcabc", "abc"))


main()

"""