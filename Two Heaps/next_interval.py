"""MY CODE"""

from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  # initialize default result list
  result = [-1 for _ in range(len(intervals))]
  # TODO: Write your code here
  minStart = []
  minEnd = []

  # add elements into heap
  for i in range(len(intervals)):
    temp_interval = intervals[i]
    heappush(minStart, (temp_interval.start, i))
    heappush(minEnd, (temp_interval.end, i))
  
  # keep going while both minStart and minEnd are not empty
  while minStart and minEnd:
    temp_end, index = heappop(minEnd)

    # discard starts while they are less than the end
    while minStart and minStart[0][0] < temp_end:
      heappop(minStart)
    
    if minStart:
      result[index] = minStart[0][1]

  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()

"""SOLUTION

from heapq import *


class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  n = len(intervals)

  # heaps for finding the maximum start and end
  maxStartHeap, maxEndHeap = [], []

  result = [0 for x in range(n)]
  for endIndex in range(n):
    heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
    heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))

  # go through all the intervals to find each interval's next interval
  for _ in range(n):
    # let's find the next interval of the interval which has the highest 'end'
    topEnd, endIndex = heappop(maxEndHeap)
    result[endIndex] = -1  # defaults to - 1
    if -maxStartHeap[0][0] >= -topEnd:
      topStart, startIndex = heappop(maxStartHeap)
      # find the the interval that has the closest 'start'
      while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
        topStart, startIndex = heappop(maxStartHeap)
      result[endIndex] = startIndex
      # put the interval back as it could be the next interval of other intervals
      heappush(maxStartHeap, (topStart, startIndex))

  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print"Next interval indices are: " + str(result))


main()

"""