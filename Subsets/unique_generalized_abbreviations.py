"""MY CODE"""

from collections import deque

class abbreviation:

  def __init__(self, string, count):
    self.string = string
    self.count = count

def generate_generalized_abbreviation(word):
  result = []

  # declare initial stuff including queue
  queue = deque()
  queue.append(abbreviation("", 0))

  # for character in word
  for char in word:

  # for abbreviation in queue
    n = len(queue)
    for i in range(n):
      prev_abbrev = queue.popleft()
      # option 1: add to count and move on
      queue.append(abbreviation(prev_abbrev.string, prev_abbrev.count + 1))
      # option 2: add to string
      new_string = prev_abbrev.string
      # if there is an accumulated count, then add previous count to string as well
      if prev_abbrev.count > 0:
        new_string += str(prev_abbrev.count)
      new_string += str(char)
      queue.append(abbreviation(new_string, 0))

  # at the very end: go through queue, add to result. if there is any with existing count, add that to end
  while queue:
    abbrev = queue.popleft()
    if abbrev.count > 0:
      result.append(abbrev.string + str(abbrev.count))
    else:
      result.append(abbrev.string)


  return result


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()

"""SOLUTION

from collections import deque


class AbbreviatedWord:

  def __init__(self, str, start,  count):
    self.str = str
    self.start = start
    self.count = count


def generate_generalized_abbreviation(word):
  wordLen = len(word)
  result = []
  queue = deque()
  queue.append(AbbreviatedWord(list(), 0, 0))
  while queue:
    abWord = queue.popleft()
    if abWord.start == wordLen:
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))
      result.append(''.join(abWord.str))
    else:
      # continue abbreviating by incrementing the current abbreviation count
      queue.append(AbbreviatedWord(list(abWord.str),
                                   abWord.start + 1, abWord.count + 1))

      # restart abbreviating, append the count and the current character to the string
      if abWord.count != 0:
        abWord.str.append(str(abWord.count))

      newWord = list(abWord.str)
      newWord.append(word[abWord.start])
      queue.append(AbbreviatedWord(newWord, abWord.start + 1, 0))

  return result

def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))

main()

"""