"""MY CODE"""

def find_permutation(str1, pattern):
  # TODO: Write your code here

  #enviornment variables
  windowStart, matched = 0,0

  #create reference dictionary
  reference_letters = {}
  for letter in pattern:
    if letter not in reference_letters.keys():
      reference_letters[letter] = 0
    reference_letters[letter] += 1

  #for loop
  for windowEnd in range(len(str1)):
    #add next value
    end_char = str1[windowEnd]
    if end_char in reference_letters.keys():
      reference_letters[end_char] -= 1
      if reference_letters[end_char] == 0:
        matched += 1
    
    #check condition
    if matched == len(reference_letters.keys()):
      return True

    #shift window start
    if windowEnd >= len(pattern) - 1:
      start_char = str1[windowStart]
      if start_char in reference_letters.keys():
        reference_letters[start_char] += 1
        if reference_letters[start_char] == 1:
          matched -= 1
      windowStart += 1
    
  return False
  
  
  
  """MY CODE
  #create reference dictionary
  reference_letters = {}
  for letter in pattern:
    if letter not in reference_letters.keys():
      reference_letters[letter] = 0
    reference_letters[letter] += 1

  #define environmental variables
  windowStart = 0
  output = False
  length = len(pattern)

  #create counters
  letter_count = {}

  #for loop
  windowEnd = 0
  while windowEnd < len(str1):
    
    #add next value(s)
    while windowEnd - windowStart + 1 <= length:
      end_char = str1[windowEnd]
      if end_char not in letter_count.keys():
        letter_count[end_char] = 0
      letter_count[end_char] += 1
      windowEnd += 1

    #check if condition
    if letter_count == reference_letters:
      output = True

    #remove start
    start_char = str1[windowStart]
    letter_count[start_char] -= 1
    if letter_count[start_char] == 0:
      del letter_count[start_char]
    windowStart += 1

  return output
  """

  """SOLUTION
  
  def find_permutation(str1, pattern):
  window_start, matched = 0, 0
  char_frequency = {}

  for chr in pattern:
    if chr not in char_frequency:
      char_frequency[chr] = 0
    char_frequency[chr] += 1

  # our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for window_end in range(len(str1)):
    right_char = str1[window_end]
    if right_char in char_frequency:
      # decrement the frequency of matched character
      char_frequency[right_char] -= 1
      if char_frequency[right_char] == 0:
        matched += 1

    if matched == len(char_frequency):
      return True

    # shrink the window by one character
    if window_end >= len(pattern) - 1:
      left_char = str1[window_start]
      window_start += 1
      if left_char in char_frequency:
        if char_frequency[left_char] == 0:
          matched -= 1
        char_frequency[left_char] += 1

  return False


def main():
  print('Permutation exist: ' + str(find_permutation("oidbcaf", "abc")))
  print('Permutation exist: ' + str(find_permutation("odicf", "dc")))
  print('Permutation exist: ' + str(find_permutation("bcdxabcdy", "bcdyabcdx")))
  print('Permutation exist: ' + str(find_permutation("aaacb", "abc")))


main()

  """