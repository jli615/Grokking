"""MY CODE"""

from collections import deque

class parenthesesString:
  def __init__(self, str, open_count, closed_count):
    self.str = str
    self.open_count = open_count
    self.closed_count = closed_count

def generate_valid_parentheses(num):
  result = []

  queue = deque()
  queue.append(parenthesesString("", 0, 0))

  while queue:
    # for all current permutations
    seq = queue.popleft()
    # if entire string is reached
    if seq.open_count == num and seq.closed_count == num:
      result.append(seq.str)
    else:
      # option 1: open parentheses
      if seq.open_count < num:
        queue.append(parenthesesString(seq.str + "(", seq.open_count + 1, seq.closed_count))
      # option 2: closed parentheses
      if seq.open_count > seq.closed_count:
        queue.append(parenthesesString(seq.str + ")", seq.open_count, seq.closed_count + 1))

  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()

"""SOLUTION

from collections import deque


class ParenthesesString:
  def __init__(self, str, openCount, closeCount):
    self.str = str
    self.openCount = openCount
    self.closeCount = closeCount


def generate_valid_parentheses(num):
  result = []
  queue = deque()
  queue.append(ParenthesesString("", 0, 0))
  while queue:
    ps = queue.popleft()
    # if we've reached the maximum number of open and close parentheses, add to the result
    if ps.openCount == num and ps.closeCount == num:
      result.append(ps.str)
    else:
      if ps.openCount < num:  # if we can add an open parentheses, add it
        queue.append(ParenthesesString(
          ps.str + "(", ps.openCount + 1, ps.closeCount))

      if ps.openCount > ps.closeCount:  # if we can add a close parentheses, add it
        queue.append(ParenthesesString(ps.str + ")",
                                       ps.openCount, ps.closeCount + 1))

  return result


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()

"""