"""MY CODE"""

def find_word_concatenation(str1, words):
  result_indices = []
  # TODO: Write your code here

  # environmental variables
  windowStart = 0
  word_length = len(words[0])
  total_length = word_length * len(words)

  # iterate through windowEnds
  for windowEnd in range(len(str1)):
    if windowEnd - windowStart + 1 == total_length:
      string = str1[windowStart:windowEnd + 1]
      copy_words = list(words)
      while string[0:word_length] in copy_words:
        copy_words.remove(string[0:word_length])
        string = string[word_length:]
      
      if copy_words == []:
        result_indices.append(windowStart)
      
      windowStart += 1
  
  return result_indices

"""SOLUTION

def find_word_concatenation(str1, words):
  if len(words) == 0 or len(words[0]) == 0:
    return []

  word_frequency = {}

  for word in words:
    if word not in word_frequency:
      word_frequency[word] = 0
    word_frequency[word] += 1

  result_indices = []
  words_count = len(words)
  word_length = len(words[0])

  for i in range((len(str1) - words_count * word_length)+1):
    words_seen = {}
    for j in range(0, words_count):
      next_word_index = i + j * word_length
      # Get the next word from the string
      word = str1[next_word_index: next_word_index + word_length]
      if word not in word_frequency:  # Break if we don't need this word
        break

      # Add the word to the 'words_seen' map
      if word not in words_seen:
        words_seen[word] = 0
      words_seen[word] += 1

      # No need to process further if the word has higher frequency than required
      if words_seen[word] > word_frequency.get(word, 0):
        break

      if j + 1 == words_count:  # Store index if we have found all the words
        result_indices.append(i)

  return result_indices


def main():
  print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
  print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()

"""