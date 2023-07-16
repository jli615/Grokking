"""MY CODE"""

def fruits_into_baskets(fruits):
  # TODO: Write your code here
  windowStart = 0
  letter_count = {}
  max_num = 0

  for windowEnd in range(len(fruits)):
    curr_char = fruits[windowEnd]
    if curr_char not in letter_count.keys():
      letter_count[curr_char] = 0
    letter_count[curr_char] += 1

    while len(letter_count) > 2:
      curr_start = fruits[windowStart]
      letter_count[curr_start] -= 1
      if letter_count[curr_start] == 0:
        del letter_count[curr_start]
      windowStart += 1
    
    max_num = max(max_num, windowEnd - windowStart + 1)

  return max_num

"""SOLUTION

def fruits_into_baskets(fruits):
  window_start = 0
  max_length = 0
  fruit_frequency = {}

  # try to extend the range [window_start, window_end]
  for window_end in range(len(fruits)):
    right_fruit = fruits[window_end]
    if right_fruit not in fruit_frequency:
      fruit_frequency[right_fruit] = 0
    fruit_frequency[right_fruit] += 1

    # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
    while len(fruit_frequency) > 2:
      left_fruit = fruits[window_start]
      fruit_frequency[left_fruit] -= 1
      if fruit_frequency[left_fruit] == 0:
        del fruit_frequency[left_fruit]
      window_start += 1  # shrink the window
    max_length = max(max_length, window_end-window_start + 1)
  return max_length


def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()


"""