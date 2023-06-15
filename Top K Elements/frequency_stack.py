"""MY CODE"""

from heapq import *

class StackElement:
  def __init__(self, num, count, order):
    self.num = num
    self.count = count
    self.order = order

  def __lt__(self, obj):
    if self.count != obj.count:
      return self.count > obj.count
    else:
      return self.order > obj.order

class FrequencyStack:

  def __init__(self):
    self.heap = []
    self.frequency = {}
    self.count = 0

  def push(self, num):
    # TODO: Write your code here
    frequency = self.frequency.get(num, 0)
    self.frequency[num] = frequency + 1
    heappush(self.heap, StackElement(num, self.frequency[num], self.count))
    self.count += 1

  def pop(self):
    stack_element = heappop(self.heap)
    most_freq_num = stack_element.num
    return most_freq_num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()

"""SOLUTION

from heapq import *


class Element:

  def __init__(self, number, frequency, sequenceNumber):
    self.number = number
    self.frequency = frequency
    self.sequenceNumber = sequenceNumber

  def __lt__(self, other):
    # higher frequency wins
    if self.frequency != other.frequency:
      return self.frequency > other.frequency
    # if both elements have same frequency, return the element that was pushed later
    return self.sequenceNumber > other.sequenceNumber


class FrequencyStack:
  sequenceNumber = 0
  maxHeap = []
  frequencyMap = {}

  def push(self, num):
    self.frequencyMap[num] = self.frequencyMap.get(num, 0) + 1
    heappush(self.maxHeap, Element(
      num, self.frequencyMap[num], self.sequenceNumber))
    self.sequenceNumber += 1

  def pop(self):
    num = heappop(self.maxHeap).number
    # decrement the frequency or remove if this is the last number
    if self.frequencyMap[num] > 1:
      self.frequencyMap[num] -= 1
    else:
      del self.frequencyMap[num]

    return num


def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()

"""