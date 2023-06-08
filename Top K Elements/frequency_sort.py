"""MY CODE"""

from heapq import *

def sort_character_by_frequency(str):
  # TODO: Write your code here
  output = ""

  freq_count = {}
  for char in str:
    if char not in freq_count.keys():
      freq_count[char] = 0
    freq_count[char] += 1
  
  max_heap = []
  for char in freq_count.keys():
    heappush(max_heap, (-freq_count[char], char))

  while max_heap:
    count, char = heappop(max_heap)
    count *= -1
    temp = char * count
    output += temp

  return output


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()

"""SOLUTION
from heapq import *


def sort_character_by_frequency(str):

  # find the frequency of each character
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  # build a string, appending the most occurring characters first
  sortedString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    for _ in range(-frequency):
      sortedString.append(char)

  return ''.join(sortedString)


def main():

  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
  print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()


"""