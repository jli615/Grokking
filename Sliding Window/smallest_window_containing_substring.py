"""MY CODE"""

def find_substring(str1, pattern):
  # define environmental variables
  windowStart = 0
  matched = 0
  current_letters = {}
  smallest_length = float("inf")
  smallest_substring = ""

  # set reference dictionary
  reference = {}
  for letter in pattern:
    if letter not in reference.keys():
      reference[letter] = 0
    reference[letter] += 1

  # slide window over by 1
  for windowEnd in range(len(str1)):
    
    # track current letter
    current = str1[windowEnd]
    if current not in current_letters.keys():
      current_letters[current] = 0
    current_letters[current] += 1
    if current in reference.keys() and current_letters[current] == reference[current]:
      matched += 1
    
    # check condition
    while matched == len(reference):
      if windowEnd - windowStart + 1 < smallest_length:
        smallest_length = windowEnd - windowStart + 1
        smallest_substring = str1[windowStart:windowEnd] + str1[windowEnd]

      #take away characters
      start = str1[windowStart]
      current_letters[start] -= 1
      if start in reference.keys() and current_letters[start] == reference[start] - 1:
        matched -= 1
      if current_letters[start] == 0:
        del current_letters[start]
      
      windowStart += 1
  
  return smallest_substring

      
"""SOLUTION

def find_substring(str1, pattern):
  # define environmental variables
  windowStart = 0
  matched = 0
  current_letters = {}
  smallest_length = float("inf")
  smallest_substring = ""

  # set reference dictionary
  reference = {}
  for letter in pattern:
    if letter not in reference.keys():
      reference[letter] = 0
    reference[letter] += 1

  # slide window over by 1
  for windowEnd in range(len(str1)):
    
    # track current letter
    current = str1[windowEnd]
    if current not in current_letters.keys():
      current_letters[current] = 0
    current_letters[current] += 1
    if current in reference.keys() and current_letters[current] == reference[current]:
      matched += 1
    
    # check condition
    while matched == len(reference):
      if windowEnd - windowStart + 1 < smallest_length:
        smallest_length = windowEnd - windowStart + 1
        smallest_substring = str1[windowStart:windowEnd] + str1[windowEnd]

      #take away characters
      start = str1[windowStart]
      current_letters[start] -= 1
      if start in reference.keys() and current_letters[start] == reference[start] - 1:
        matched -= 1
      if current_letters[start] == 0:
        del current_letters[start]
      
      windowStart += 1
  
  return smallest_substring

      



"""