"""MY CODE"""

from heapq import *


def rearrange_string(str):
  # TODO: Write your code here
  freq_count = {}
  for char in str:
    if char not in freq_count.keys():
      freq_count[char] = 0
    freq_count[char] += 1

  heap = []
  for key, count in freq_count.items():
    heappush(heap, (-count, key))

  if - heap[0][0] > (len(str) + 1) / 2:
    return ""

  characters = []
  while heap:
    count, char = heappop(heap)
    count *= -1
    characters = characters + count * [char]

  split = (len(str) + 1) // 2
  first_half = characters[:split]
  second_half = characters[split:]

  outcome = []
  for i in range(len(second_half)):
    outcome.append(first_half[i])
    outcome.append(second_half[i])
  
  if len(first_half) > len(second_half):
    outcome.append(first_half[-1])

  return "".join(outcome)

def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()

"""SOLUTION

from heapq import *


def rearrange_string(str):
  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  previousChar, previousFrequency = None, 0
  resultString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    # add the previous entry back in the heap if its frequency is greater than zero
    if previousChar and -previousFrequency > 0:
      heappush(maxHeap, (previousFrequency, previousChar))
    # append the current character to the result string and decrement its count
    resultString.append(char)
    previousChar = char
    previousFrequency = frequency+1  # decrement the frequency

  # if we were successful in appending all the characters to the result string, return it
  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Rearranged string:  " + rearrange_string("aappp"))
  print("Rearranged string:  " + rearrange_string("Programming"))
  print("Rearranged string:  " + rearrange_string("aapa"))


main()

"""