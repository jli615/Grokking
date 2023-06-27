"""MY CODE"""

from collections import deque

def can_construct(originalSeq, sequences):
  sorted_order = []
  # TODO: Write your code here
  graph = {i:[] for i in originalSeq}
  in_degrees = {i:0 for i in originalSeq}
  for sequence in sequences:
    for i in range(len(sequence) - 1):
      parent, child = sequence[i], sequence[i+1]
      graph[parent].append(child)
      in_degrees[child] += 1

  queue = deque()
  for vertex, degree in in_degrees.items():
    if degree == 0:
      queue.append(vertex)

  while queue:
    if len(queue) > 1:
      return False
    else:
      vertex = queue.popleft()
      sorted_order.append(vertex)
      for child in graph[vertex]:
        in_degrees[child] -= 1
        if in_degrees[child] == 0:
          queue.append(child)

  if len(sorted_order) != len(originalSeq):
    return False
  else:
    return True


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()


"""SOLUTION


from collections import deque


def can_construct(originalSeq, sequences):
  sortedOrder = []
  if len(originalSeq) <= 0:
    return False

  # a. Initialize the graph
  inDegree = {}  # count of incoming edges
  graph = {}  # adjacency list graph
  for sequence in sequences:
    for num in sequence:
      inDegree[num] = 0
      graph[num] = []

  # b. Build the graph
  for sequence in sequences:
    for i in range(1, len(sequence)):
      parent, child = sequence[i - 1], sequence[i]
      graph[parent].append(child)
      inDegree[child] += 1

  # if we don't have ordering rules for all the numbers we'll not able to uniquely construct the sequence
  if len(inDegree) != len(originalSeq):
    return False

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    if len(sources) > 1:
      return False  # more than one sources mean, there is more than one way to reconstruct the sequence
    if originalSeq[len(sortedOrder)] != sources[0]:
      # the next source(or number) is different from the original sequence
      return False

    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # if sortedOrder's size is not equal to original sequence's size, there is no unique way to construct
  return len(sortedOrder) == len(originalSeq)


def main():
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
  print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
  print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()
"""