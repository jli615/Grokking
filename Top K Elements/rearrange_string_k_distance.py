"""MY CODE"""

from heapq import *
from collections import deque

def reorganize_string(str, k):
  # TODO: Write your code here
  freq_count = {}
  for char in str:
    if char not in freq_count.keys():
      freq_count[char] = 0
    freq_count[char] += 1
  
  heap = []
  for char, count in freq_count.items():
    heappush(heap, (-count, char))

  # base case to rule a few out
  if len(heap) < k or -heap[0][0] > ((len(str)/ k) + 1):
    return ""

  queue = deque()
  output = ""
  while heap:
    count, char = heappop(heap)
    count += 1
    output += char
    queue.append((count, char))
    if len(queue) == k:
      queue_count, queue_char = queue.popleft()
      if queue_count < 0:
        heappush(heap, (queue_count, queue_char))

  return output if len(output) == len(str) else ""
  
    



def main():
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()

"""SOLUTION

from heapq import *
from collections import deque


def reorganize_string(str, k):
  if k <= 1: 
    return str

  charFrequencyMap = {}
  for char in str:
    charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

  maxHeap = []
  # add all characters to the max heap
  for char, frequency in charFrequencyMap.items():
    heappush(maxHeap, (-frequency, char))

  queue = deque()
  resultString = []
  while maxHeap:
    frequency, char = heappop(maxHeap)
    # append the current character to the result string and decrement its count
    resultString.append(char)
    # decrement the frequency and append to the queue
    queue.append((char, frequency+1))
    if len(queue) == k:
      char, frequency = queue.popleft()
      if -frequency > 0:
        heappush(maxHeap, (frequency, char))

  # if we were successful in appending all the characters to the result string, return it
  return ''.join(resultString) if len(resultString) == len(str) else ""


def main():
  print("Reorganized string: " + reorganize_string("Programming", 3))
  print("Reorganized string: " + reorganize_string("mmpp", 2))
  print("Reorganized string: " + reorganize_string("aab", 2))
  print("Reorganized string: " + reorganize_string("aapa", 3))


main()

"""